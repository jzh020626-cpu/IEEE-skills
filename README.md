# IEEE Transactions Skills

[中文版说明](README.zh-CN.md)

IEEE Transactions Skills is a Codex skill suite for robotics, automation,
control, communications, industrial informatics, and networked intelligent
systems research. It targets IEEE Transactions-style manuscripts rather than
general scientific or life-science writing.

The suite is designed for PhD-level workflows around journals such as T-ASE,
TII, T-RO, RA-L, TAC, TCST, TIE, TWC, TCOM, and IoT-J. It focuses on strict
submission readiness: IEEEtran structure, numbered references, double-column
readability, reproducible experiments, baselines, ablations, stability or
convergence arguments, communication constraints, latency, robustness, and
venue-specific checklists.

## What this repository contains

```text
.
|-- README.md
|-- LICENSE
|-- UPSTREAM_ADAPTATION.md
|-- scripts/
|   |-- autoupdate-skills.sh
|   |-- check-nature-upstream.sh
|   |-- nature-upstream.lock
|   `-- update-codex-skills.sh
`-- skills/
    |-- ieee-shared/
    |-- ieee-writing/
    |-- ieee-polishing/
    |-- ieee-citation/
    |-- ieee-figure/
    |-- ieee-data/
    |-- ieee-experiment-log/
    |-- ieee-response/
    |-- ieee-reviewer/
    |-- ieee-submission-audit/
    |-- ieee-academic-search/
    |-- ieee-literature-pipeline/
    |-- ieee-paper-card/
    |-- ieee-reader/
    |-- ieee-ref-verifier/
    |-- ieee-downloader/
    |-- ieee-paper2ppt/
    |-- ieee-paper-to-patent/
    |-- ieee-statistics/
    `-- ieee-proposal-writer/
