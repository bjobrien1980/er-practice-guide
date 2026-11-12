#!/usr/bin/env python3
"""Check the built site's rendered content and internal routes."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
MODULE_SOURCE = ROOT / "src" / "content" / "modules"

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])
    def handle_data(self, data):
        self.text.append(data)


def source_slugs():
    slugs = []
    for path in sorted(MODULE_SOURCE.glob("*.mdx")):
        match = re.search(r"^slug:\s*['\"]?([^'\"\n]+)", path.read_text(), re.MULTILINE)
        if not match:
            raise AssertionError(f"{path.name}: missing slug metadata")
        slugs.append(match.group(1).strip())
    return slugs


def decisions_table_errors():
    """Each module's <DecisionsCited moduleId> must match its own frontmatter id.

    The citation registry keys decisions by module id, so a stale id silently renders
    another module's decisions (or an empty table) after modules are renumbered.
    """
    errors = []
    for path in sorted(MODULE_SOURCE.glob("*.mdx")):
        text = path.read_text()
        own = re.search(r"^id:\s*(\d+)", text, re.MULTILINE)
        if not own:
            errors.append(f"{path.name}: missing id metadata")
            continue
        for used in re.findall(r"<DecisionsCited\s+moduleId=\{(\d+)\}", text):
            if used != own.group(1):
                errors.append(f"{path.name}: DecisionsCited moduleId={used} does not match module id {own.group(1)}")
    return errors


def main():
    if not DIST.exists():
        raise AssertionError("dist/ does not exist; run the static build first")

    errors = decisions_table_errors()
    expected = {"index.html", "start-here/index.html", "pathways/index.html", "glossary/index.html"}
    expected.update(f"modules/{slug}/index.html" for slug in source_slugs())
    for relative in sorted(expected):
        if not (DIST / relative).exists():
            errors.append(f"missing rendered route: /{relative.removesuffix('/index.html')}")

    for html_path in sorted(DIST.rglob("*.html")):
        relative = html_path.relative_to(DIST).as_posix()
        text = html_path.read_text()
        parser = LinkParser()
        parser.feed(text)
        plain = " ".join(" ".join(parser.text).split())

        if "404: Not found" in text or "<title>404" in text:
            errors.append(f"rendered 404 page included in dist: {relative}")
        if relative.startswith("modules/"):
            for required in ("Training material only — not legal advice", "Version", "Last updated"):
                if required not in plain:
                    errors.append(f"{relative}: missing required rendered text: {required}")
            if "Last verified" in plain or "Reviewer" in plain:
                errors.append(f"{relative}: stale review metadata remains")
            if re.search(r"Version\s*</b>\s*</span>|Last updated\s*</b>\s*</span>", text):
                errors.append(f"{relative}: blank version/update metadata")

            duplicate = re.search(r'(<a class="cite"[^>]*>[^<]+</a>)\s+\1', text)
            if duplicate:
                label = re.sub(r"<[^>]+>", "", duplicate.group(1))
                errors.append(f"{relative}: duplicated adjacent citation: {label}")

        for href in parser.hrefs:
            if href.startswith("/") and not href.startswith(("//", "/_astro/", "/pagefind/")):
                route = href.split("#", 1)[0].split("?", 1)[0]
                if route in ("", "/"):
                    target = DIST / "index.html"
                else:
                    target = DIST / route.strip("/") / "index.html"
                if not target.exists():
                    errors.append(f"{relative}: internal link has no rendered target: {href}")

    if errors:
        print("RENDERED CONTENT CHECK FAILED:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"Rendered content check passed: {len(expected)} required routes and {len(list(DIST.rglob('*.html')))} HTML files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
