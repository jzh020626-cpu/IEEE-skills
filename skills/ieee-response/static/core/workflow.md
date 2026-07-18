# Workflow and output format

## Accepted inputs

The skill may receive a pasted decision email; editor/reviewer comments; a previous response; change notes; line/page numbers; figure/table/supplement list; Chinese or English author notes; journal/article type; manuscript metadata; original text or LaTeX; and requested cover-letter/LaTeX formats.

If reviewer boundaries or comment segmentation are ambiguous, flag the ambiguity instead of inventing reviewer structure.

## Workflow

1. Identify `draft`, `audit`, `revise`, `triage-only`, `cover-letter`, `revision-package`, `latex-template`, or `appeal-like`.
2. Parse pasted emails for metadata, decision, deadline, required files, editor constraints, reviewer boundaries, and portal instructions.
3. Identify decision type.
4. Assign editor IDs `E.1...`, then reviewer IDs `R1.1...`.
5. Classify category, severity, action, missing input, readiness, and risk.
6. Build a strategy summary and tracker.
7. Draft preserved-comment responses except in `triage-only`, `cover-letter`, or `appeal-like`.
8. Draft a concise cover letter for `cover-letter` or `revision-package`.
9. Map every claimed change to a location, figure, table, supplement, citation, or explicit placeholder.
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

Missing information / risk flags
- [specific unresolved items or "None"]

中文核对
- [when the user writes in Chinese; otherwise omit unless useful]
```
