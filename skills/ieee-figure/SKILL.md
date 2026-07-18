---
name: ieee-figure
description: >-
  Submission-grade IEEE Transactions figure workflow for Python or R. Use to create, revise, audit, or polish manuscript figures, multi-panel scientific plots, IEEE double-column-ready SVG/PDF/EPS/TIFF outputs, and robotics/control/communications experiment visualizations.
---

# IEEE Figure Router

Use `manifest.yaml` to select one exclusive plotting backend and load only the relevant fragments.

## Routing protocol

1. Read `manifest.yaml` and all `always_load` paths.
2. Resolve the backend in this order:
   - the user's explicit Python/R choice;
   - a clearly language-specific input script or workflow;
   - a saved preference from `scripts/ieee_figure_backend.py get`;
   - otherwise ask exactly one concise question: “Python or R?”
3. Once resolved, keep the backend exclusive for drawing, previewing, exporting, and visual QA. Save an explicit user choice with `scripts/ieee_figure_backend.py set`.
4. Define the figure contract before plotting: claim, target journal/column width, panel map, variables, units, baselines, independent unit, statistics, uncertainty, source data, and export formats.
5. Run the data-integrity gate: preserve values and labels, do not fabricate data, distinguish demo data, and document transformations/aggregation.
6. Select an existing template only when its evidence structure matches; read `references/template-catalog.md` and `references/asset-adaptation.md`.
7. Build and export. Prefer vector PDF/EPS/SVG for plots and diagrams; use PNG/TIFF for raster content when appropriate.
8. Run `scripts/validate_figure.py` and the QA contract, inspect final-size output, fix blocking findings, and revalidate.

## IEEE gates

- Default target widths are 88.9 mm for one column and 182 mm for two columns unless the named journal says otherwise.
- Use readable labels at final size, self-contained captions, visible units, consistent panel labels, and black-and-white robustness.
- General IEEE raster guidance is at least 300 dpi for color/grayscale and at least 600 dpi for black-and-white line art; verify exact journal requirements.
- For robotics/control/communications, check trajectories, timing, stability, convergence, latency, throughput, reliability, ablation, failure cases, and baseline comparisons as applicable.
- Do not invent samples, error bars, confidence intervals, p values, hardware traces, or metric values.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
