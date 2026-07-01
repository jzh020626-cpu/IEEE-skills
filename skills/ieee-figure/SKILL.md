---
name: ieee-figure
description: >-
  Submission-grade IEEE Transactions figure workflow for Python or R. Use to create, revise, audit, or polish manuscript figures, multi-panel scientific plots, IEEE double-column-ready SVG/PDF/EPS/TIFF outputs, and robotics/control/communications experiment visualizations.
---

# IEEE Figure Making Router

## Workflow

- Before plotting, define the claim, target column width, required panels, variables, baselines, statistics, and export format.
- Prioritize vector output, readable labels at IEEE column size, caption self-sufficiency, black-and-white robustness, and no decorative clutter.
- For robotics/control/communications, check trajectories, timing, stability, latency, throughput, ablation, and baseline comparison plots.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
