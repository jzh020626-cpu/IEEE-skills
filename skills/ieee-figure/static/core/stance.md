# Default operating stance

The figure skill supports Python/matplotlib and R plotting for IEEE Transactions manuscripts in robotics, automation, control, communications, and industrial informatics.

## Color policy

Prefer stable method/condition colors across all panels. Use neutral grays for context, one signal family for the proposed method, one comparison family for baselines, and one restrained accent for failures, violations, or highlighted constraints. Do not use saturated rainbow palettes for metric comparison.

## Stance

- Start by classifying the requested figure into one of four archetypes: `quantitative grid`, `schematic-led system figure`, `experiment snapshot + quant`, or `asymmetric mixed-modality figure`.
- Prefer one hero panel plus subordinate evidence panels over equal-sized dashboard grids.
- If the user asks for a single chart, still identify its manuscript role: problem definition, method, theory, validation, comparison, robustness, ablation, latency/throughput, stability, or deployment evidence.
- Keep plot backgrounds white; use dark backgrounds only inside sensor images, simulator screenshots, camera frames, or occupancy/map panels where the source image requires it.
- Prefer direct labels over legends when method identities are spatially fixed or the legend would force unnecessary eye travel.
- Keep one restrained palette per figure: usually one neutral family, one signal family, and one accent family.
- Treat statistics, trial count, seed count, error-bar definitions, source-data traceability, and engineering constraints as part of the figure contract, not optional caption cleanup.
- When the user asks for broad IEEE Transactions style, read `references/ieee-2026-observations.md` before choosing layout.
- Bundled legacy demo assets are internal pattern references only; never copy their domain labels or make them recommended IEEE examples.

## User-facing privacy rule

Do not disclose private local paths, private filenames, chat-attachment names, internal reference filenames, template identifiers, or the provenance of private working materials in user-facing replies, generated code comments, figure legends, reports, or manuscript text. Use generic descriptions such as "the provided template collection", "a private working draft", or "the internal figure contract". Only reveal an exact path or source file when the user explicitly asks for that audit trail.

## When to load this skill

- Python or R figures for papers, slides, or reports targeting IEEE Transactions/Letters in robotics, automation, control, communications, industrial informatics, or networked systems.
- Requests involving grouped bars, trend lines, trajectories, timing plots, heatmaps, radar plots, multi-panel grids, system diagrams, or PDF/SVG/EPS/TIFF output.
- Any mention of "IEEE Transactions style", "publication figure", "paper figure", "SCI figure", "R plotting template", "robotics figure", "control figure", "communication figure", or "high-quality engineering plot".
- Requests to improve a figure's logic, aesthetics, panel layout, caption, export quality, or journal readiness.

## When NOT to load

- Plotly, Altair, Bokeh, or other interactive/web-first plotting.
- EDA-only plots without a publication target.
- Primary workflow is GIS, CAD, or non-scientific illustration tooling.
- Illustrator / Figma-first layout.
