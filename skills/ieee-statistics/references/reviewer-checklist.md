# Reviewer checklist

## Severity

- `P0`: wrong/undefined independent unit, leakage, ignored pairing/nesting, uncorrected comparison family, or undisclosed failure/exclusion that can change a central claim.
- `P1`: missing run counts, uncertainty, aggregation rule, metric definition, software/version, or robustness disclosure.
- `P2`: terminology, placement, or clarity issue unlikely to change the conclusion.

## Final questions

1. Is the independent unit defined?
2. Are within-run observations separated from independent runs?
3. Are seeds, scenarios, datasets, devices, or topologies counted and paired correctly?
4. Is tuning separated from final evaluation?
5. Does every central claim map to a metric and comparison?
6. Are effect size and uncertainty reported?
7. Is the multiple-comparison family explicit?
8. Are failures, timeouts, exclusions, and missing data disclosed?
9. Are remaining gaps phrased as specific `AUTHOR_INPUT_NEEDED` items?

Use neutral language: `A reviewer may challenge...`, `not assessable from the supplied material`, or `requires author confirmation`. Do not accuse authors of manipulation without direct evidence.
