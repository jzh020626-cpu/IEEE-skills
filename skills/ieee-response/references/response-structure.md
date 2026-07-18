# Response structure

Use this file when drafting or auditing a reviewer response, revision cover letter, marked manuscript, or combined revision package.

## Default package

Return the response in this order unless the user asks for another format:

1. Response strategy summary.
2. Comment-response tracker.
3. Draft point-by-point response letter.
4. Draft revision cover letter when requested or when returning a combined package.
5. Marked manuscript changes when requested.
6. LaTeX deliverables when requested.
7. Manuscript change checklist.
8. Missing information / risk flags.
9. Chinese confirmation notes when useful.

## Response strategy summary

Keep this short and editor-readable:

```text
Response strategy summary
- Decision type: Major revision
- Task mode: draft
- Package readiness: draft_with_placeholders
- Overall posture: Cooperative, evidence-forward, non-defensive
- Major risks: missing validation results; unclear replicate definition
- Suggested ordering: address editor first, then Reviewer 1 and Reviewer 2 in full
```

Decision types:

- `minor revision`
- `major revision`
- `revise-and-resubmit`
- `transfer after review`
- `appeal-like case` routed outside the default workflow
- `unclear` when the decision type is not supplied

Task modes:

- `draft`
- `audit`
- `revise`
- `triage-only`
- `cover-letter`
- `revision-package`
- `latex-template`
- `appeal-like`

Package readiness:

- `ready_to_submit`: no unresolved placeholders or missing facts remain.
- `draft_with_placeholders`: usable draft, but visible placeholders remain.
- `needs_author_input`: final text depends on facts the author has not supplied.
- `blocked`: credible revision response is blocked by ethics, compliance, data integrity, central evidence, or appeal-like routing.

## Comment-response tracker

Use a compact table:

```markdown
| ID | Reviewer concern | Type | Severity | Proposed action | Readiness | Missing author input |
|---|---|---|---|---|---|---|
| R1.1 | Missing independent validation | Evidence / validation | Major | ACCEPT_ANALYSIS | needs_author_input | Need result summary and manuscript location |
```

Keep reviewer concern text short in the tracker. Preserve the full wording in the letter when available.
Use `E.1`, `E.2`, etc. for editor instructions and list them before reviewer comments.

## Point-by-point letter anatomy

Use this default structure:

```markdown
Dear Editor and Reviewers,

We thank the editor and reviewers for their careful evaluation of our manuscript.
We have revised the manuscript to address the concerns raised and provide a point-by-point response below.

## Response to Reviewer 1

**Reviewer comment R1.1**
[Full reviewer comment preserved here.]

**Response**
We thank the reviewer for raising this point. [Direct answer.]
To address this concern, we have [specific action]. This change appears in [section/page/line/figure].

**Revised manuscript text**
*[Paste revised manuscript text here in italics.]*
```
For LaTeX or print-oriented letters, start each reviewer on a new page. Use `\ReviewerSection{1}` from `templates/response-to-reviewers.tex`.

## Revision cover letter

Keep the cover letter shorter than the response. Identify the manuscript, thank the editor/reviewers, summarize the major revision actions and resolved themes, point to the point-by-point response, and avoid hiding unresolved concerns.

## Marked manuscript and LaTeX deliverables

- Work on a copy of the original manuscript; keep a clean version separately when required.
- Mark changed text in red. For LaTeX use `\revised{...}` from `templates/revised-manuscript-redline.tex`.
- Quote revised manuscript text in the response in italics; for LaTeX use `\RevisedExcerpt{...}`.
- Use `templates/cover-letter.tex`, `templates/response-to-reviewers.tex`, and `templates/revised-manuscript-redline.tex` as applicable.
- Preserve visible placeholders for missing IDs, names, locations, figures, dates, or author information.

## Manuscript change checklist

List manuscript actions, not polite intentions:

```text
Manuscript change checklist
- R1.1: Add validation result summary to Results and cite Fig. 5.
- R1.2: Clarify replicate definition in Methods.
- R2.1: Soften causal claim in Abstract and Discussion.
```

## Missing information / risk flags

Use specific requests:

```text
Missing information / risk flags
- R1.1: Need validation result direction and effect/performance summary before final wording.
- R1.2: Need test name, replicate unit, sample size, and correction method.
- R2.1: No line numbers supplied; using section names for now.
```
