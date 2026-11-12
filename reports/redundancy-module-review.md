# Review — Module 18: Redundancy, restructuring and consultation

**Review date:** 2026-11-12 22:15 AWST
**Review basis:** working branch `content/redundancy-module`, module source, current local citation registry/facts, live FWC chunk database, and the Federal Register current-compilation metadata.
**Status:** **review findings resolved; build and source gates pass**.

## Executive conclusion

The module is substantively strong and is a useful addition to the Guide. It correctly separates the three s.389 limbs, consultation, redeployment, the later s.387 assessment and redundancy pay.

It is not yet merge-ready for three reasons:

1. **The local validation gate fails:** 514 pinpoint checks pass, but two citations in the new module fail.
2. **Several propositions are stated more categorically than the authorities support**, particularly the treatment of a signed termination letter, competition for vacancies and consultation sequencing.
3. **The module has no explicit current-source gate** despite dealing with s.389, award/EA consultation clauses and ss.119–120 redundancy pay; its `law_current_as_at` and `law_sources` fields remain unset.

No module edits were made during this review.

## Findings

### R-001 — Build-blocking pinpoint failures

**Severity:** High
**Location:** `18-redundancy-restructuring-and-consultation.mdx`, lines 68 and 70
**Status:** must fix before merge.

The module cites `[2022] FWC 1905` at `[92]` with these phrases:

- “either immediately or with a reasonable period of retraining”;
- “advertise the vacancy and require the employee to compete with other applicants”.

The validation gate reports that neither phrase occurs in paragraph `[92]` of the cited decision. The reason is visible in the source: paragraph `[92]` introduces a quoted passage from *Ulan Coal Mines Limited v Honeysett* and the quoted text is numbered `[34]`, not part of Graydon’s own paragraph `[92]` for the pinpoint verifier.

**Recommended correction:** preserve the indirect-authority warning, but cite the Graydon paragraph with a phrase actually present at `[92]` and make clear that the substantive passage is quoted from *Honeysett*. Alternatively, add a properly verified direct source entry for *Honeysett* before using the quoted proposition.

### R-002 — Consultation sequencing is overcategorical

**Severity:** Medium
**Locations:** lines 58–64, checklist lines 170–172.

The module correctly explains the standard award clause and correctly uses *Graydon* to show that written information was required before discussion under that clause. But these statements are too broad when read outside the relevant clause:

- “The written information comes first.”
- “If the termination letter is already signed, the meeting is not consultation.”
- “The termination letter was not prepared or issued before consultation finished.”

The controlling obligation comes from the applicable award or enterprise agreement, and clauses vary. A signed letter may be powerful evidence that the outcome was predetermined, but it is not necessarily a universal legal test independent of the applicable instrument and facts.

**Recommended formulation:**

> Under the applicable consultation clause, check what information must be supplied, when it must be supplied and what discussion is required. A termination letter prepared or issued before the consultation is complete is strong evidence that the individual outcome was predetermined, but the legal consequence depends on the instrument and the facts.

### R-003 — Vacancy competition should not read as an absolute prohibition

**Severity:** Medium
**Locations:** lines 68–74; checklist line 175.

The module's treatment of redeployment is generally good, and the cited *Honeysett* passage supports concern where an employer advertises a suitable vacancy instead of redeploying an employee. But “Don't make a redundant employee compete for a vacancy” can be read as an absolute rule.

The legal question remains whether redeployment would have been reasonable in all the circumstances, including suitability, skills, retraining, location, remuneration and the nature of the role. Competition for a vacancy is a significant risk indicator; it is not necessarily determinative in every case.

**Recommended formulation:**

> Do not assume that making the employee compete for a suitable vacancy will preserve the genuine-redundancy defence. It may be strong evidence that redeployment would have been reasonable, depending on the facts and the applicable authority.

### R-004 — Redundancy-pay cooperation proposition needs a boundary

**Severity:** Medium
**Location:** lines 100–106.

The module says an employee “must meaningfully cooperate” in exploring acceptable employment. That proposition is taken from `[2026] FWC 2083`, and the cited decision is confirmed in the local facts registry. It should not be presented as an unqualified rule governing every s.120 application.

Section 120 involves a Commission discretion and the acceptability of alternative employment is fact-sensitive. The module should distinguish the case-specific observation from the statutory discretion.

