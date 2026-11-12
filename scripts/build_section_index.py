#!/usr/bin/env python3
"""Build a small heading-level index used for direct search cross-links."""
from html.parser import HTMLParser
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT = DIST / "search-sections.json"

class SectionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current = None
        self.parts = []
        self.in_ignored = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style"}:
            self.in_ignored = True
        if tag in {"h1", "h2", "h3"}:
            self.flush()
            self.current = {"heading": "", "id": attrs.get("id", "")}
            self.parts = []

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.in_ignored = False
        if tag in {"h1", "h2", "h3"} and self.current:
            self.current["heading"] = " ".join("".join(self.parts).split())
            self.parts = []

    def handle_data(self, data):
        if self.in_ignored:
            return
        if self.current is not None:
            self.parts.append(data)
        elif data.strip() and self.sections:
            self.sections[-1]["parts"].append(data)

    def flush(self):
        if self.current and self.current["heading"]:
            self.sections.append({**self.current, "parts": []})
        self.current = None
        self.parts = []

    def finish(self):
        self.flush()
        for section in self.sections:
            excerpt = " ".join("".join(section.pop("parts")).split())
            section["excerpt"] = excerpt[:320]


def route_for(path: Path) -> str:
    relative = path.relative_to(DIST).as_posix()
    if relative == "index.html":
        return "/"
    return "/" + relative.removesuffix("/index.html") + "/"


def main():
    entries = []
    for path in sorted(DIST.rglob("index.html")):
        parser = SectionParser()
        parser.feed(path.read_text())
        parser.finish()
        route = route_for(path)
        for section in parser.sections:
            if section["heading"]:
                entries.append({
                    "url": route + (f"#{section['id']}" if section["id"] else ""),
                    "title": path.parent.name if path.parent != DIST else "ER Practice Guide",
                    **section,
                })
    OUT.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")))
    print(f"Wrote {OUT} ({len(entries)} searchable sections)")


if __name__ == "__main__":
    main()
