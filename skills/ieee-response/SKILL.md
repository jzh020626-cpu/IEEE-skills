---
name: ieee-response
description: >-
  Draft, audit, or revise IEEE Transactions and Letters revision correspondence: point-by-point reviewer responses, rebuttal letters, revision cover letters, LaTeX response/cover templates, and red-marked manuscript excerpts. Use for decision emails, reviewer comments, editor instructions, revision packages, major/minor revision, marked manuscripts, appeals that need separate routing, or Chinese requests such as 审稿意见回复、逐点回复、修回信、返修 cover letter、标红修改、LaTeX 回复模板.
---

# IEEE Reviewer Response Router

Use `manifest.yaml` and load the response core before drafting.

## Routing protocol

1. Read `manifest.yaml` and every `always_load` path.
2. Use `references/intake-and-routing.md` to select `draft`, `audit`, `revise`, `triage-only`, `cover-letter`, `revision-package`, `latex-template`, or `appeal-like`.
3. If the user pasted a decision email, extract manuscript ID/title, journal, decision, deadline, required files, editor instructions, reviewer boundaries, and portal constraints before drafting.
4. Preserve editor items as `E.1...` and reviewer items as `R1.1...`; classify novelty, theory, experiment, baseline, ablation, statistics, clarity, citation, format, reproducibility, or venue fit.
5. Build a strategy/tracker, then draft a direct answer, action/evidence, manuscript location, and scoped limitation or disagreement for every item.
6. If manuscript text is edited, work on a copy and mark changes visibly. Revised excerpts quoted in the response are italic.
7. In print/LaTeX output, begin each reviewer on a new page. Use templates under `templates/` when requested.
8. Run `references/qa-checklist.md` and return a readiness state.

## Red lines

- Never invent experiments, analyses, citations, statistics, line numbers, figure panels, supplements, editor requirements, reviewer identity, or completed changes.
- Do not claim submission readiness while placeholders remain.
- Respectfully disagree when supported; do not use hostile language or convenience as the main reason to decline evidence.
- For conference extensions, identify the prior paper and added archival value without inventing a universal percentage threshold.
- Route an actual appeal separately instead of disguising it as a routine revision response.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
