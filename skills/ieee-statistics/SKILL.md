---
name: ieee-statistics
description: Audit, revise, or draft statistical reporting for IEEE Transactions manuscripts and engineering experiments. Use for p values, confidence intervals, effect sizes, random seeds, simulation runs, hardware trials, packet/frame/trajectory samples, cross-validation, repeated measures, multiple comparisons, train-test leakage, benchmark aggregation, latency or reliability distributions, figure legends, reviewer statistics comments, or Chinese requests such as 统计审查、统计分析小节、p值、置信区间、随机种子、重复实验、多重比较、显著性检验、图注统计.
---

# IEEE Engineering Statistics

Make the experimental unit, uncertainty, comparison design, and claim boundary explicit. This is a reporting and audit workflow; do not claim to reanalyse raw data unless the user supplies the data and requests computation.

## Default stance

- Separate what was measured, what was independently repeated, and what inference is claimed.
- Treat frames, packets, time samples, pixels, windows, trajectories within one run, and folds from one dataset as potentially dependent.
- Report effect size, uncertainty, sample size, and metric definition, not significance alone.
- Distinguish variability across seeds, scenarios, datasets, devices, subjects, topologies, and repeated measurements.
- Use `AUTHOR_INPUT_NEEDED` instead of inventing tests, runs, seeds, exclusions, software versions, or p values.

## Workflow

1. Classify the task: audit, draft, rewrite, figure alignment, reviewer response, or data-backed analysis.
2. Extract design: baselines, factors, datasets/scenes/topologies, independent unit, repeated structure, randomization, seeds, exclusions, tuning, and missing-data handling.
3. Map each claim to its metric, aggregation rule, comparison, test/model, assumptions, multiplicity policy, effect estimate, and uncertainty.
4. Check leakage, pseudoreplication, paired versus unpaired comparison, autocorrelation, and benchmark-selection bias.
5. Read `references/statistical-reporting.md` for Methods/Results wording.
6. Read `references/common-failure-modes.md` for high-risk designs.
7. Read `references/figure-statistics.md` for legends and plots.
8. Run `references/reviewer-checklist.md` before final delivery.

## Output

```text
Statistics review scope
- material reviewed:
- independent unit:
- repetitions/seeds/scenarios:
- boundary:

Major statistical issues
- [P0/P1/P2] Issue:
  Evidence:
  Why it matters:
  Fix:

Ready-to-paste revision
[Methods, Results, or legend text]

AUTHOR_INPUT_NEEDED
- [specific factual question]

Reviewer-risk note
- [remaining challenge]
```

## Red lines

- Do not invent sample sizes, seeds, confidence intervals, test statistics, degrees of freedom, software versions, or correction methods.
- Do not count correlated packet/frame/time-point samples as independent experiments without a justified model.
- Do not infer that two methods differ because one is significant and the other is not; test the paired difference or interaction.
- Do not use the final test set for model selection without flagging leakage.
- Do not equate statistical significance with engineering importance, robustness, safety, or deployment value.
