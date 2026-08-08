# IEEE Figure QA Contract

## Rendered panel-by-panel audit

Do not approve a figure from a whole-page glance. Inspect each panel at final physical size and record:

| Panel | Unique claim | Center/summary | Spread/interval | Independent unit | Labels/legend | Collision check | Pass |
|---|---|---|---|---|---|---|---|

If removing a panel leaves the argument complete, merge or remove it. Comparable seed/run/scenario aggregates must show the same variability definition or document a justified exemption. Recompute label clearance from the upper uncertainty extent after adding error bars.

## PDF glyph and numerical-safety gates

- The 5 pt conservative floor applies to every rendered glyph, including math superscripts and subscripts, not only the parent source `fontsize`; verify the current target journal if it differs.
- Run `python scripts/audit_pdf_text.py figure.pdf --min-pt 5`. A non-auditable result requires another verified method and final-size visual inspection.
- Reject duplicate or direction-changing interpolation grids. When a grid is decreasing, reverse coordinates and values together; use `scripts/figure_safety.py::interp_monotone` for Python figures.
- Derive annotations from actual data and uncertainty bounds. Avoid fixed label positions and opaque masks that hide curves.
- Check hierarchy, grayscale, and color-vision robustness after rendering; numerical color distance alone does not prove the intended evidence is visually salient.

Use this before final delivery, before a revision package, and whenever the figure contains statistical claims, hardware/simulation screenshots, trajectory plots, latency/throughput curves, stability evidence, or baseline comparisons.

Journal rules change, so verify the latest target journal author guide for final submission. The values below are conservative defaults for IEEE Transactions work.

## Current official references to verify

- IEEE Author Center graphics file formatting: `https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/`
- IEEE Article Templates: `https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/`
- IEEE supplementary materials: `https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/`
- T-ASE final manuscript checklist: `https://www.ieee-ras.org/publications/t-ase/information-for-authors-t-ase/t-ase-author-checklist-for-accepted-papers-final-manuscripts/`

## Pre-submission checklist

| Check | Pass condition |
|---|---|
| Core conclusion | One-sentence claim exists and every panel maps to it |
| Archetype | Figure has a declared engineering archetype and panel hierarchy |
| Backend exclusivity | The selected backend produced all plotting, previews, exports, and visual QA renders |
| Final size | Single-column or double-column IEEE width is chosen before styling |
| Text size | Body/tick/legend text is readable at final size |
| Panel labels | Subfigures use consistent `(a)`, `(b)`, `(c)` or equivalent IEEE-compatible labels |
| Editable text | SVG/PDF text remains editable; no outlined text unless unavoidable |
| Font | Arial/Helvetica/sans-serif fallback is used consistently |
| Color | No rainbow color maps; red/green is not the only encoding; grayscale print remains interpretable |
| Legend strategy | Shared or direct labels where possible; no repeated redundant legends |
| Statistics | Trial/seed count, center, spread, test, correction, and exact comparison are documented |
| Figure/table data | Quantitative panels can be traced to CSV/TSV/XLSX/log/script output |
| Engineering context | Platform/simulator/network/controller settings are clear where the figure depends on them |
| Export bundle | Script, figure/table data, SVG/PDF/EPS or TIFF/PNG preview, and QA notes are delivered when requested |

## Engineering legend minimum

For each quantitative panel, capture:

```text
trial/seed definition:
number of runs:
center statistic:
spread/interval:
test or confidence method:
baseline definition:
metric definition:
figure/table data file:
```

For robotics/control/communications figures, also capture:

```text
platform or simulator:
controller/network/channel setting:
constraint or safety threshold:
sampling rate / time step:
latency / throughput / packet-loss model:
```

## Export checks

IEEE accepts PS, EPS, PDF, PNG, or TIFF graphics. Use vector output for plots/diagrams and high-resolution raster only when the source is raster.

### Python

```python
import matplotlib as mpl
mpl.rcParams["svg.fonttype"] = "none"
mpl.rcParams["pdf.fonttype"] = 42
fig.savefig("figure.svg", bbox_inches="tight")
fig.savefig("figure.pdf", bbox_inches="tight")
fig.savefig("figure.tiff", dpi=600, bbox_inches="tight")
```

### R

```r
svglite::svglite("figure.svg", width = width_mm / 25.4, height = height_mm / 25.4)
print(plot)
dev.off()

grDevices::cairo_pdf("figure.pdf", width = width_mm / 25.4, height = height_mm / 25.4, family = "Arial")
print(plot)
dev.off()

ragg::agg_tiff("figure.tiff", width = width_mm / 25.4, height = height_mm / 25.4, units = "in", res = 600)
print(plot)
dev.off()
```

Open the SVG/PDF after export and verify that text can be selected, labels do not overlap, and the figure still reads at final printed size.
