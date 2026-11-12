# Comparative full-mirror review — ER Practice Guide

**Review date:** 2026-11-12 17:55 AWST  
**Purpose:** Compare the current guide baseline against the research available through the full read-only mirror, without changing guide content during the comparison.

## Scope and method

The comparison used the same deterministic MCP search path against:

1. the limited snapshot set used for the initial module build; and
2. the current full read-only mirror at:

```text
/Users/benobrien/briefer-claude/full-research-mirror/latest
```

The following 13 topic queries were run against both sources, with the top 25 distinct decision results compared:

- general protections;
- performance warnings;
- notification and response;
- support persons;
- suspension;
- drug and alcohol;
- safety;
- bullying and harassment;
- medical capacity;
- absenteeism and abandonment;
- social media;
- dishonesty;
- Commission remedies.

The guide's 126 unique `<Cite>` authorities were also checked against the MasterDB citation population in both sources.

## Results

| Measure | Limited snapshots | Full mirror | Difference |
|---|---:|---:|---:|
| MasterDB decisions | 30,081 | 30,084 | +3 |
| FWC/chunk rows | 530,627 | 921,914 | +391,287 |
| Distinct chunk decision IDs | 29,498 | 29,501 | +3 |
| Citation Map rows | 153,381 | 153,497 | +116 |
| Guide authorities present in MasterDB | 126/126 | 126/126 | none |

The three additional distinct decision IDs in the full mirror are:

- `[2026] FCA 1677`;
- `[2026] FCA 1682`;
- `[2026] FCAFC 141`.

They are Federal Court/Federal Court Full Court records and were not extracted in the current MasterDB population (`passes_completed = 0`). They did not produce additional results in the FWC-focused topic searches used for the guide comparison.

### Topic-search comparison

For every topic query except the deliberately narrow dishonesty query, the limited snapshot and full mirror returned the same top-result decision-ID set. No new decision IDs appeared in the full-mirror result set for:

- general protections;
- performance warnings;
- notification and response;
- support persons;
- suspension;
- drug and alcohol;
- safety;
- bullying and harassment;
- medical capacity;
- absenteeism and abandonment;
- social media; or
- Commission remedies.

The dishonesty query returned zero results in both sources. That is a query-design limitation, not evidence that the full mirror contains no dishonesty material.

## Conclusion

The initial modules would **not have been materially different merely because the full mirror had been available**, at least on the FWC conduct/performance research tested here.

The evidence supports a narrower conclusion:

> The initial limited snapshots already contained the relevant FWC decision population and the authorities used in the current guide. The full mirror adds substantial chunk-row volume and a small number of Federal Court records, but it did not produce additional top-ranked FWC authorities for the tested module topics.

That is a useful result. It means the main remaining improvements are not a simple matter of giving Claude more cases. They are:

- selecting and qualifying authorities well;
- distinguishing holdings from observations and synthesis;
- checking current legislation and procedure;
- incorporating Federal Court or Full Court material where it actually changes a proposition;
- checking source identity and pinpoints;
- avoiding overconfident generalisation from a narrow fact pattern.

## Where a genuinely broader second research pass could still add value

The current MCP interface exposes the full mirror's MasterDB, Citation Map and FWC chunk database. It does not yet expose every raw source family in the mirror as a dedicated research tool. A later targeted pass could therefore investigate:

1. **Federal Court and Full Court authorities** relevant to general protections, discrimination, capacity and procedural fairness.
2. **Current legislation and regulations** against the time-sensitive propositions in the guide.
3. **Source-text and provenance records** where a current proposition is presently supported by an indirectly quoted authority.
4. **Enterprise-agreement and award material**, but only for a clearly framed baseline question—not to turn one employer's process into a universal guide rule.
5. **Current procedural materials** for Commission representation, conciliation, costs and remedies.

Those should be targeted research questions, not a wholesale rewrite of the guide.

## Recommendation

Do not replace the current guide on the assumption that full-mirror access would have produced a fundamentally different baseline. Treat the current v0.2.0 guide as substantively supported by the same core FWC population available in the full mirror.

The next research work should be proposition-led:

- identify a proposition that may be current, contested or source-sensitive;
- query the full mirror and current primary source;
- record whether the proposition changes, is strengthened, or remains unchanged;
- update only where the evidence warrants it.

No guide content was changed as a result of this comparative review.
