# Legacy Demo Index

Use this file only when a user explicitly asks to inspect or reuse bundled legacy plotting demos. These assets are retained for compatibility with the original repository layout, but they are not IEEE-recommended examples and their domain labels must not be copied into new manuscripts.

## How to use legacy demos safely

1. Select a generic chart family, not a domain project name.
2. Read only the nearest plotting script for layout, palette, axis, legend, and export mechanics.
3. Replace all demo data, labels, captions, and terminology with the user's robotics/control/communications content.
4. Preserve IEEE export rules from `qa-contract.md`.
5. Do not reveal local repository paths or internal asset filenames in user-facing prose unless the user asks for an audit trail.

## Generic routing

| Need | Look for this pattern |
|---|---|
| Method comparison | grouped bars, dot plots, or line plots with shared baseline ordering |
| Ablation | compact grouped bars or small multiples with one removed component per panel |
| Latency/throughput trend | line plots with direct labels and confidence bands |
| Robustness or sensitivity | sweep curves, heatmaps, or interval plots |
| Trajectory or state evolution | time-series panels, path overlays, or phase plots |
| System overview | schematic-led composite with 2-4 supporting quantitative panels |

## Relationship to older demo assets

The older demo assets remain in `assets/` as compatibility material. Treat them as internal plotting mechanics only. For IEEE Transactions work, the governing rules are:

- `qa-contract.md` for export and readability.
- `figure-contract.md` for evidence hierarchy.
- `figure-legend-conventions.md` for IEEE captions.
- `ieee-2026-observations.md` for robotics/control/communications figure archetypes.
