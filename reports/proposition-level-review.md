# Proposition-level review — ER Practice Guide

**Review date:** 2026-11-12 17:55 AWST  
**Evidence basis:** live MS64 Briefer production databases, current official legislation register and official FWC guidance.  
**Scope:** load-bearing or time-sensitive propositions in the core and Tier 3 modules; not a sentence-by-sentence legal opinion on every paragraph.

## Executive conclusion

The review did not identify a reason to replace the guide's core analysis. It did identify several propositions that should be tightened before a later publication revision.

The most important findings are:

1. **Confirmed:** the general-protections reverse-onus explanation is materially sound after the v1.2 qualification.
2. **Confirmed:** the support-person proposition is consistent with current official FWC guidance, subject to the guide's existing instrument/policy qualification.
3. **Amend:** the performance-warning “four-part test” should be described as a recurring analytical framework in decisions, not as a universal statutory test or PIP requirement.
4. **Amend:** the suspension module still contains an internal contradiction: its new warning says suspension is not automatically routine or low-risk, but later text still says it is “routine and low-risk” where a contractual basis exists.
5. **Amend:** the after-acquired-evidence statement that an employer can “usually” rely on later-discovered dishonesty is too broad and needs a more careful formulation.
6. **Verify before reliance:** the current positive-duty, summary-dismissal-regulation and Commission-procedure propositions need direct current-source checks.

No guide content was changed during this review. The findings are recorded here for the next controlled content pass.

## Proposition findings

### P-001 — Current-law currency

**Modules:** all; especially 04, 10, 12, 13, 20 and 21.  
**Status:** **needs ongoing source check**.

The current official Fair Work Act compilation identified through the Federal Register is dated **7 July 2026**. The guide now carries a visible currency warning, which is the correct baseline control. The module metadata still has no module-specific `law_current_as_at` value, so `Last updated` must not be read as legal verification.

**Recommendation:** keep the global currency warning; populate a module-specific current-law date only when the relevant primary sources have actually been checked.

### P-002 — General protections and reverse onus

**Module:** 02.  
**Status:** **confirmed with qualification**.

The guide correctly distinguishes:

- the protected right, activity or attribute;
- adverse action;
- the statutory presumption about reason; and
- the separate question whether dismissal or adverse action occurred.

The current wording that the selected “doors” are screening questions rather than an exhaustive list is appropriate. The live MasterDB authorities used by the module remain present in production, including `[2024] FWC 2475`, `[2024] FWC 840`, `[2026] FWC 1138` and `[2026] FWC 1685`.

**Recommendation:** no immediate substantive amendment. Recheck the current Act text before the next release.

### P-003 — Notification and response

**Module:** 06.  
**Status:** **confirmed with qualification**.

The distinction between notification/opportunity to respond and the timing of the dismissal decision is sound. The new qualification that awards, EAs, contracts, policies and established processes may impose additional requirements is necessary and should remain.

**Recommendation:** no immediate substantive amendment.

### P-004 — Support persons

**Module:** 07.  
**Status:** **confirmed**.

The official FWC guidance states that there is no positive statutory obligation to offer a support person, and that the factor becomes relevant when an employee requests one and the employer unreasonably refuses. The guide now correctly qualifies that proposition by reference to awards, EAs, contracts, policies and established processes.

Official cross-check:

```text
https://www.fwc.gov.au/unreasonable-refusal-support-person
```

**Recommendation:** no immediate substantive amendment.

### P-005 — Performance warnings and PIPs

**Module:** 08.  
**Status:** **amend**.

The module currently presents a recurring four-element warning framework—deficiency, assistance/training, required standard and reasonable timeframe. That is useful, but it should not read as a universal statutory test.

The new opening qualification correctly says that a PIP is not universally required. The later language should also avoid “the warning must” where the proposition is a synthesis of decisions rather than statutory text.

**Recommended formulation:**

> In decisions dealing with s.387(e), the Commission commonly examines whether the warning identified the deficiency, the required standard, available assistance or training, and a reasonable opportunity to improve. The weight of each feature depends on the facts and any applicable instrument or policy.

### P-006 — Summary dismissal and reg 1.07

**Module:** 04.  
**Status:** **needs direct current-source verification and qualification**.

The module says the regulation’s listed conduct “will meet the standard on their own.” That is too categorical for a baseline guide. The regulation may identify conduct capable of constituting serious misconduct, but the application still depends on the current regulation, the employment relationship, the source of the summary-dismissal power, the facts and the process.

**Recommended formulation:**

> The regulation identifies examples of conduct that may constitute serious misconduct. Whether summary dismissal is available and fair still depends on the current regulation, the contract or applicable instrument, the facts, and the s.387 assessment.

The current official Act compilation and current Fair Work Regulations should be checked directly before this section is treated as current.

### P-007 — Suspension

**Module:** 18.  
**Status:** **critical internal contradiction**.

The module now says:

> Suspension is not automatically routine or low-risk.

But later it still says:

> Where that basis exists and is followed, suspension pending investigation is routine and low-risk.

