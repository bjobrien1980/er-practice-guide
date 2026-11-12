#!/usr/bin/env python3
"""
Static link check — no live HTTP requests (WebFetch is denied for this project; see CLAUDE.md).

Confirms:
  1. Every <Cite id="..."> in content resolves to an entry in data/citations.json.
  2. Every citations.json URL is either null or an https URL on an expected government domain
     (fwc.gov.au or judgments.fedcourt.gov.au) — catches a hand-typed or malformed link.
  3. No MDX content file hand-types a link directly to a decision (fwc.gov.au / fedcourt.gov.au)
     via a raw <a href>. All decision links must go through <Cite>, which renders from the
     registry — never a hand-entered URL.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
CITATIONS_PATH = ROOT / "data" / "citations.json"
CONTENT_DIR = ROOT / "src" / "content" / "modules"

ALLOWED_DOMAINS = {
    "www.fwc.gov.au", "fwc.gov.au",
    "dms.fwc.gov.au",  # FWC's media-download subdomain, used when a decision has no landing-page URL
    "www.judgments.fedcourt.gov.au", "judgments.fedcourt.gov.au",
}
CITE_ID_RE = re.compile(r'<Cite\s+[^/>]*?id="([^"]+)"')
RAW_HREF_RE = re.compile(r'href="(https?://[^"]+)"')


def main():
    errors = []
    registry = json.loads(CITATIONS_PATH.read_text())["citations"]

    for mdx_path in sorted(CONTENT_DIR.glob("*.mdx")):
        text = mdx_path.read_text()

        for cid in CITE_ID_RE.findall(text):
            if cid not in registry:
                errors.append(f"{mdx_path.name}: <Cite id=\"{cid}\"> has no entry in data/citations.json")

        for href in RAW_HREF_RE.findall(text):
            host = urlparse(href).netloc
            if host in ALLOWED_DOMAINS or "fwc.gov.au" in host or "fedcourt.gov.au" in host:
                errors.append(
                    f"{mdx_path.name}: hand-typed link to a decision host ({href}) — use <Cite> instead"
                )

    for cite, entry in registry.items():
        url = entry.get("url")
        if url is None:
            continue
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc not in ALLOWED_DOMAINS:
            errors.append(f"citations.json[{cite!r}].url is not on an approved government domain: {url}")

    if errors:
        print("LINK CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Link check passed: {len(registry)} registry entries, "
          f"{sum(1 for e in registry.values() if e.get('url'))} linked, "
          f"{sum(1 for e in registry.values() if not e.get('url'))} unlinked.")


if __name__ == "__main__":
    main()
