# Figure and table statistics

Each quantitative panel or table should state:

- what points, bars, lines, boxes, bands, or CDFs represent;
- the independent unit and panel-specific `n`;
- repetitions/seeds/scenarios and whether comparisons are paired;
- aggregation and error/interval definition;
- test/model and multiplicity correction when inferential annotations appear;
- failure/timeout/exclusion handling.

## Plot-specific checks

- **Learning curves/time series:** show across-run uncertainty; do not treat time steps as independent.
- **CDF/CCDF:** define the pooled unit, observation window, warm-up removal, and percentile estimator.
- **Box/violin plots:** define box/whisker rules and whether points are runs or within-run samples.
- **Trajectory plots:** distinguish illustrative trajectories from inferential repetitions.
- **Benchmark bars/tables:** state macro/micro aggregation, dataset weighting, and paired comparison unit.
- **Heatmaps:** state normalization, selected rows/columns, clustering, and missing-value handling.
- **Ablations:** define whether variants share seeds/settings and avoid interpreting isolated significance thresholds.

Prefer exact estimates and intervals. Star notation may supplement, but should not replace, the reported comparison.
