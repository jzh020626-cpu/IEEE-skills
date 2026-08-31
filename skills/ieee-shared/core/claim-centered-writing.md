# Evidence-Calibrated Press-Release Principle

Use this module for author-facing argument design, drafting, restructuring,
polishing, result presentation, captions, submission audits, and reviewer
responses. Do not use it to soften an independent reviewer assessment, hide
evidence during paper reading, or bias a statistical audit.

## Governing stance

A paper should have the focus of an evidence-calibrated academic press release,
not read like a project report, experiment log, or self-audit. Identify the
strongest publishable contribution that the evidence supports and make every
main-text section help the reader understand and trust it. That contribution may
be a theorem or guarantee, a new mechanism, a system capability, a complexity or
resource improvement, an engineering trade-off, or a clarified failure boundary;
it need not be a leaderboard win.

Remove unsupported self-attack; never remove decision-relevant evidence.
Truthfulness, protocol and preregistration commitments, editor/reviewer
questions, safety, reproducibility, and venue rules override rhetorical
advantage.

## Build the story around the strongest supported claim

1. Write one central claim with the condition in which it holds and the evidence
   that supports it.
2. Organize the paper as problem -> gap -> distinctive solution -> evidence ->
   significance. Do not narrate attempts, failed branches, internal version
   history, debugging, or how the project evolved.
3. Name the evaluation or proof obligation the work actually satisfies. Narrow
   the claim, assumptions, task, metric, comparator, scenario, or application
   scope when needed; do not force every contribution into a performance contest.
4. State the advantage explicitly. Give the metric, comparator, condition,
   uncertainty, and practical meaning when available.
5. Let every main-text experiment perform one job: establish the main effect,
   test the mechanism, demonstrate target-scenario value, quantify a meaningful
   trade-off, or rule out the strongest alternative explanation.
6. Restructure the title, Abstract, Introduction, contributions, Results,
   Discussion, figures, and Conclusion when the strongest evidence supports a
   different story from the original plan.

This does not permit post-hoc relabeling. If the winning evaluation frame was
chosen after observing outcomes, label it exploratory and retain protocol-
required original analyses in the appropriate record.

## Separate the main manuscript from the complete evidence record

The main manuscript is the argument. The supplement and artifact package are the
complete auditable record.

Keep in the main manuscript:

- the evidence that directly supports each headline claim;
- relevant uncertainty, trade-offs, and failure boundaries that change how a
  reasonable reader interprets the contribution;
- protocol-required outcomes and information requested by the venue, editor, or
  reviewer; and
- safety, applicability, or reproducibility facts needed to prevent a misleading
  claim.

Move to the supplement or artifact record when scientifically appropriate:

- complete scenario tables, audit trails, hashes, evaluator counts, projection
  diagnostics, and implementation provenance;
- unsuccessful development branches and stopped validation attempts that do not
  alter the bounded central claim;
- non-leading ablations retained for transparency but not needed to establish the
  main contribution; and
- detailed negative outcomes whose consequence is already stated once in a
  proportional Limitations paragraph.

Do not hide essential support in the supplement, and do not omit evidence in a
way that cherry-picks datasets, metrics, seeds, baselines, time windows, or
examples.

## Handle unfavorable or mixed evidence

Use this order:

1. Decide whether the result changes the central conclusion, safety,
   applicability, or claimed robustness. If yes, disclose it clearly.
2. If it is relevant only to a broader claim, narrow the claim instead of
   defending the broader claim.
3. Explain a supported objective difference, constraint, scenario boundary, or
   trade-off without relabeling a loss as a win.
4. Give a non-leading result one proportional location. Do not repeat it in the
   Abstract, contributions, Results, Discussion, and Conclusion.
5. If it does not strengthen, delimit, or test the central claim, move it out of
   the main narrative while preserving the auditable record where required.

Describe mixed evidence neutrally and precisely. Prefer “accuracy decreased
while latency improved by 34%” or “the interval crossed zero” over
“unfortunately,” “only,” “merely,” “failed badly,” or a broad judgment of
inadequacy. Factual comparisons such as “lower than” remain appropriate when
they are necessary and supported.

## Section contracts

- **Title:** name the system, capability, and consequence the evidence supports.
- **Abstract:** establish the problem, gap, distinctive solution, strongest
  decisive evidence, and significance. This may be a quantitative result or a
  formal result with its assumptions and guarantee. Do not headline a non-leading ablation,
  stopped attempt, missing validation, or project-history caveat.
- **Introduction:** position the important unresolved gap and the paper's move.
  Contributions state advances and evidence, not audit activities.
- **Methods:** define assumptions and operational scope once. Avoid immediately
  retracting every theorem, definition, or design choice with repeated caveats.
- **Results:** open each subsection with the claim it establishes, then give the
  evidence. Keep process narration, budget accounting, and traceability logs out
  of the main result unless they are themselves the contribution.
- **Discussion and Limitations:** interpret the advance, address the strongest
  alternative explanation, and state each material boundary once. Do not elevate
  a local non-leading result into a verdict on the whole method.
- **Conclusion:** reinforce what was solved, proposed, demonstrated, and why it
  matters. Do not introduce new limitations, missing work, or self-negation.
- **Reviewer response:** answer the question directly. Narrative focus never
  authorizes evading a requested result or a conclusion-changing weakness.

## Hard red lines

- Do not fabricate, relabel, selectively aggregate, or visually manipulate
  evidence to create a win.
- Do not switch metrics, datasets, baselines, hypotheses, or stopping rules after
  observing results without explicit disclosure and suitable statistical care.
- Do not suppress negative results, anomalies, exclusions, or failure cases that
  affect the claim boundary.
- Do not convert statistical non-significance into equivalence, an observed mean
  difference into superiority, simulation into deployment, or correlation into
  causation.
- Do not weaken an audit finding or reviewer concern merely because it is
  rhetorically inconvenient.

## Final attack-surface check

- Is the strongest supported advantage explicit in the Abstract, contributions,
  Results, and Conclusion?
- Does every main-text paragraph help establish, explain, test, or proportionally
  delimit that advantage?
- Does any paragraph read like a work report, experiment diary, provenance log,
  or pre-emptive reviewer response?
- Has a non-leading metric or ablation become a headline contest?
- Is the same limitation repeated across several sections?
- Does the Conclusion end on the demonstrated value rather than on missing work?
- Would moving a detail to the supplement preserve integrity while making the
  main argument clearer?

## Provenance

Adapted from Adkid-Zephyr's *Anti-Defensive Writing* skill, commit
`0212d11541f6df5ce8a6f22ae82bc651452abd24`, under the MIT License. The IEEE
adaptation preserves the press-release principle and adds research-integrity,
statistical, reporting, and reviewer-response boundaries. See
`../licenses/anti-defensive-writing-MIT.txt`.
