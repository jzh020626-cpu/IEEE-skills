# Statistical reporting checklist

For each central comparison, extract:

- endpoint and exact metric definition;
- baseline/method groups and evaluation conditions;
- independent unit: run, seed, dataset, scene, device, subject, topology, channel realization, plant instance, or another justified unit;
- nested or repeated samples: frames, packets, time points, windows, folds, trajectories, sensors, or subsystems;
- repetitions, seeds, scenario count, and pairing;
- train/validation/test split and tuning boundary;
- exclusions, failures, missing data, and warm-up/transient removal;
- aggregation: macro/micro, per-run then across runs, pooled, weighted, median, percentile, or worst case;
- test/model, assumptions, multiplicity policy, effect estimate, uncertainty, and exact p-value policy;
- software/package/version when supplied.

## Methods paragraph order

1. Software and environment.
2. Dataset/scenario split and metric definitions.
3. Independent unit, runs/seeds, and pairing.
4. Summary convention and uncertainty.
5. Test/model and assumptions.
6. Multiple-comparison strategy.
7. Exclusions, failures, and robustness checks.

## Wording

Prefer:

- `Across 20 paired channel realizations, method A reduced median latency by ... (95% CI ...).`
- `Each seed produced one independent training run; frame-level predictions were aggregated within run before comparison.`
- `The observed gain is small relative to run-to-run variability and should be interpreted cautiously.`

Avoid:

- `proved superior` from a p value;
- `n = 100000 packets` when the experiment used three network runs;
- `average accuracy` without macro/micro and dataset weighting;
- `no difference` based only on a non-significant test.