**Recommended formulation:**

> In a s.120 application, the Commission may consider whether the employee meaningfully engaged with the alternative employment offered, but the acceptability of the employment remains an objective, fact-sensitive question and the statutory discretion must be checked in its current form.

### R-005 — Current-source gate missing

**Severity:** Medium
**Location:** frontmatter and opening module text.

The module deals with current statutory provisions, modern-award consultation terms, enterprise agreements, redundancy pay and Commission procedure, but has:

```yaml
law_current_as_at: null
law_sources: []
```

The Federal Register metadata currently identifies Fair Work Act compilation **73**, commencing 7 July 2026 and registered 31 July 2026. That confirms that the Act has a later current compilation than the baseline work used earlier in the Guide, but it does not by itself verify each proposition in this module.

**Recommended addition:** add a visible current-source gate requiring the user to check:

- current ss.385, 389, 396 and 119–121;
- the applicable modern award consultation clause;
- the applicable enterprise agreement;
- any contractual redundancy or consultation term; and
- current Commission procedure for any s.120 application.

### R-006 — “Yes, yes, no” is confusing

**Severity:** Low
**Location:** line 42.

> “A ‘yes, yes, no’ is needed.”

This is memorable but ambiguous because the three questions are framed as “is the job gone?”, “was consultation done?” and “was redeployment reasonable?” The clearer formulation is:

> The first two limbs must be established, and redeployment must not have been reasonable in all the circumstances.

### R-007 — Useful separation of redundancy and unfair-dismissal merits

**Severity:** None — positive finding.

The module correctly explains that failure of s.389 removes the genuine-redundancy exclusion but does not itself determine the s.387 outcome. The contrast between *Semaan*, *Hurley* and *Graydon* is pedagogically valuable and avoids presenting consultation failure as having a fixed remedy.

### R-008 — Useful handling of indirect authority

**Severity:** None — positive finding.

The module openly identifies *Ulan Coal Mines v Howarth*, *Ulan Coal Mines v Honeysett*, *Helensburgh Coal v Bartley* and *Maswan* as indirectly sourced or not independently read. That is consistent with the Guide’s provenance discipline. The citation failure in R-001 is therefore a repairable implementation problem, not a reason to remove the underlying analysis.

## Integration review

- The existing genuine-redundancy discussion in Module 1 links to Module 18.
- The pathways page links to the new redundancy module.
- The module ID and slug are internally coherent on the working branch.
- The working branch shifts the former Modules 18–23 to Modules 19–24. This is coherent locally but is a broader release change and should be reviewed as part of the branch diff, not treated as an incidental file rename.
- The build reaches the content and rendered-route stages but fails the pinpoint gate, so the module should not be published in its current state.

## Validation output

```text
514 confirmed, 2 failed

Failed:
[2022] FWC 1905 at [92] — “either immediately or with a reasonable period of retraining”
[2022] FWC 1905 at [92] — “advertise the vacancy and require the employee to compete with other applicants”
```

The build did complete the static route generation and rendered-content checks after the pinpoint failures were reported; that does not make the source-verification gate pass.

## Recommended disposition

**Do not merge yet.** Make the following targeted changes first:

1. repair the two `[2022] FWC 1905` citations or add a verified direct *Honeysett* source;
2. qualify the consultation sequencing and signed-letter propositions;
3. qualify the vacancy-competition proposition;
4. qualify the s.120 cooperation proposition;
5. add the current-source gate; and
6. rerun the full registry, pinpoint, link, build and rendered-content checks.

## Resolution

Applied the requested repair and qualifications:

- added a direct official source record for `[2010] FWAFB 7578`, with the original-text limitation stated explicitly;
- moved both redeployment propositions from the Graydon `[92]` citation to the direct Honeysett record;
- qualified consultation sequencing and the effect of a prepared or issued termination letter;
- qualified vacancy competition as a risk indicator rather than an absolute prohibition;
- qualified the s.120 cooperation point as a fact-sensitive Commission consideration;
- added the current-source gate;
- replaced “yes, yes, no” with the actual three-limb explanation.

The external-authority registry now distinguishes direct source records from corpus-backed decisions. Validation now reports `513 confirmed, 2 external source records, 0 flagged, 0 failed`; the external count reflects two uses of the Honeysett record.
