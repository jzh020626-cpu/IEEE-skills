# Common engineering statistical failure modes

## P0: central inference may be invalid

### Pseudoreplication

Frames, packets, pixels, time samples, windows, or observations inside one run are treated as independent repetitions. Aggregate at the justified unit or use a hierarchical/time-series model.

### Test-set or benchmark leakage

Hyperparameters, thresholds, prompts, stopping decisions, or model variants are selected on the reported test set. Separate selection and final evaluation, or label the result exploratory.

### Pairing ignored

Methods are evaluated on the same seeds, scenes, datasets, topologies, or disturbances but compared as independent groups. Use paired differences or an appropriate repeated/mixed model.

### Multiple comparisons without a family

Many baselines, datasets, metrics, time points, or ablations are tested with selective reporting. Define the comparison family and correction or identify prespecified primary comparisons.

### Difference in significance used as significance of difference

One method passes a threshold and another does not, but their effects are never directly compared. Test the contrast or interaction.

## P1: important reviewer risk

### Too few runs or seeds

Strong claims rest on unstable stochastic results. Report run-level values and uncertainty; bound the claim.

### Aggregation hides heterogeneity

A grand mean mixes datasets, scenarios, devices, loads, or users. Report per-condition results and state macro/micro or weighting rules.

### Time dependence ignored

Latency, queue, trajectory, or sensor samples are autocorrelated. Do not use sample count as independent `n`; model or aggregate by run/window with a justified rule.

### Failures and timeouts omitted

Only completed trials enter the metric. Report failure rate, timeout policy, and whether failed runs receive a defined penalty.

### Outlier removal is post hoc

State the rule, timing, number removed, and sensitivity to inclusion.

## P2: reporting clarity

- Error bars or confidence bands are undefined.
- Seeds or trial counts vary across panels without panel-specific disclosure.
- `ns` replaces the estimate and uncertainty.
- Units, percentile definitions, or metric direction are missing.
- Software and hardware versions are absent.
