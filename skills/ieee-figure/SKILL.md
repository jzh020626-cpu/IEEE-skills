---
name: ieee-figure
description: >-
  Submission-grade IEEE Transactions figure workflow for Python or R. Use to create, revise, audit, or polish manuscript figures, multi-panel scientific plots, graphical abstracts, IEEE double-column-ready SVG/PDF/EPS/TIFF outputs, and robotics/control/communications experiment visualizations, including rendered alignment and collision QA.
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
   For a multi-panel figure or manuscript-level figure sequence, load
   `references/multipanel-evidence-architecture.md` and give every panel a
   distinct inferential role.
5. Run the data-integrity gate: preserve values and labels, do not fabricate data, distinguish demo data, and document transformations/aggregation.
   For author-facing panel selection, emphasis, or captions, also apply
   `../ieee-shared/core/claim-centered-writing.md`; give the strongest supported
   evidence the visual hierarchy, move non-leading audit displays to the
   supplement when appropriate, and never hide uncertainty, relevant baselines,
   exclusions, or conclusion-changing failures.
6. Select an existing template only when its evidence structure matches; read `references/template-catalog.md` and `references/asset-adaptation.md`.
7. Build and export. Prefer vector PDF/EPS/SVG for plots and diagrams; use PNG/TIFF for raster content when appropriate.
8. For every multi-panel layout, call the render-time alignment gate after the
   final layout-affecting change and before export. The default `1.5 pt` QA
   tolerance is an internal check, not an IEEE rule; use only narrow, reasoned
   panel exemptions. Use `scripts/audit_panel_alignment.py` directly for JSON
   manifests, or its Matplotlib/R helper from the selected backend.
9. Run `scripts/validate_figure.py` and the QA contract. For PDF output also run
   `scripts/audit_pdf_text.py FIGURE.pdf --min-pt 5` and
   `scripts/audit_figure_collisions.py FIGURE.pdf --expected-width-mm WIDTH --json-out FIGURE.collisions.json`,
   where `WIDTH` is the verified `88.9`, `182`, or venue-specific final width.
   Text overlap, text–stroke collision, or clipping blocks delivery. A
   non-auditable PDF requires documented final-size visual review, not a pass.
10. Inspect every panel at final physical size, record its unique claim, uncertainty definition, independent unit, label/legend status, alignment result, and collision result; then inspect the assembled figure and revalidate.

## IEEE gates

- Default target widths are 88.9 mm for one column and 182 mm for two columns unless the named journal says otherwise.
- Do not export the publication bundle with `bbox_inches="tight"`; it changes
  final physical width after layout QA. Fix margins on the declared canvas and
  verify the final PDF media box.
- Use readable labels at final size, self-contained captions, visible units, consistent panel labels, and black-and-white robustness.
- General IEEE raster guidance is at least 300 dpi for color/grayscale and at least 600 dpi for black-and-white line art; verify exact journal requirements.
- For robotics/control/communications, check trajectories, timing, stability, convergence, latency, throughput, reliability, ablation, failure cases, and baseline comparisons as applicable.
- Do not invent samples, error bars, confidence intervals, p values, hardware traces, or metric values.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
- For Python transformations, reject duplicate/non-monotone interpolation grids and derive annotation clearance from the data plus uncertainty extent; `scripts/figure_safety.py` provides safe helpers.
- When the user explicitly requests a graphical abstract, load
  `references/ai-graphical-abstract-workflow.md`; verify the current target
  journal policy and keep generated technical text, symbols, and evidence
  untrusted until reconstructed and checked.
