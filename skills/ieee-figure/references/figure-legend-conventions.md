# IEEE Figure and Table Caption Conventions

Use this file when writing or auditing figure/table captions for IEEE Transactions manuscripts.

## Figure caption structure

1. Start with `Fig. N.` followed by a concise descriptive sentence.
2. Define every subpanel label in order: `(a)`, `(b)`, `(c)`, etc.
3. State variables, units, metrics, baselines, trial/seed counts, and error-bar definitions needed to read the figure without returning to the Methods section.
4. Keep captions compact. Do not turn the caption into a Results paragraph or a second Discussion.
5. Put permissions or adaptation statements only when a panel reuses or adapts external material.

## Tense and wording

- Use present tense for visual facts: "The curve shows...", "The shaded region denotes...".
- Use past tense only for generation procedure when needed: "Experiments were run with...".
- Avoid hype words such as "remarkable", "dramatic", or "groundbreaking".
- Prefer engineering nouns: `latency`, `completion time`, `tracking error`, `packet loss`, `force imbalance`, `stability margin`, `throughput`, `success rate`.

## Self-containment rule

The caption must define:

- color and marker meanings
- line style meanings
- units and normalization
- baseline names
- trial/seed count or confidence interval definition
- safety, stability, or communication thresholds if drawn
- whether values are simulation, hardware, dataset, or analytical results

## Table captions

Start with `TABLE N` in the IEEE style used by the template, followed by a short title. Define abbreviations, units, and bold/underline conventions in the table note or caption. Tables comparing methods should identify whether higher/lower is better for each metric.

## Attribution and permissions

For adapted or reused material, include a neutral permission line such as:

```text
Adapted from [n] with permission.
```

Never cite a source in the caption if it is not present in the IEEE reference list.

## Chinese caption notes

- Use `Fig. N.` and explain `(a)`, `(b)`, `(c)` in order.
- Make the caption self-contained: colors, line styles, units, baselines, error bars, trial counts, and thresholds must be clear.
- IEEE captions do not use a pipe-style figure title or mandatory source-data boilerplate.
- Table captions should define abbreviations, units, bold/underline meaning, and whether each metric is better when higher or lower.
