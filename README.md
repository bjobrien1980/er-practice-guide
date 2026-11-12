# ER Practice Guide

An Astro-based ER practice guide focused on conduct, performance and dismissal-related issues under the Fair Work Act 2009 (Cth).

## Repository model

- **MS64 is the canonical working environment.** Private Briefer snapshots and source material remain on MS64.
- **GitHub is the versioned publication mirror.** The repository is private: <https://github.com/bjobrien1980/er-practice-guide>
- **`staging` is the automatic-sync branch.** Local changes are validated and pushed there.
- **`main` is the publication branch.** Review the staging pull request before merging or deploying.

The committed `data/` files contain the guide's citation facts and generated citation registry. The underlying Briefer snapshots referenced by the generation scripts are intentionally not copied into GitHub.

## Local commands

Run from the repository root:

| Command | Purpose |
|---|---|
| `npm run dev` | Start the local guide at `http://localhost:4321` |
| `npm run build` | Run the MS64 source-aware validation gates and build the static site |
| `npm run verify` | Verify citation pinpoints against the local Briefer decision snapshot |
| `npm run linkcheck` | Check citation registry integrity and approved link domains |
| `npm run preview` | Preview the production build locally |
| `bash scripts/sync-staging.sh` | Validate, commit and push pending changes on `staging` |

## Automatic staging sync

MS64 has a launchd configuration at:

```text
~/Library/LaunchAgents/com.benobrien.er-practice-guide-sync.plist
```

It runs `scripts/sync-staging.sh` periodically. The script only acts when the working copy is on `staging`; it runs the full local build and pushes only after validation succeeds. It never pushes directly to `main`.

## GitHub validation

The GitHub Actions workflow at `.github/workflows/validate-staging.yml` runs for pushes to `staging` and pull requests into `main`. Because private Briefer snapshots stay on MS64, GitHub runs the repository link check and static Astro build; the source-aware registry and pinpoint checks run locally before a staging push.

## Publication

The staging-to-main pull request is the review point. Do not merge it until content, authority links, source status and deployment configuration have been reviewed. The eventual `briefer.com.au` deployment can be connected to the `main` branch through the selected hosting provider.
