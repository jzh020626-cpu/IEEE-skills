# IEEE Figure QA Contract

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
