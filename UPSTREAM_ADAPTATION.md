# Upstream Adaptation Record

## Current baseline

- Upstream: `https://github.com/Yuan1z0825/nature-skills.git`
- Adapted commit: `14ca69710cae192325395a380e9cdd4ae5d9d0c8`
- Adaptation date: 2026-11-16
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

## 2026-11 synchronization

- Previous adapted commit: `ebd722e18808442688bd205917a3e774195c258f`.
- Reviewed upstream HEAD: `14ca69710cae192325395a380e9cdd4ae5d9d0c8`.
- IEEE plugin version: `0.3.0`; 22 task skills plus `ieee-shared`.
- Method: compare the complete upstream delta, three-way port reusable runtime
  fixes against the prior adapted source, and resolve behavior manually against
  the IEEE contract. Preserve stronger existing IEEE safeguards. This is a
  semantic adaptation, not a declaration that every upstream file was copied.

| Upstream change family | IEEE disposition |
|---|---|
| Task-scoped discovery, writing and revision | Preserve local-edit scope, existing framing and approvals; missing package metadata blocks only dependent work. Complete-record conversion stays local. |
| Reviewer forensic audit | Add an editorial numerical/aggregation/provenance audit after reports freeze. Keep audit-only errors separate from independent-review consensus. Add packet/slot, task/run, resource and sampled-stability checks. |
| Vector schematics and figure QA | Add editable SVG workflow/auditor with IEEE 88.9/182 mm canvas defaults. Port PDF text-transform, panel input, collision and backend-preference fixes; retain IEEE rendering and data-integrity gates. Size thresholds remain internal QA settings. |
| OpenAlex, arXiv, Scopus and Crossref | Add header-based optional OpenAlex key configuration; suppress false error/empty records, tolerate unknown dates and citation fields, and preserve IEEE-first source dispatch. |
| Citation conversion and scope | Port author/date/export/retry and XML/input handling fixes where applicable. Keep IEEE exact named-journal scope, not upstream Nature-family allowlists. |
| Downloader runtime | Port service-specific Springer credentials/host fixes, unsuccessful-response checks, open-license determination, collision-safe PDF names and atomic browser writes. Preserve manual authentication-challenge handoff. |
| Image2PPT runtime | Port atomic config writes, secure XML/URL/page-path handling, transparent-image compositing, OPC targets, PowerPoint slide-size limits and workdir preservation. Preserve existing consent, COM and external-config hardening. |
| Paper cards and Office export | Validate source page ranges; account for grouped slide transforms; preserve Markdown on DOCX export, table separators, inline math, superscripts, claim antecedents and figure node identities. Keep the stronger local Windows Mermaid argv/PowerShell handling and adapt its regression tests. |
| `nature-paper-xray` | Add `ieee-paper-xray`: reconstruct engineering reasoning with labelled teaching examples and source-anchored evidence boundaries. An unisolated component is not established, not decorative. |
| `nature-paper2word` | Add `ieee-paper2word` with paragraph-sample helper and MIT notice. Explicit IEEE requirements/templates and numeric references override engine defaults. External engine availability and rendered QA are required; no unverified deterministic-output or submission-ready promise. |
| Optional publisher/PDF readers | Document an optional existing connected reader route, without provider pricing/quota claims, mandatory credentials or unrequested confidential uploads. |
| Installer and metadata | Port literal-tilde destination handling, add offline manifest/UI/resource validation, preserve transactional rollback and unrelated skills, update bilingual index and plugin version. |

### Deliberate exclusions and retained differences

- Website, promotions, RDA result dumps, star-history assets and maintenance
  scripts do not belong in this engineering skill suite.
- `nature-social-science`, Nature/CNS exact-journal lists, Nature publication
  presets and flagship typography/word limits are not default IEEE behavior.
- `nature-paper-trans` is not installed as a default IEEE translation route.
  Its image-generated, raster-only PDF delivery has a different fidelity and
  accessibility contract from the equation-aware bilingual `ieee-reader`.
  A future explicit image-translation workflow needs its own IEEE fidelity,
  service authorization and rendered-page validation design.
- Provider-specific OpenRouter generation remains excluded; use the existing
  provider-neutral graphical-abstract route and user-authorized image tools.
- Upstream punctuation taste rules, hardcoded free-tier claims and blanket
  approval stages are not adopted as universal engineering requirements.
- No claim is made that external publication requirements were refreshed in
  this update; existing dated IEEE rules still require current official checks
  when used for an actual submission.

### Validation scope

Runtime tests use an isolated ignored `.upstream/test-env` and mocked fixtures;
no model tasks, live publisher credentials, paid APIs or confidential manuscripts
are needed. Run the repository Python regression groups, Image2PPT suite,
downloader Node tests, installer rollback/state/tilde tests, skill metadata checks
and `git diff --check`. Optional live Elsevier tests are deliberately skipped.
The new Word helper is tested against its declared engine dependency; this does
not certify an arbitrary journal template or install the engine for users.
Independent skill forward tests cover a local sentence edit, audit-only impossible
success counts, missing Word engine/template, and an unablated component with a
clearly labelled toy example. Their findings corrected two contradictory rules.

Validation completed for this adaptation: 188 core/citation Python tests, 81
search/downloader Python tests (5 optional live tests skipped), 190 Image2PPT
Python tests and 121 downloader Node tests passed: 580 automated test cases.
All 23 skill packages passed metadata/resource and skill-creator validation.
Installer rollback/prune, updater state isolation and both tilde-expansion
suites passed. The local Codex install was backed up and the installer
`--check` verified the updated destination against source. External-engine
PDF/Word rendering against a real submission manuscript and live services
remain outside this offline validation.
