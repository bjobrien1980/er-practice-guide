#!/usr/bin/env python3
"""
Verify every <Cite> pinpoint in content/modules against the actual decision text.

For each <Cite id="[citation]" at="[n]" phrase="..."> in the MDX content, this script:
  1. Resolves the citation to a download_id via data/citation_facts.json.
  2. Reconstructs the decision's paragraph-indexed text from fwc-decision-chunks.snapshot.db
     chunk_text — never from the paragraph_range column, which is known to carry false end
     bounds (a citation year misread as a paragraph number).
  3. Confirms every paragraph number in `at` exists in the reconstructed text.
  4. Confirms `phrase` (case-insensitive substring) appears within those paragraphs.

A <Cite> may omit `phrase` only if status="flagged" — it then renders a visible "unverified"
marker instead of failing the build. Any other failure fails the build.

Usage:
  python3 scripts/verify_pinpoints.py
  python3 scripts/verify_pinpoints.py --facts data/citation_facts.module-1.json --content src/content/modules/01-who-can-claim.mdx

--content may be a single file, a directory (globbed for *.mdx), or omitted (globs the
whole content dir). Use --facts to self-check an isolated per-module facts file before it's
merged into the shared data/citation_facts.json — this never writes anything.

Exit code 0 = all pinpoints confirmed or explicitly flagged. Exit code 1 = a failure.
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHUNKS_DB = "file:" + str(Path.home() / "briefer-claude/snapshots/fwc-decision-chunks.snapshot.db") + "?mode=ro"
DEFAULT_FACTS_PATH = ROOT / "data" / "citation_facts.json"
DEFAULT_CONTENT_DIR = ROOT / "src" / "content" / "modules"

CITE_TAG_RE = re.compile(r'<Cite\s+([^/>]+?)\s*/?>')
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
PARA_NUM_RE = re.compile(r"\[(\d+)\]")


def find_cites_in_content(content_path):
    """Yield (module_file, citation, at, phrase, status) for every <Cite> in content.

    content_path may be a single .mdx file or a directory of them.
    """
    if content_path.is_file():
        mdx_files = [content_path]
    else:
        mdx_files = sorted(content_path.glob("*.mdx"))

    for mdx_path in mdx_files:
        text = mdx_path.read_text()
        for tag in CITE_TAG_RE.findall(text):
            attrs = dict(ATTR_RE.findall(tag))
            cid = attrs.get("id")
            at = attrs.get("at")
            if not cid or not at:
                continue
            yield (mdx_path.name, cid, at, attrs.get("phrase"), attrs.get("status"))


_text_cache = {}


def reconstruct_paragraphs(download_id):
    if download_id in _text_cache:
        return _text_cache[download_id]
    con = sqlite3.connect(CHUNKS_DB, uri=True)
    cur = con.cursor()
    cur.execute("SELECT chunk_text FROM chunks WHERE download_id = ? ORDER BY chunk_index", (download_id,))
    rows = cur.fetchall()
    full = "\n".join(r[0] for r in rows)

    paras = {}
    # Primary pass: paragraph markers that sit alone on their own line.
    parts = re.split(r"\n?\[(\d+)\]\s*\n", full)
    for i in range(1, len(parts) - 1, 2):
        num = int(parts[i])
        paras.setdefault(num, "")
        paras[num] += parts[i + 1]

    _text_cache[download_id] = (full, paras)
    return full, paras


def paragraph_numbers(at):
    """Parse an `at` attribute like "[30]" or "[53]-[56]" or "[28], [31]" into a list of ints."""
    nums = [int(n) for n in PARA_NUM_RE.findall(at)]
    if "-" in at or "–" in at or "—" in at:
        if len(nums) == 2:
            return list(range(min(nums), max(nums) + 1))
    return nums


def verify_one(citation, at, phrase, facts):
    fact = facts.get(citation)
    if fact is None:
        return False, f"no verified entry in citation_facts.json for {citation!r}"
    download_id = fact["download_id"]
    full_text, paras = reconstruct_paragraphs(download_id)

    nums = paragraph_numbers(at)
    if not nums:
        return False, f"could not parse paragraph number(s) from at={at!r}"

    missing = []
    found_text = ""
    for n in nums:
        if n in paras:
            found_text += paras[n] + "\n"
        elif f"[{n}]" in full_text:
            # Marker exists inline (not on its own line) — fall back to a window search.
            idx = full_text.find(f"[{n}]")
            found_text += full_text[idx: idx + 2000] + "\n"
        else:
            missing.append(n)

    if missing:
        return False, f"paragraph(s) {missing} not found in download_id {download_id}"

    if phrase:
        # Source text has literal line-wrap newlines mid-sentence (and sometimes mid-word,
        # hyphenated) carried over from the original PDF extraction. Normalise before comparing
        # so a wrapped line doesn't produce a false "phrase not found".
        if normalise(phrase) not in normalise(found_text):
            return False, f"phrase {phrase!r} not found in paragraph(s) {nums} of download_id {download_id}"

    return True, "confirmed"


def normalise(text):
    text = re.sub(r"-\s*\n\s*", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS_PATH)
    parser.add_argument("--content", type=Path, default=DEFAULT_CONTENT_DIR)
    args = parser.parse_args()

    facts_doc = json.loads(args.facts.read_text())
    facts = facts_doc.get("citations", {})
    external_authorities = facts_doc.get("external_authorities", {})

    confirmed = 0
    flagged = 0
    external = 0
    failures = []

    for module_file, citation, at, phrase, status in find_cites_in_content(args.content):
        if citation in external_authorities:
            external += 1
            print(f"EXTERNAL  {module_file}  {citation} at {at}  (direct source record; original text not independently read)")
            continue

        if status == "flagged":
            flagged += 1
            print(f"FLAGGED  {module_file}  {citation} at {at}  (renders with visible unverified marker)")
            continue

        if not phrase:
            failures.append((module_file, citation, at, "no `phrase` attribute and not status=\"flagged\""))
            continue

        ok, detail = verify_one(citation, at, phrase, facts)
        if ok:
            confirmed += 1
            print(f"OK       {module_file}  {citation} at {at}")
        else:
            failures.append((module_file, citation, at, detail))

    print()
    print(f"{confirmed} confirmed, {external} external source records, {flagged} flagged, {len(failures)} failed")

    if failures:
        print("\nFAILURES:", file=sys.stderr)
        for module_file, citation, at, detail in failures:
            print(f"  {module_file}  {citation} at {at}  -- {detail}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
