# Gap review: Modules 14, 18 and 29, plus one correction to Module 13

**Review date:** 22 November 2026
**Branch:** `draft/modules-34-35` (from `staging` at `ded86ca`, v1.0.0)
**Scope:** check whether fitness for work, incapacity, and redundancy and restructuring needed new modules. They don't. **Follow-up status:** Modules 13, 14, 18 and 29 were updated in the local draft. The findings below record the original review; see the disposition immediately below.

## Follow-up disposition

- **Module 18:** implemented G18-1 and G18-4 against the current Act and Regulations, with separate Centrelink and employee-association steps, s.534 exclusions and the prescribed form. Implemented G18-3 using the issued *Helensburgh* judgment already held in Briefer. Deferred G18-2: the existing selection warning remains; any future voluntary-redundancy guidance should start with whether there was a dismissal under s.386.
- **Module 14:** implemented G14-1 without limiting it to certified leave. Checked that the decision cited in G14-3 discusses *Blackadder*, not *Grant*; clarified the source-of-power and reasonableness checks. Qualified the *Rennick* passage rather than treating permanent incapacity as a general clearance. G14-2 remains optional; no broader WHS or disability-law currency claim was added (G14-4).
- **Module 29:** implemented G29-1 with *Buckeridge* at [141] and kept *Leung* as a fact-specific illustration. Added a link to Module 30 for G29-2.

## Original conclusions

The v1.0.0 Guide already covers fitness for work and incapacity in two modules: Module 14 (medical capacity and inherent requirements, s.387(a)) and Module 29 (illness, injury and leave as general protections). It covers redundancy in Module 18. All three are substantive (3,800–4,500 words) and use current authority, including *Helensburgh* in Module 18. A new module in either area would duplicate them.

The gaps are narrow. The most useful additions are a short section in Module 18 on the notification duties for 15 or more dismissals, and a correction to Module 13's description of where sexual harassment applications sit.

## Module 13: correction (high priority)

**G13-1. Wrong Part for sexual harassment applications.** Line 32 says an employee may bring "a sexual harassment application under Part 6-4B of the FW Act". Since 6 March 2023, new applications are made under s.527F in **Part 3-5A**. Part 6-4B (s.789FC) now covers stop-bullying applications, and sexual harassment only for some conduct that began before that date (see the note to rule 87 of the Fair Work Commission Rules 2024).

Proposed replacement: "…a stop-bullying order under s.789FC, or a sexual harassment application under s.527F (Part 3-5A) — see [Module 34](/modules/stop-bullying-and-sexual-harassment-orders)." Add 34 to `related`.

**Source:** FW Act s.527F and FWC Rules r.87, as held in the Briefer legislation collection (current as at 3 April 2026). Check this against the live register.

## Module 14: Medical capacity and inherent requirements

The module already covers IME directions, competing medical evidence, the substantive-role point, WHS fitness-for-duty directions, how long to wait, and a disability-discrimination flag. Proposed edits:

- **G14-1. Point to s.352 earlier (medium).** The module mentions s.351 once and s.352 not at all, and leaves temporary absence to Module 29. Add one line under "Capacity, not conduct": *if the employee is absent on certified illness or injury leave, check the s.352 temporary absence rule in Module 29 before acting on capacity.* This is a common sequencing error for new advisers.
- **G14-2. Name the High Court source for "inherent requirements" (low).** The module explains the objective test but doesn't name *Qantas Airways Ltd v Christie*. The corpus has FWC decisions applying it, for example [2022] FWC 1614 at [24] (quoting the High Court) and [2022] FWC 1871 at [39]. Optional; it only gives the reader the source of the test.
- **G14-3. Check the IME authority is named consistently (low).** Module 14 at line 71 describes a Full Federal Court holding through [2023] FWC 2906 at [93]. Module 29 names *Grant v BHP Coal*. Check that the two modules describe the same authority the same way.
- **G14-4. Currency.** `law_current_as_at` is null. Fine for an s.387(a) module, but record a check date if WHS or disability law statements are added.

## Module 18: Redundancy, restructuring and consultation

The module's own review (`reports/redundancy-module-review.md`, 12 November 2026) is resolved. Proposed edits:

- **G18-1. Notification duties for 15 or more dismissals (high).** The module doesn't mention ss.530–531. Proposed new short section, "Larger restructures: 15 or more dismissals":
  - s.530: an employer that decides to dismiss 15 or more employees for economic, technological, structural or similar reasons must give written notice to Centrelink (Services Australia) as soon as practicable and before any dismissal. Dismissing before complying is a civil remedy contravention (s.530(4)).
  - s.531: notify, and give an opportunity to consult, each relevant registered employee association where the employer could reasonably be expected to know that one or more of the employees are members. The Commission can make orders if it doesn't (s.532).
  - Checklist item: "If 15 or more dismissals are proposed, ss.530–531 notices have been given before any dismissal."
  - **Source:** FW Act ss.530–531 as held in the Briefer legislation collection (current as at 3 April 2026). Check against the live register before publishing.
- **G18-2. Selection for redundancy and voluntary redundancy (medium, needs research).** "Voluntary" doesn't appear and "selection" appears twice. A short passage on how selection criteria and expressions of interest affect the later s.387 assessment would help new advisers. No authority has been gathered for this yet. Do a proposition audit in Briefer before drafting.
- **G18-3. Read *Helensburgh* directly (medium, when available).** The module relies on *Helensburgh Coal Pty Ltd v Bartley* [2025] HCA 29 as quoted in [2026] FWC 1315, and flags this. Once the High Court parsing on MS128 includes [2025] HCA 29, add it as an external authority read directly. Later FWC decisions applying it are in the corpus, for example [2025] FWC 2758 at [14] and [2025] FWC 3442 at [11].
- **G18-4. Currency.** `law_current_as_at` is still null for a module that relies on ss.119–120 and s.389. Record a check date when G18-1 is added.

## Module 29: Illness, injury and leave

The module is the most complete of the three and has a currency check recorded (14 November 2026). Proposed edits:

- **G29-1. "Because of" the absence, not "during" it (low).** *Roohizadegan v Technology One (No 6)* [2025] FCA 1619 at [2183]–[2186] restates, citing *Buckeridge v Littlepay* [2023] FCA 1036 at [141]–[142], that s.352 prohibits dismissal because of a temporary absence, not dismissal during one. *Buckeridge* is already an external authority in `citation_facts.json`. Its [141]–[142] pinpoints would need checking against the judgment file before use.
- **G29-2. Federal and state disability discrimination law (none needed).** Module 29 doesn't mention the Disability Discrimination Act, but Modules 2 and 30 do. No change is needed beyond a cross-reference if not already present.

## Out of scope but noticed

- The repository's `reports/duplicate-citations.md` lists 52 duplicate groups after this branch's registry rebuild, unchanged from the baseline pattern. The new modules cite only one download ID per decision.
- `[2025] FWC 3115` at [53] was outside the approved snapshot. The review pass checked the locally held decision and replaced that indirect reference with a direct citation to *Paper Australia* [2025] FWCFB 224.
