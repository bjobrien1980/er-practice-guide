# Comparative live-production review — ER Practice Guide

**Review date:** 2026-11-12 17:55 AWST  
**Scope:** read-only comparison of the guide baseline against live Briefer production databases on MS64.

## Live sources inspected

The comparison used immutable, read-only SQLite connections to:

```text
/Users/benobrien/briefer-data/db/sqlite/briefer_master.db
/Users/benobrien/briefer-data/fwc-decision-chunks.db
/Users/benobrien/briefer-data/citation-map-v2.db
```

No live database, Qdrant collection, source corpus, pipeline state or operational record was modified. The live files were read through `mode=ro&immutable=1`.

The same deterministic topic queries used in the earlier snapshot/full-mirror comparison were run against live FWC chunk data and compared with the full mirror's MCP source.

## Live-versus-mirror results

| Measure | Live production | Full mirror |
|---|---:|---:|
| MasterDB decisions | 30,084 | 30,084 |
| FWC/chunk rows | 921,914 | 921,914 |
| Citation Map rows | 153,497 | 153,497 |
| Guide authorities present in MasterDB | 126/126 | 126/126 |

For all 13 topic queries, the live and full-mirror searches returned the same number of results and the same top-25 distinct decision-ID sets:

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

The dishonesty query returned zero results in both sources because the query was too narrow. That is a search-design limitation, not a substantive conclusion.

The live and mirror MasterDB decision identity populations also matched exactly on `(download_id, sha256)` for all 30,084 rows.

Raw SQLite file hashes differ between live and mirror. That is expected for a derived SQLite backup and is not evidence of content divergence; the decision identity and source-hash populations matched exactly.

## Comparison with the initial limited baseline

The initial bounded snapshots contained:

| Measure | Initial limited snapshots | Live production |
|---|---:|---:|
| MasterDB decisions | 30,081 | 30,084 |
| FWC/chunk rows | 530,627 | 921,914 |
| Citation Map rows | 153,381 | 153,497 |
| Guide authorities present | 126/126 | 126/126 |

The live production system therefore confirms the earlier conclusion: the initial baseline already contained the authorities returned by the tested FWC topic searches. The live system adds three MasterDB decisions and substantially more chunk rows, but it did not produce different top-ranked FWC results for the guide topics tested.

The three additional decision IDs previously identified in the full mirror are Federal Court/Federal Court Full Court records:

- `fca-2026-1677`;
- `fca-2026-1682`;
- `fcafc-2026-141`.

They are not extracted in the current MasterDB population and did not change the FWC-focused module searches.

## Conclusion

The live-production comparison does **not** justify a wholesale rewrite of the guide or a claim that the initial Claude build was materially constrained for the FWC conduct/performance topics tested.

It does support targeted follow-up work in areas not answered by this FWC-focused search comparison:

1. extract and assess the additional Federal Court/Full Court records before relying on them;
2. run targeted current-legislation and regulation checks;
3. review indirectly sourced authorities against original decisions;
4. rerun the dishonesty comparison with narrower searches;
5. examine live source text and provenance where a proposition is time-sensitive or contested.

No guide content was changed as a result of this live-production comparison.
