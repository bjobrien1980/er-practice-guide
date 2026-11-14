# Changelog

What changed in each version of the ER Practice Guide, and what is known to be unfinished.

## 1.0.0 — 14 November 2026

The first version released as a whole. Before this, each module carried its own version number (0.1.0 to 0.2.1).

### Added

- **Tier 5: General protections in depth.** Nine new modules (25 to 33) on workplace rights, adverse action, the reason for the action, managing an employee who has complained, illness and leave, discrimination, industrial activity, coercion and misrepresentation, and court proceedings.
- **Module 18: Redundancy, restructuring and consultation.** Modules 19 to 24 were renumbered to make room.
- **Advocacy in the Fair Work Commission.** A guide to preparing and running a hearing, with a complete example witness statement and outline of submissions.
- **About this guide** and this changelog.

### Changed

- **One voice.** Tier 5 and the advocacy guide were rewritten in the same conversational register as Modules 1 to 24.
- **One notice per module.** The separate warnings were merged, and the explanation of how decisions and legislation are checked moved to the About page.
- **Case cards use a fixed set of ten outcome labels**, listed on the About page.
- **Representation before the Commission is explained once**, in Module 22. Module 8 and the advocacy guide point to it.
- **Consistent terms.** "The Commission", "show cause" and "this guide" are used throughout.
- **Scenario titles** follow one pattern across all modules.
- **Module 33** is now titled "Court proceedings, remedies and personal exposure".
- **Related modules** now link the older tiers to their Tier 5 counterparts.

### Checks

- Citations in standalone pages are now verified at build, not only those in modules.
- A citation whose quotation contains "/" is no longer skipped by the verifier.
- The build fails if a link labelled "Module N" points to a different module, or if a case card uses a label outside the fixed set.
- Citations can show their quotation inline, so a sentence that relies on quoted words displays them.
- Links to Federal Court judgments were checked live on 14 November 2026 and are working.

### Known limits of this version

- **Links to Commission practice notes** on the advocacy page have not been opened.
- **Some statute summaries were written without a decision to anchor them** and should be read against the Act: the agreements covered by s.344, ss.349 and 350, the workplace delegates' rights, the six-year limit for non-dismissal claims, consent arbitration, the grounds for a costs order in court, and who needs permission to appear.
- **Modules 26 and 28 show no "law checked" date.**
- **No systematic search for appeals has been done.** Three interlocutory decisions (*Weber*, *Blade*, *RTBU v Metro Trains Sydney*) were searched on 14 November 2026; no appeal was found.
- **Tier 5 modules are longer** than the others (16 to 24 minutes against 8 to 17).
- **Interactive features and narrow screens** were not tested for this release.
