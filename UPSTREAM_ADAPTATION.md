# Upstream Adaptation Record

## Current baseline

- Upstream: `https://github.com/Yuan1z0825/nature-skills.git`
- Adapted commit: `ebd722e18808442688bd205917a3e774195c258f`
- Adaptation date: 2026-09-01
- Tracked lock: `scripts/nature-upstream.lock`

## 2026-08 synchronization

- Upstream baseline: `adb7b8a5a7d72ed6fe9f71e085785e9972dd8db2`
- Scope: substantive skill/tooling capabilities added after the 2026-07 baseline.
- Policy: port workflow and validation improvements semantically; do not copy Nature flagship rules, life-science assumptions, marketing assets, or unverified venue limits into IEEE workflows.

This repository performs a semantic IEEE adaptation. It does not bulk-rename upstream content.

## 2026-09 synchronization

- Previous baseline: `adb7b8a5a7d72ed6fe9f71e085785e9972dd8db2`
- New upstream baseline: `ebd722e18808442688bd205917a3e774195c258f`
- Scope: reusable writing discipline, engineering evidence-chain alignment,
  multi-panel figure architecture, rendered figure QA, Image2PPT reconstruction,
  dependency notes, and Codex plugin packaging.
- Boundary: Nature Machine Intelligence/flagship Nature limits, Nature-specific
  AI policy, marketing/star-history content, and provider-specific OpenRouter
  routing remain excluded.

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
| Codex skill metadata | Added or refreshed `agents/openai.yaml` for every installed IEEE skill |
| main-text discipline | Added result classification, main/caption/Supplementary Material/appendix/artifact allocation, deletion checks, paragraph necessity, and claim-repetition auditing |
| Discussion calibration | Added finding-to-interpretation sequencing, modal-strength gates, claim-specific limitations, and uncertainty-resolving future work |
| engineering evidence chain | Added algorithm, control/theory, robotics/system, communications/networking, and benchmark routes across Abstract–Conclusion |
| multi-panel figure architecture | Added distinct engineering evidence roles and across-figure claim progression without Nature corpus examples |
| rendered figure QA | Added PyMuPDF collision/media-box auditing and physical-point panel alignment for Matplotlib and R/patchwork while retaining IEEE 88.9/182 mm widths and rejecting tight-crop width drift |
| AI graphical abstracts | Added provider-neutral concept/provenance/policy routing with explicit external-service authorization and no submission-policy assumptions |
| `nature-image2ppt` | Added separate `ieee-image2ppt` for faithful reconstruction of existing slide images; preserved the bundled MIT license and upstream Image2PPT source provenance |
| Image2PPT hardening | Removed unverified OCR cost/quota claims, made external OCR run-scoped and explicit-consent-only, moved persistent configuration outside the replaceable skill tree, rejected Windows `convert.exe` as ImageMagick, and replaced the PowerShell heuristic with a real PowerPoint COM probe |
| Codex plugin package | Added a validated `.codex-plugin/plugin.json` for the IEEE suite; repo-local marketplace metadata was not copied without a verified source-path/install flow |
| dependency and installer safety | Installer reports required figure/Image2PPT dependencies without installing them, preserves unrelated non-`ieee-*` skills even if a manifest is polluted, and points commands at the installed destination |

## Intentionally not ported

- Nature/CNS/Cell Press venue rules and broad-audience editorial positioning.
- Life-science-only examples, MeSH/PubMed-first workflow defaults, genomics/single-cell templates, and biological replicate assumptions.
- Website/marketing copy and upstream bilingual promotional README additions.
- OpenRouter-specific image-generation code; IEEE schematic generation remains routed through the installed image/figure tools.
- Nature Machine Intelligence article limits, display/Extended Data counts,
  NMI-specific data/code placement, Software Submission Checklist, and other
  Nature Portfolio stage rules.
- Upstream repo-local marketplace metadata whose `source.path: "./"` has not
  been verified against this private repository layout; the validated plugin
  manifest is included without claiming marketplace installation.
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
