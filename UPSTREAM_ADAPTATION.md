# Upstream Adaptation Record

## Current baseline

- Upstream: `https://github.com/Yuan1z0825/nature-skills.git`
- Adapted commit: `adb7b8a5a7d72ed6fe9f71e085785e9972dd8db2`
- Adaptation date: 2026-08-08
- Tracked lock: `scripts/nature-upstream.lock`

## 2026-08 synchronization

- Upstream baseline: `adb7b8a5a7d72ed6fe9f71e085785e9972dd8db2`
- Scope: substantive skill/tooling capabilities added after the 2026-07 baseline.
- Policy: port workflow and validation improvements semantically; do not copy Nature flagship rules, life-science assumptions, marketing assets, or unverified venue limits into IEEE workflows.

This repository performs a semantic IEEE adaptation. It does not bulk-rename upstream content.

## Ported in this update

| Upstream capability | IEEE adaptation |
|---|---|
| `nature-experiment-log` | New `ieee-experiment-log` with control, robotics hardware, and communications examples |
| `nature-ref-verifier` | New `ieee-ref-verifier` for DOI, Early Access, article-number, conference/journal, and version-of-record checks |
| `nature-statistics` | New `ieee-statistics` for seeds/runs, benchmark aggregation, dependence, leakage, uncertainty, and engineering figures |
| shared package rename | `_ieee_shared` migrated to installable internal `ieee-shared` |
| strict citation-impact audit | Added to `ieee-academic-search` with conservative independent-citation rules |
| downloader provider architecture | Added modular API/OA/CNKI/institutional routing, credentials, SI confirmation, validation, and manifests |
| figure templates/preferences/validator | Added persisted Python/R preference, semantic template-adaptation gate, engineering-safe demos, and static preflight |
| paper-to-PPT QA | Added crop/alignment/de-template gates and `audit_pptx_quality.py` |
| patent disclosure workflow | Added technical-disclosure and disclosure-iteration modes plus Office/CNIPA tooling |
| response LaTeX package | Added cover letter, response, redline templates, decision-email parsing, and revision-package routing |
| writing submission package | Added initial-submission task, IEEE metadata/ORCID/prior-version checks, and templates |
| reviewer domain gates | Rebuilt around official IEEE peer-review axes and engineering domain gates |
| startup updater | Added Codex-default `autoupdate-skills.sh` |
| missing skill manifests | Added IEEE-adapted manifests for experiment logging, literature pipeline, proposal writing, reference verification, reviewer simulation, and the shared package |
| `nature-paper-card` | Added `ieee-paper-card` with algorithm, system, theory, benchmark, application, and review lenses for traceable single-paper deep reading |
| equation-aware reader | Added stable equation IDs, source-map equation records, low-confidence visual fallback, and `validate_reader_math.py` |
| response-package consistency | Added quote/manuscript and marked/clean consistency checks with a blocking delivery gate |
| reviewer concern traceability | Added engineering concern axes, severity/blocking calibration, evidence pointers, resolution tests, and independent-review synthesis rules |
| shared consistency and compliance | Added cross-section numeric/terminology/assumption sweeps and conditional robotics, spectrum, cybersecurity, data, and dual-use readiness checks |
| figure rendering safety | Added PDF glyph-size auditing, monotone interpolation helpers, uncertainty/annotation checks, and panel-by-panel QA |
| proposal-writer expansion | Added compose/revise/hybrid modes, scope control, evidence-first foundation files, specialist lenses, review-paper framing, and low-commitment fallback |
| citation metadata integrity | Changed default export to RIS and made incomplete author metadata a blocking condition unless explicitly overridden |
| downloader slim routing | Added on-demand institutional-browser and delivery/failure references while preserving manual security-challenge handoff |
| transactional installer | Added destination-scoped state/locks, staging, backup, rollback, safe pruning, and isolation/safety tests |
| Codex skill metadata | Added or refreshed `agents/openai.yaml` for all 20 installed IEEE skills |

## Intentionally not ported

- Nature/CNS/Cell Press venue rules and broad-audience editorial positioning.
- Life-science-only examples, MeSH/PubMed-first workflow defaults, genomics/single-cell templates, and biological replicate assumptions.
- Website/marketing copy and upstream bilingual promotional README additions.
- OpenRouter-specific image-generation code; IEEE schematic generation remains routed through the installed image/figure tools.
- CAPTCHA, slider, or anti-bot automation. Verification is always handed to the user in the authenticated browser.

## IEEE rule refresh

Generic rules were refreshed against official IEEE Author Center and society pages. The suite now treats the named journal's current instructions as authoritative and records a check date for changing requirements. Notable current checks include:

- ORCID for all IEEE journal authors.
- 88.9 mm one-column / 182 mm two-column figure planning, with 300 dpi color/grayscale and 600 dpi black-and-white line-art floors.
- T-ASE 100-300 word Note to Practitioners after the Abstract and before Index Terms; 200-word Regular / 50-word Communication Abstract limits; current 10-page Regular submission target.
- TII 10-page New Research, 12-page Review/SoA with current permission logic, 4-page Letters, plus current anonymity/institutional-email checks.
- TAC/TCST current article-type page rules and explicit prior-version added-value disclosure.
- No universal IEEE conference-extension percentage rule.

## Safety and provenance

- The upstream commit is recorded in a tracked lock file.
- `check-nature-upstream.sh` creates only local ignored pending state until an adaptation is validated and marked.
- Credentials, cookies, downloaded papers, browser state, generated artifacts, and runtime caches remain excluded from version control.