Those statements do not sit comfortably together. A contractual or instrument-based power may make suspension lawful, but does not make the decision low-risk in every case.

**Recommended edit:** replace the later sentence with:

> Where that basis exists and is followed, suspension may be available, but its legal and practical risk still depends on the purpose, duration, pay position, process, facts and applicable instrument.

### P-008 — Drug and alcohol testing

**Module:** 10.  
**Status:** **substantively bounded but still source-sensitive**.

The new opening qualification is appropriate. The following proposition—that a positive result can, on its own, be a valid reason—must remain tied to the particular regime, policy, test reliability, role and circumstances of the cited decision. The module's own cited `[2026] FWC 218` decision is not a universal rule for all testing regimes.

**Recommendation:** retain the qualification and amend the proposition to:

> In a safety-critical role, under a clear and communicated testing regime, a reliable confirmed positive result may itself provide a valid reason. That conclusion cannot be transferred to a different testing method, policy, role or medical context without further analysis.

### P-009 — Bullying, sexual harassment and positive duty

**Module:** 12.  
**Status:** **current-source verification required**.

The pathway separation is sound. The module itself acknowledges that its positive-duty treatment has not been independently checked for currency. That warning should remain until the current Sex Discrimination Act text and current official guidance are checked directly.

**Recommendation:** treat positive-duty propositions as provisional in v0.2.0; do not expand them from the current module until the primary-source check is complete.

### P-010 — Medical capacity

**Module:** 13.  
**Status:** **amend for precision**.

The three-part capacity framework is useful, but it is an analytical framework drawn from authority, not a universally exhaustive statutory test. The module's new privacy and adjustment paragraph improves the position.

**Recommendation:** change “the three-part test” in the instructional framing to “a commonly used analytical framework” and retain the explicit privacy, adjustment and discrimination qualifications.

### P-011 — Social media and out-of-hours conduct

**Module:** 15.  
**Status:** **confirmed with qualification**.

The module correctly treats connection to employment as fact-dependent and now warns against treating employer identification or embarrassment as a legal rule. Its treatment of privacy settings, authenticity and protected expression is appropriately cautious.

**Recommendation:** no immediate substantive amendment. The cited Full Bench authority should be independently checked before the next legal currency pass.

### P-012 — Dishonesty and falsified records

**Module:** 16.  
**Status:** **amend**.

The fact/intent distinction is sound. The after-acquired-evidence section remains too broad:

> you can usually still rely on it to support that a valid reason existed.

That statement needs to distinguish the existence of a reason at the dismissal date, later discovery, procedural fairness and remedy. Later evidence may affect the assessment, but it does not create a decision-maker reason that did not exist or repair the original process.

**Recommended formulation:**

> Later-discovered evidence may bear on whether a reason existed at the time of dismissal or on remedy, depending on the facts and authority. It does not create a reason the decision-maker did not have, and it cannot retrospectively supply the opportunity to respond or other procedural fairness that was absent at dismissal.

### P-013 — Remedies and reinstatement

**Module:** 21.  
**Status:** **confirmed at the statutory-sequence level**.

The proposition that compensation cannot be ordered unless reinstatement is inappropriate is consistent with the s.390 sequence. The discretionary nature of remedy is also correctly stated.

**Recommendation:** current legislation and current Commission practice should still be checked before relying on any current procedural or compensation calculation detail.

### P-014 — Commission representation, conciliation and costs

**Module:** 20.  
**Status:** **needs current procedural-source verification**.

The general treatment is appropriately cautious, but statements about representation, costs and conciliation outcomes are procedural and time-sensitive. The module should not be treated as current solely because the cited cases remain in the corpus.

**Recommendation:** add current FWC procedural guidance to the next source check and distinguish:

- statutory rule;
- Commission discretion;
- case-specific costs outcome;
- practical settlement advice.

## Priority amendments from this review

Before the next publication revision I would make four direct text amendments:

1. Remove the remaining “routine and low-risk” suspension sentence.
2. Replace the “four-part test” wording in the performance-warning module with “commonly used analytical framework”.
3. Reframe the reg 1.07 summary-dismissal examples as capable of supporting serious misconduct, not automatically determinative.
4. Replace the “usually still rely” after-acquired-evidence paragraph with a more precise existence/reason/procedural-fairness/remedy distinction.

I would not add new Federal Court authorities until the three additional live records are extracted and independently reviewed.

## Sources checked

- Federal Register of Legislation, current Fair Work Act compilation: <https://www.legislation.gov.au/C2009A00028/latest>
- Federal Register of Legislation, current Act text/downloads: <https://www.legislation.gov.au/C2009A00028/latest/text>
- Fair Work Commission, unreasonable refusal of a support person: <https://www.fwc.gov.au/unreasonable-refusal-support-person>
- Fair Work Commission, unfair dismissals benchbook: <https://www.fwc.gov.au/benchbook/unfair-dismissals-benchbook>
- Live MS64 MasterDB, FWC chunk database and Citation Map listed above.

No external source, live database or guide module was modified during this review.
