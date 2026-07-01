# Search Strategy

## Turn claims into searchable concepts

Break each sentence into:

- `phenomenon`: what is being claimed
- `entity`: robot, controller, network, protocol, sensor, actuator, platform, dataset, benchmark, or industrial system
- `relationship`: increases, decreases, predicts, stabilizes, reduces, improves, detects, estimates, or bounds
- `context`: task scenario, platform, simulator, channel model, operating regime, device, method, or dataset
- `boundary`: "under packet loss", "on AGV transport tasks", "with bounded delay", "in industrial edge settings", etc.

Create search queries at three levels:

1. `precise`: entity + relationship + outcome + context
2. `synonym`: alternate names and abbreviations
3. `broad`: field context if no direct paper is found

For Chinese claims, translate the scientific concepts, not the sentence literally. Keep acronyms and
standard nomenclature unchanged.

## Support grading

Use the smallest support grade that is defensible:

| Grade | Meaning | Good use |
|---|---|---|
| strong support | Directly tests the same core relationship in a similar context | Experimental, mechanistic, or quantitative manuscript claims |
| partial support | Supports one component or a narrower setting | Carefully qualified claims |
| background support | Establishes field context or prior observation | Introduction/background sentences |
| contradictory/limiting | Conflicts with or narrows the claim | Discussion, limitations, or avoid citing as support |
| metadata-only candidate | Metadata suggests relevance; abstract/full text not checked | Screening only |

## Evidence note template

```text
Claim: [original claim]
Paper: [first author/year/title/journal/DOI]
Support grade: [grade]
Evidence basis: [title/abstract/publisher page/full text]
Reasoning: [why the result supports or does not support the exact claim]
Citation wording: [how to phrase the manuscript sentence if using this citation]
```

## Common failure modes

- The paper is related to the same task family but tests a different system model or mechanism.
- The paper supports an association, but the manuscript sentence claims causality.
- The evidence is in a different robot/platform, network model, operating regime, or deployment setting.
- A review is used as primary evidence when original research exists.
- The claim is too broad for a single citation.
- The searched journal title contains "IEEE Transactions" but is not a IEEE Xplore journal.

## Better search moves

- Add the method or model when results are broad: `multi-robot`, `networked control`,
  `model predictive control`, `packet loss`, `industrial informatics`, `edge intelligence`.
- Add context terms when there are many irrelevant hits: task, platform, simulator, channel model,
  delay regime, safety constraint, metric, or deployment setting.
- Search the opposite direction if the claim might be overconfident: `improves` vs `degrades`,
  `stable` vs `unstable`, `robust` vs `sensitive`, `low latency` vs `delay`.
- Use recent limits for fast-moving areas, but remove them if no direct IEEE Transactions/IEEE Transactions-series paper appears.