```

Each skill follows the standard Codex skill layout:

- `SKILL.md`: trigger description and operating instructions.
- `manifest.yaml`: declarative routing metadata for every shipped skill.
- `static/`: reusable fragments loaded by the skill.
- `references/`: detailed guidance, checklists, examples, or source notes.
- `scripts/`: local helper scripts used by that skill.
- `assets/`: optional figures or demonstration resources where needed.

Runtime caches and local state are intentionally excluded from version control:
`.upstream/`, `__pycache__/`, `.pytest_cache/`, `.env`, virtual environments,
and generated logs.

## Design goals

This repository is intentionally IEEE-first:

- Use IEEE numbered citation style (`[1]`, `[2]`, ...), not author-year style.
- Prefer IEEE archival sources and engineering venues for citation support.
- Preserve IEEE double-column constraints in figures, captions, tables, and
  prose density.
- Treat technical novelty as a system, algorithm, control, communication, or
  engineering contribution, not as a broad biological discovery claim.
- Require clear problem formulation, assumptions, baselines, ablations,
  reproducibility artifacts, and limitations.
- Support T-ASE `Note to Practitioners` drafting and auditing.
- Support control-paper checks for assumptions, theorem/proof structure,
  stability, convergence, feasibility, and conference-extension value.
- Support robotics and communications checks for hardware/simulation setup,
  task scenes, latency, throughput, packet drops, robustness, and statistical
  significance.

## Install into Codex

From this repository:

```bash
cd /path/to/IEEE-skills
scripts/update-codex-skills.sh
scripts/update-codex-skills.sh --check
```

By default the installer copies only `skills/ieee-*`, including the internal
`ieee-shared` dependency.

into:

```text
~/.codex/skills
```

It does not prune or overwrite unrelated skills. It also writes a local install
manifest named:

```text
~/.codex/skills/.ieee-trans-skills-install.txt
```

Useful options:

```bash
scripts/update-codex-skills.sh --check
scripts/update-codex-skills.sh --dest /tmp/skills-check
scripts/update-codex-skills.sh --pull
scripts/update-codex-skills.sh --prune
```

`--prune` removes only directories previously managed by this installer and no
longer shipped by this repository.

## Skill index

| Skill | Main use |
|---|---|
| [`ieee-writing`](skills/ieee-writing/README.md) | Draft or restructure IEEE Transactions manuscript sections from claims, results, figures, notes, or Chinese drafts. |
| [`ieee-polishing`](skills/ieee-polishing/README.md) | Polish, translate, and tighten prose into IEEE Transactions-style English. |
| [`ieee-citation`](skills/ieee-citation/README.md) | Add IEEE-style numbered citations, verify claim support, and manage RIS/ENW/BibTeX-oriented citation workflows. |
| [`ieee-figure`](skills/ieee-figure/README.md) | Create, revise, or audit IEEE single-column/double-column manuscript figures. |
| [`ieee-data`](skills/ieee-data/README.md) | Prepare reproducibility packages, code/data availability notes, seeds, logs, parameters, and hardware/simulation metadata. |
| [`ieee-experiment-log`](skills/ieee-experiment-log/README.md) | Normalize simulation, hardware, field, network, training, and benchmark runs into traceable engineering logs. |
| [`ieee-response`](skills/ieee-response/README.md) | Draft or audit point-by-point IEEE reviewer responses. |
| [`ieee-reviewer`](skills/ieee-reviewer/README.md) | Simulate IEEE Transactions reviewer assessment before submission or revision. |
| [`ieee-submission-audit`](skills/ieee-submission-audit/SKILL.md) | Run a strict pre-submission audit for IEEEtran, page limits, figures, references, NtP, reproducibility, and venue-specific hard constraints. |
| [`ieee-academic-search`](skills/ieee-academic-search/README.md) | Multi-source literature search, citation verification, DOI/arXiv/IEEE-oriented reference management, and optional MCP dispatch. |
| [`ieee-literature-pipeline`](skills/ieee-literature-pipeline/README.md) | Automated literature discovery, scoring, clustering, and reading workflow for engineering manuscripts. |
| [`ieee-paper-card`](skills/ieee-paper-card/README_EN.md) | Deep-read one engineering paper into a source-grounded Sections 01–16 claim–evidence card. |
| [`ieee-reader`](skills/ieee-reader/README.md) | Build figure/table-aware Chinese-English paper readers for IEEE or engineering papers. |
| [`ieee-ref-verifier`](skills/ieee-ref-verifier/README.md) | Verify DOI, author order, venue, Early Access/issue metadata, pages/article numbers, and conference/journal versions. |
| [`ieee-downloader`](skills/ieee-downloader/README.md) | Configure legitimate institutional or open-access paper retrieval and organize authorized PDFs. |
| [`ieee-paper2ppt`](skills/ieee-paper2ppt/README.md) | Build IEEE-style Chinese presentation decks from robotics, automation, control, communications, or industrial informatics papers. |
| [`ieee-paper-to-patent`](skills/ieee-paper-to-patent/README.md) | Convert engineering papers, theses, technical reports, source code, or figures into Chinese invention patent drafts. |
| [`ieee-statistics`](skills/ieee-statistics/README.md) | Audit seeds/runs, independent units, uncertainty, benchmark aggregation, leakage, comparisons, and figure statistics. |
| [`ieee-proposal-writer`](skills/ieee-proposal-writer/README.md) | Run a proposal-first research writing workflow for IEEE Transactions manuscripts. |

## Typical triggers

After installation, Codex can trigger these skills by natural language or by
explicit skill name.

Examples:

```text
Use ieee-writing to rewrite my T-ASE introduction.
Use ieee-polishing to polish this Chinese draft into IEEE Transactions English.
Use ieee-citation to add numbered IEEE references for these claims.
Use ieee-figure to audit whether this figure works in a double-column paper.
Use ieee-data to prepare a reproducibility package checklist.
Use ieee-experiment-log to normalize these simulation and hardware run notes.
Use ieee-ref-verifier to verify every reference and publication version.
Use ieee-statistics to audit seeds, repeated runs, uncertainty, and leakage.
Use ieee-paper-card to deep-read this robotics or communications paper and audit its claim-evidence boundaries.
Use ieee-response to draft replies to TII reviewer comments.
Use ieee-submission-audit to run a strict pre-submission check for T-ASE.
```

For fully deterministic routing, name the skill explicitly:

```text
$ieee-submission-audit
```

## Strict IEEE submission audit

`ieee-submission-audit` is the strict mode for final checks. It is intended for
manuscripts that are close to submission or resubmission.

It checks:

- IEEEtran compatibility and front-matter structure.
- Title, abstract, keywords, and contribution statements.
- T-ASE `Note to Practitioners` separation from the abstract.
- Numbered citation style and reference completeness.
- Figure readability under IEEE single-column and double-column constraints.
- Table density, caption self-sufficiency, and cross-reference hygiene.
- Page budget, appendix placement, and supplementary material boundary.
- Baselines, ablations, statistical evidence, and robustness evidence.
- Control-specific assumptions, theorems, proofs, stability, and convergence.
- Robotics and automation setup: task scene, hardware/simulation setup,
  safety boundaries, latency, throughput, and reliability.
- Reproducibility package readiness: code, datasets, seeds, logs, model
  weights, ROS bags where relevant, parameters, and run commands.

## Optional dependencies

Most skills are prompt/instruction skills and do not require extra packages.
Some helper scripts have optional dependencies:

```bash
python -m pip install -r skills/ieee-paper-to-patent/requirements.txt
python -m pip install -r skills/ieee-academic-search/mcp-server/requirements.txt
```

Run these only when using the corresponding scripts.

## IEEE academic search MCP

`ieee-academic-search` includes an optional MCP server under:

```text
skills/ieee-academic-search/mcp-server
```

Default behavior is IEEE-first and low-risk:

- CrossRef/OpenAlex-style DOI metadata.
- arXiv discovery for preprints.
- IEEE Xplore or official publisher pages when available.
- Scopus and ScienceDirect only when explicitly configured and requested.

Optional Elsevier/Scopus credentials are not stored in this repository. Configure
them locally through environment variables or `pybliometrics` configuration:

```bash
export ELSEVIER_API_KEY=...
export SCOPUS_API_KEY=...
export IEEE_ACADEMIC_SEARCH_LIVE_ELSEVIER=1
```

Live API tests should be run only when credentials and quota are available.

## Upstream synchronization

This repository tracks reusable architecture changes from upstream
`nature-skills` while preserving IEEE behavior. The current semantic adaptation
is documented in [`UPSTREAM_ADAPTATION.md`](UPSTREAM_ADAPTATION.md), and the
adapted upstream SHA is stored in `scripts/nature-upstream.lock`.

Script:

```bash
scripts/check-nature-upstream.sh
```

The script compares the upstream `nature-skills` HEAD with the last IEEE-adapted
commit and creates a pending state when upstream changes appear. It does not
mark the update complete automatically. After a human or Codex automation ports
the reusable structure into IEEE form and validation passes, mark the update:

```bash
scripts/check-nature-upstream.sh --mark <commit>
```

Important boundary:

- Upstream `nature-*` content is source material for architecture diffs only.
- Active skill behavior must remain `ieee-*`.
- Do not copy life-science, clinical, genomics, Nature Portfolio, Nat Commun,
  CNS, or Cell Press assumptions into default IEEE instructions.
- Do not port CAPTCHA/slider automation. Authentication challenges require user
  handoff in the authorized browser.

## Validation checklist

Before publishing or installing an updated version:

```bash
scripts/update-codex-skills.sh --check
```

Recommended additional checks:

```bash
rg -n "__pycache__|\\.pytest_cache|\\.upstream" .
rg -i "Nature|Nat Commun|CNS|Cell Press|biolog|clinical|genomic|single-cell" skills README.md
rg -i "IEEE|T-ASE|TII|Transactions|Note to Practitioners|double-column|baselines|ablation|stability|latency" skills README.md
```

Some legacy assets or source notes may mention non-IEEE origins. They should not
appear as default writing behavior, active routing, or recommended examples for
IEEE submissions.

## Repository maintenance

Recommended publish hygiene:

- Keep source skills, references, scripts, and small reusable assets in Git.
- Do not commit runtime caches, local credentials, downloaded PDFs, browser
  sessions, `.env` files, virtual environments, or local `.upstream` state.
- Keep large legacy demo assets only when a skill or test still depends on
  them; otherwise replace them with smaller IEEE-oriented examples over time.
- Prefer focused commits that separate README/documentation changes from skill
  behavior changes.

## License

See [`LICENSE`](LICENSE).
