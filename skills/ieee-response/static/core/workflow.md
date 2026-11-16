# Workflow and output format

## Accepted inputs

The skill may receive a pasted decision email; editor/reviewer comments; a previous response; change notes; line/page numbers; figure/table/supplement list; Chinese or English author notes; journal/article type; manuscript metadata; original text or LaTeX; and requested cover-letter/LaTeX formats.

If reviewer boundaries or comment segmentation are ambiguous, flag the ambiguity instead of inventing reviewer structure.

## Decision-dependent work

Identify the editorial decision before choosing a package-level Major/Minor Revision strategy or drafting a complete revision package. Extract it from supplied correspondence and context. If it is still unknown, ask only when that strategy depends on it. Continue local wording edits, audits of existing replies, and comment-level triage with the decision marked unknown. These bounded tasks do not establish package readiness.

## Workflow

1. Identify `draft`, `audit`, `revise`, `triage-only`, `cover-letter`, `revision-package`, `latex-template`, or `appeal-like`.
2. Parse pasted emails for metadata, decision, deadline, required files, editor constraints, reviewer boundaries, and portal instructions.
3. Identify decision type.
4. Assign editor IDs `E.1...`, then reviewer IDs `R1.1...`.
5. Classify category, severity, action, missing input, readiness, and risk.
6. Build a strategy summary and tracker.
7. Draft preserved-comment responses except in `triage-only`, `cover-letter`, or `appeal-like`.
8. Draft a concise cover letter for `cover-letter` or `revision-package`.
9. Map every claimed change to a location, figure, table, Supplementary Material, artifact repository, citation, or explicit placeholder. For every main-text edit, load `../../../ieee-shared/core/main-text-discipline.md`, classify the result or explanation, and decide whether it belongs in the main text, caption, Methods, artifact record, Supplementary Material, or response letter. Answer the reviewer fully in the letter while keeping the manuscript change to the shortest reader-facing text that preserves the central inference. Every addition triggers a deletion check across the affected paragraph.
10. When editing, use a backup/copy and red-mark changes; italicize quoted revised excerpts.
11. Start each reviewer on a new page in LaTeX/print outputs and use bundled templates when requested.
12. Flag missing input, run QA, and return `ready_to_submit`, `draft_with_placeholders`, `needs_author_input`, or `blocked`.

## Output format

Unless the user asks for another format, return:

```text
Response strategy summary
- Decision type:
- Task mode:
- Overall posture:
- Major risks:
- Parsed email metadata:
- Suggested ordering:

Comment-response tracker
| ID | Reviewer concern | Type | Severity | Proposed action | Missing author input |
|---|---|---|---|---|---|

Draft point-by-point response letter
[editor-readable English response]

Draft revision cover letter
[when requested or part of a revision package]

Marked manuscript / LaTeX files
- [paths, filled templates, or visible placeholders]

Manuscript change checklist
- [specific manuscript changes or placeholders]
- Main-text discipline audit: [result/explanation class; destination; appended, replaced, compressed, relocated, or deleted; before/after paragraph word count]

Missing information / risk flags
- [specific unresolved items or "None"]

中文核对
- [when the user writes in Chinese; otherwise omit unless useful]
```
