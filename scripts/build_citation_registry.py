#!/usr/bin/env python3
"""
Build data/citations.json from data/citation_facts.json + the approved Briefer snapshots.

data/citations.json is always generated — never typed by hand. The only hand-maintained
input is data/citation_facts.json, which records facts a human (or the verification pass)
confirmed by reading the decision text: download_id, a short name, and the outcome with its
pinpoint. This script never trusts decision_extracts model fields (summary_150w, outcome,
member_name, etc.) for any claim that ends up in the registry — it only uses the snapshots to
resolve citation/jurisdiction/date and the public URL, and to catch a citation_facts entry that
doesn't match a real decision.

Reads (read-only):
  ~/briefer-claude/snapshots/briefer_master.snapshot.db   (?mode=ro)
  ~/briefer-claude/snapshots/fwc-decision-public-urls.json

Writes:
  data/citations.json
  reports/missing-urls.md
  reports/duplicate-citations.md
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_DB = "file:" + str(Path.home() / "briefer-claude/snapshots/briefer_master.snapshot.db") + "?mode=ro"
URLS_JSON = Path.home() / "briefer-claude/snapshots/fwc-decision-public-urls.json"
URL_OVERRIDES = ROOT / "data" / "citation-url-overrides.json"
DEFAULT_FACTS_PATH = ROOT / "data" / "citation_facts.json"
DEFAULT_CONTENT_DIR = ROOT / "src" / "content" / "modules"
DEFAULT_OUT_PATH = ROOT / "data" / "citations.json"
MISSING_URLS_REPORT = ROOT / "reports" / "missing-urls.md"
DUPLICATES_REPORT = ROOT / "reports" / "duplicate-citations.md"
FLAGGED_REPORT = ROOT / "reports" / "flagged-authorities.md"

# Attribute values are matched as whole quoted strings so that a "/" or ">" inside a quoted
# phrase (e.g. "personal/carer's leave") does not hide the tag from this check.
CITE_TAG_RE = re.compile(r'<Cite\s+((?:[^"/>]|"[^"]*")+?)\s*/?>')
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def scan_content_for_cites(content_path):
    """Return {citation: set(module_ids)} by scanning MDX content for <Cite> usage.

    content_path may be a single .mdx file or a directory of them.
    """
    usage = {}
    mdx_files = [content_path] if content_path.is_file() else sorted(content_path.glob("*.mdx"))
    # Standalone pages (e.g. the advocacy guide) may also use <Cite>; they have no module id.
    if content_path == DEFAULT_CONTENT_DIR:
        mdx_files += sorted((ROOT / "src" / "pages").rglob("*.astro"))
    for mdx_path in mdx_files:
        text = mdx_path.read_text()
        module_id = None
        fm_match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if fm_match:
            id_match = re.search(r"^id:\s*(\d+)", fm_match.group(1), re.MULTILINE)
            if id_match:
                module_id = int(id_match.group(1))
        for tag in CITE_TAG_RE.findall(text):
            attrs = dict(ATTR_RE.findall(tag))
            cid = attrs.get("id")
            if not cid:
                continue
            usage.setdefault(cid, set())
            if module_id is not None:
                usage[cid].add(module_id)
    return usage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS_PATH)
    parser.add_argument("--content", type=Path, default=DEFAULT_CONTENT_DIR)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT_PATH)
    parser.add_argument("--dry-run", action="store_true",
                         help="Self-check only: skip writing reports/*.md (use for an isolated per-module facts file before it's merged).")
    args = parser.parse_args()

    facts = json.loads(args.facts.read_text())
    citations = facts.get("citations", {})
    external_authorities = facts.get("external_authorities", {})
    flagged_authorities = facts.get("flagged_authorities", {})

    usage = scan_content_for_cites(args.content)

    # Every <Cite id> used in content must have a verified fact entry.
    unverified_in_content = sorted(set(usage) - set(citations) - set(external_authorities))
    if unverified_in_content:
        print("ERROR: <Cite> used in content with no verified entry in citation_facts.json:",
              file=sys.stderr)
        for c in unverified_in_content:
            print(f"  - {c}", file=sys.stderr)
        sys.exit(1)

    url_records = json.loads(URLS_JSON.read_text())["records"]
    url_overrides = json.loads(URL_OVERRIDES.read_text()) if URL_OVERRIDES.exists() else {}

    con = sqlite3.connect(MASTER_DB, uri=True)
    cur = con.cursor()

    registry = {}
    missing_url = []
    duplicate_lines = []

    for cite, fact in citations.items():
        download_id = fact["download_id"]
        cur.execute(
            "SELECT citation, jurisdiction, decision_date, source_family FROM decisions WHERE download_id = ?",
            (download_id,),
        )
        row = cur.fetchone()
        if row is None:
            print(f"ERROR: download_id {download_id} for {cite} not found in briefer_master.snapshot.db", file=sys.stderr)
            sys.exit(1)
        db_citation, jurisdiction, decision_date, source_family = row
        if db_citation != cite:
            print(f"ERROR: citation_facts.json has {cite!r} but decisions.citation is {db_citation!r} "
                  f"for download_id {download_id}", file=sys.stderr)
            sys.exit(1)

        url = None
        if source_family == "FederalCourt":
            cur.execute("SELECT word_doc_url FROM court_decision_metadata WHERE download_id = ?", (download_id,))
            r = cur.fetchone()
            url = r[0] if r else None
        else:
            rec = url_records.get(download_id)
            if rec:
                url = rec.get("url_source") or rec.get("url_pdf") or rec.get("document_key")

        if cite in url_overrides:
            url = url_overrides[cite]

        if url is None:
            missing_url.append(cite)

        if "duplicate_download_ids" in fact:
            dupe_list = ", ".join(fact["duplicate_download_ids"])
            duplicate_lines.append(
                f"- `{cite}` — canonical `download_id` **{download_id}**; duplicate record(s) `{dupe_list}`. "
                f"{fact.get('duplicate_note', '')}"
            )

        registry[cite] = {
            "citation": cite,
            "short_name": fact["short_name"],
            "download_id": download_id,
            "url": url,
            "jurisdiction": jurisdiction,
            "decision_date": decision_date,
            "outcome": fact["outcome"],
            "outcome_pinpoint": fact["outcome_pinpoint"],
            "outcome_status": fact["outcome_status"],
            "verification_status": fact["verification_status"],
            "modules": sorted(usage.get(cite, [])),
        }

    for cite, fact in external_authorities.items():
        if cite in registry:
            print(f"ERROR: external authority duplicates citation entry {cite}", file=sys.stderr)
            sys.exit(1)
        registry[cite] = {
            "citation": cite,
            "short_name": fact["short_name"],
            "download_id": None,
            "url": fact["url"],
            "jurisdiction": fact.get("jurisdiction", ""),
            "decision_date": fact.get("decision_date"),
            "outcome": fact["outcome"],
            "outcome_pinpoint": fact["outcome_pinpoint"],
            "outcome_status": fact["outcome_status"],
            "verification_status": fact["verification_status"],
            "modules": sorted(usage.get(cite, [])),
            "source_type": "external_authority",
        }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({
        "generated_by": "scripts/build_citation_registry.py",
        "source_snapshot": "briefer_master.snapshot.db + fwc-decision-public-urls.json",
        "citations": registry,
        "flagged_authorities": flagged_authorities,
    }, indent=2) + "\n")
    print(f"Wrote {args.out} ({len(registry)} citations)")

    if args.dry_run:
        print("Dry run: skipped reports/*.md")
        return

    MISSING_URLS_REPORT.parent.mkdir(exist_ok=True)
    with MISSING_URLS_REPORT.open("w") as f:
        f.write("# Missing public URLs\n\n")
        if missing_url:
            f.write("These citations have no recorded public URL and render unlinked:\n\n")
            for c in missing_url:
                f.write(f"- `{c}` (download_id {registry[c]['download_id']})\n")
        else:
            f.write("None. Every cited decision has a recorded public URL.\n")
    print(f"Wrote {MISSING_URLS_REPORT} ({len(missing_url)} missing)")

    with DUPLICATES_REPORT.open("w") as f:
        f.write("# Duplicate decision records\n\n")
        f.write("Citations where the same decision appears under more than one `download_id` "
                "in briefer_master.snapshot.db. The canonical record is the one used in the registry.\n\n")
        if duplicate_lines:
            f.write("\n".join(duplicate_lines) + "\n")
        else:
            f.write("None found among cited decisions.\n")
    print(f"Wrote {DUPLICATES_REPORT} ({len(duplicate_lines)} duplicate groups)")

    with FLAGGED_REPORT.open("w") as f:
        f.write("# Flagged authorities — check against the original\n\n")
        f.write("These authorities are quoted in a decision that is in the corpus, but are not "
                "independently located in the corpus themselves. The quote has been confirmed "
                "verbatim against the quoting decision's text; the authority itself has not been "
                "checked against its own original text.\n\n")
        for name, fa in flagged_authorities.items():
            f.write(f"## {name}\n\n")
            f.write(f"- Status: `{fa['status']}`\n")
            f.write(f"- Quoted in: {fa['quoted_in']} at {fa['quoted_in_pinpoint']}\n")
            f.write(f"- {fa['note']}\n\n")
    print(f"Wrote {FLAGGED_REPORT} ({len(flagged_authorities)} flagged authorities)")


if __name__ == "__main__":
    main()
