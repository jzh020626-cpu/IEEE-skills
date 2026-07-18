---
name: ieee-reader
description: >-
  Build full-paper Chinese-English side-by-side, figure/table-aware, source-grounded Markdown readers for IEEE and engineering journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text.
---

# IEEE Paper Reader

## Workflow

- Preserve section order, equations, assumptions, figures, tables, experimental settings, and source anchors.
- Do not collapse into a summary unless the user asks for a summary.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../ieee-shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
