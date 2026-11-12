#!/bin/bash
set -euo pipefail

# Validate changed local content, then commit and push it to staging.
# Intended to be called by launchd on MS64; it is deliberately not a main-branch publisher.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if [[ "$(git branch --show-current)" != "staging" ]]; then
  exit 0
fi

if git diff --quiet && git diff --cached --quiet && [[ -z "$(git status --porcelain --untracked-files=all)" ]]; then
  exit 0
fi

# Build runs registry generation, pinpoint verification, static link checks and Astro build.
npm run build

git add -A
if git diff --cached --quiet; then
  exit 0
fi

git commit -m "chore(sync): update staging guide"
git push origin staging
