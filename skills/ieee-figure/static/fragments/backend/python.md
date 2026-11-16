# Backend: Python (matplotlib / seaborn)

**Python-only execution rule.** When the user has selected Python, do all figure drawing, previewing, exporting, and visual QA in Python. Do not call R/ggplot2, ComplexHeatmap, patchwork, or any R graphics device to create a temporary preview, fallback export, or layout approximation. If Python or required Python plotting packages are missing, pause rendering, continue independent script or data checks, and report the missing dependency. You may still write the Python script, provide `pip`/environment install commands, or ask permission to install dependencies, but do not cross-render the figure in R.

## Python quick-start

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
from audit_panel_alignment import require_matplotlib_panel_alignment

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",     # editable text in SVG
    "pdf.fonttype": 42,         # editable TrueType text in PDF
    "font.size": 7,             # use 15-24 only for large slide-sized panels
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
})

def save_pub_py(fig, filename, dpi=600):
    require_matplotlib_panel_alignment(
        fig,
        json_out=f"{filename}.alignment.json",
        overlay_svg=f"{filename}.alignment.svg",
        tolerance_pt=1.5,
        gutter_tolerance_pt=1.5,
        strict=True,
    )
    # Keep the declared canvas width. Tight bounding-box cropping changes the
    # final physical width and is forbidden for the publication bundle.
    fig.savefig(f"{filename}.svg")
    fig.savefig(f"{filename}.pdf")
    fig.savefig(f"{filename}.tiff", dpi=dpi)
```

Use `text.usetex = True` only when LaTeX is installed and math-rich labels are required.

## Going deeper

- `references/api.md` — Python PALETTE, helper function signatures, validation rules.
- `references/common-patterns.md` — hero panels, legend-only axes, sensor/screenshot panels, asymmetric layouts.
- `references/chart-types.md` — radar, 3D sphere, fill_between, scatter patterns.
- `references/tutorials.md` — end-to-end walkthroughs for bars, trends, heatmaps.
- `references/demos.md` — bundled figures4papers Python scripts and output previews.
- `scripts/audit_panel_alignment.py` — mandatory final-layout alignment gate for multi-panel figures.
- `scripts/audit_pdf_text.py` and `scripts/audit_figure_collisions.py` — inspect the exported PDF without redrawing it.
