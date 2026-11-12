# Law currency

Per Ben's decision at the end of Phase 0, modules in this phase were built without live
currency checks against legislation.gov.au or fwc.gov.au — `WebFetch`/`WebSearch` are
hard-denied in `.claude/settings.json` for this project, and the project asked to proceed
without them for now rather than loosen that rule. Every module's frontmatter carries
`law_current_as_at: null` and `law_sources: []` until this is done, and nothing in the
rendered page claims a currency check that hasn't happened.

| Module | Provisions relied on | Currency checked | Known amendments to check when this is done |
|---|---|---|---|
| 5. Valid reason | FWA s.387(a) | Not yet | s.387(a) itself has not moved recently, but confirm no Secure Jobs, Better Pay Act 2022 or Closing Loopholes Acts 2023–24 amendments touch it before publishing. |

This table should grow as each module is built, and gets resolved either by lifting the
WebFetch/WebSearch block for `legislation.gov.au` and `fwc.gov.au`, or by Ben supplying
verified currency notes directly.
