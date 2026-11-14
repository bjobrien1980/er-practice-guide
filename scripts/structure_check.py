#!/usr/bin/env python3
"""Check guide structure: module IDs, numeric references, routes and glossary linkability."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
MODULE_DIR = ROOT / "src" / "content" / "modules"
GLOSSARY = ROOT / "src" / "data" / "glossary.ts"

errors = []
modules = {}
for path in sorted(MODULE_DIR.glob("*.mdx")):
    text = path.read_text()
    frontmatter = text.split("---", 2)[1]
    id_match = re.search(r"^id:\s*(\d+)", frontmatter, re.MULTILINE)
    slug_match = re.search(r"^slug:\s*(.+)$", frontmatter, re.MULTILINE)
    if not id_match or not slug_match:
        errors.append(f"{path.name}: missing id or slug")
        continue
    modules[int(id_match.group(1))] = (slug_match.group(1).strip(), path)

ids = sorted(modules)
if ids and ids != list(range(min(ids), max(ids) + 1)):
    errors.append(f"module IDs are not contiguous: {ids}")

all_content = "\n".join(p.read_text() for p in MODULE_DIR.glob("*.mdx"))
for number in map(int, re.findall(r"\bModule\s+(\d+)\b", all_content, re.IGNORECASE)):
    if number not in modules:
        errors.append(f"numeric cross-reference points to missing Module {number}")

for path in list(MODULE_DIR.glob("*.mdx")) + list((ROOT / "src" / "pages").glob("*.astro")):
    text = path.read_text()
    for slug in re.findall(r'href="/modules/([^"#?]+)', text):
        if slug not in {value[0] for value in modules.values()}:
            errors.append(f"{path.relative_to(ROOT)}: link points to missing module slug /modules/{slug}")

# A link's "Module N" label must match the module it points to.
slug_to_id = {value[0]: key for key, value in modules.items()}
LABELLED_LINKS = [
    re.compile(r'href="/modules/([^"#?]+)"[^>]*>\s*(?:<[^>]+>\s*)*Module\s+(\d+)'),
    re.compile(r'\[Module\s+(\d+)[^\]]*\]\(/modules/([^)#?]+)\)'),
]
for path in list(MODULE_DIR.glob("*.mdx")) + list((ROOT / "src" / "pages").rglob("*.astro")):
    text = path.read_text()
    for index, pattern in enumerate(LABELLED_LINKS):
        for match in pattern.finditer(text):
            slug, number = (match.group(1), int(match.group(2))) if index == 0 else (match.group(2), int(match.group(1)))
            if slug in slug_to_id and slug_to_id[slug] != number:
                errors.append(f"{path.relative_to(ROOT)}: link labelled Module {number} points to /modules/{slug}, which is Module {slug_to_id[slug]}")

# Case cards use a fixed set of outcome labels (see the About page).
CARD_LABELS = {'Process risk', 'Employer won, narrowly', 'Point of principle', 'Employer won', 'Regulator won', 'Union won', 'Respondent won', 'Mixed result', 'Interim ruling', 'Employee won'}
for path in MODULE_DIR.glob("*.mdx"):
    for label in re.findall(r'<span class="tag">([^<]*)</span>', path.read_text()):
        if label not in CARD_LABELS:
            errors.append(f"{path.name}: case card label not in the fixed set: {label!r}")

for term in re.finditer(r'\{\s*id:\s*"([^"]+)"\s*,\s*term:\s*"([^"]+)"\s*,\s*definition:', GLOSSARY.read_text()):
    start = term.start()
    entry_end = GLOSSARY.read_text().find("},", start)
    entry = GLOSSARY.read_text()[start:entry_end if entry_end >= 0 else start]
    if "match:" not in entry:
        errors.append(f"glossary entry has no match pattern: {term.group(2)} ({term.group(1)})")

if errors:
    print("STRUCTURE CHECK FAILED:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print(f"Structure check passed: {len(modules)} contiguous modules, numeric references valid, module links valid, glossary entries linkable.")
