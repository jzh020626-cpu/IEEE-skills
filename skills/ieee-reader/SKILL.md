---
name: ieee-reader
description: >-
  Build full-paper Chinese-English side-by-side, figure/table/equation-aware, source-grounded Markdown readers for IEEE and engineering journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use when equations must render correctly instead of exposing raw LaTeX and when every formula needs a stable source anchor.
---

# IEEE Paper Reader

## Workflow

- Preserve section order, equations, assumptions, figures, tables, experimental settings, and source anchors.
- Do not collapse into a summary unless the user asks for a summary.
- When equations are present, read `references/equation-handling.md`, assign stable `E...` IDs, preserve symbols exactly, and use a cropped visual fallback for low-confidence formulas.
- Before delivery, run `scripts/validate_reader_math.py paper.md --source-map source_map.json` when a source map exists; unresolved formula-traceability errors block delivery.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../ieee-shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
