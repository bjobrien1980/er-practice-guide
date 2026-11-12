#!/usr/bin/env python3
"""Estimate each module's reading time from its MDX source.

Counts the words a reader actually sees: body prose, tables, failure cards, checklist
items, scenario facts, questions and the model answer. Front matter, imports, markup
and citation tags are excluded. The estimate is words / WORDS_PER_MINUTE, rounded up.
It is reading time only: it does not allow for writing scenario answers.

Usage:
  python3 scripts/estimate_reading_time.py           # report
  python3 scripts/estimate_reading_time.py --write   # update reading_minutes in front matter
  python3 scripts/estimate_reading_time.py --check   # exit 1 if any front matter is stale
"""
import argparse
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "src" / "content" / "modules"

# Dense legal training material with pinpoint citations reads slower than general prose.
WORDS_PER_MINUTE = 200

STRING = r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\''


def strings_in(source: str) -> str:
    return " ".join(a or b for a, b in re.findall(STRING, source))


def visible_text(mdx: str) -> str:
    body = re.sub(r"\A---\n.*?\n---\n", "", mdx, count=1, flags=re.DOTALL)
    body = re.sub(r"^import .*$", "", body, flags=re.MULTILINE)
    # Checklist: every quoted string is shown (group labels and item text); the title is not.
    body = re.sub(
        r"<Checklist\b(.*?)/>",
        lambda m: strings_in(re.sub(r'\b(title|openAdvice|readyAdvice)=(?:"[^"]*"|\{[^\n]*\})', "", m.group(1))),
        body,
        flags=re.DOTALL,
    )
    # Scenario: the questions array is shown; the rest of the block is ordinary markup.
    body = re.sub(r"<Scenario\b([^>]*)>", lambda m: strings_in(m.group(1)), body)
    # Citations render as a short label; the phrase attribute is never shown.
    body = re.sub(r"<Cite\b[^>]*/>", " cite ", body)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"\]\([^)]*\)", "]", body)  # markdown link targets
    return body


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.()/-]*", text))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="update reading_minutes in front matter")
    mode.add_argument("--check", action="store_true", help="fail if front matter differs from the estimate")
    args = parser.parse_args()

    stale = []
    print(f"{'module':<46} {'words':>6} {'current':>8} {'estimate':>9}")
    for path in sorted(MODULES.glob("*.mdx")):
        text = path.read_text()
        match = re.search(r"^reading_minutes:\s*(\d+)\s*$", text, re.MULTILINE)
        if not match:
            print(f"{path.name}: missing reading_minutes metadata", file=sys.stderr)
            return 1
        current = int(match.group(1))
        words = count_words(visible_text(text))
        estimate = max(1, math.ceil(words / WORDS_PER_MINUTE))
        print(f"{path.stem:<46} {words:>6} {current:>8} {estimate:>9}")
        if estimate != current:
            stale.append(path.name)
            if args.write:
                path.write_text(text[: match.start(1)] + str(estimate) + text[match.end(1):])

    if args.write:
        print(f"Updated {len(stale)} module(s).")
    elif stale:
        print(f"{len(stale)} module(s) differ from the estimate; run with --write to update.")
        return 1 if args.check else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
