# Figure contract before plotting

A publication-quality scientific figure is a visual argument, not an isolated pretty plot. Every figure starts from a claim, an evidence hierarchy, and a review-risk check before code or aesthetics. Before generating or editing code, establish the contract below.

## Backend selection follows task scope

Read-only inspection and backend-neutral validation do not require a plotting backend. A vector-only SVG schematic follows `references/vector-schematic-workflow.md` (relative to the skill root) without the plotting gate. For quantitative rendering, resolve explicit choice, language-specific input, an established task choice, then `scripts/ieee_figure_backend.py get`. Ask once only if still unresolved, and pause dependent rendering while continuing independent inspection. Save explicit choices and preserve backend exclusivity for actual plotting.

## The selected backend is exclusive

Once Python or R is selected, every plotting script, preview image, SVG/PDF/TIFF/PNG export, QA render, and visual workaround must be produced by that same backend. Do not use Python to draw a preview for an R figure, and do not use R to draw a preview for a Python figure, even if the selected runtime or packages are missing locally. The non-selected language may only be used for non-visual file inspection or data conversion when it does not open a graphics device, import plotting libraries, create image/vector files, or change the final visual appearance.

The backend-neutral `audit_panel_alignment.py`, `audit_pdf_text.py`, and
`audit_figure_collisions.py` may inspect a layout manifest or final PDF from
either backend. They do not redraw scientific content. Alignment/collision
overlays are QA-only and never replace the selected-backend submission asset.

## Missing runtime/package rule

After the backend is selected, check the selected runtime early (`Rscript`/R for R; Python and required plotting packages for Python). If the selected runtime or required packages are unavailable, stop before rendering and report the exact blocker. You may provide a selected-backend script and installation commands, or ask permission to install dependencies, but you must not fall back to the other language to make a substitute figure.

## The five-point contract

1. **Core conclusion**: write the one-sentence claim the figure must defend.
2. **Evidence chain**: map each planned panel to one distinct inferential role, and drop, merge, or demote panels that only redraw another panel's evidence.
3. **Archetype**: classify the figure as `quantitative grid`, `schematic-led system figure`, `experiment snapshot + quant`, or `asymmetric mixed-modality figure`.
4. **Backend**: quantitative plots use the selected Python or R track exclusively. Read-only audits and vector-only SVG schematics follow their explicit exceptions above. Do not cross-render quantitative content with the other language.
5. **Journal/export contract**: set final dimensions, editable text, figure/table data, statistics, image-integrity notes, export formats, render-time multi-panel alignment, and final PDF collision QA before styling.

The highest-priority rule is: **the chart serves the scientific logic**. Aesthetic polish, template matching, and complex layout are subordinate to making the core conclusion clear, defensible, and reviewable.

For the full method to convert a request into core conclusion, evidence hierarchy, panel map, and review-risk checks, open `references/figure-contract.md`.
For a multi-panel figure or figure sequence, also open
`references/multipanel-evidence-architecture.md`.
