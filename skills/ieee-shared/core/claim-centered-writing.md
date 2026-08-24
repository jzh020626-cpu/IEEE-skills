# Evidence-Calibrated Anti-Defensive Writing

Use this module for author-facing argument design, drafting, restructuring,
polishing, result presentation, captions, submission audits, and reviewer
responses. Do not use it to soften an independent reviewer assessment, hide
evidence during paper reading, or bias a statistical audit.

## Governing distinction

Remove unsupported self-attack; never remove decision-relevant evidence.

The paper should make its strongest *supported* contribution easy to see. This
does not authorize selective reporting, post-hoc metric switching, misleading
comparison scopes, suppressed failure cases, or evasive reviewer responses.
Truthfulness, protocol and preregistration commitments, editor/reviewer
questions, safety, reproducibility, and the target venue's rules override
rhetorical advantage.

## Author-facing workflow

1. Write the central claim in one sentence, including the condition or scope in
   which it holds.
2. Map each material claim to direct evidence. Separate core evidence,
   mechanism evidence, boundary/failure evidence, and contextual results.
3. Organize the argument as problem -> gap -> method -> evidence -> significance,
   not as a chronology of attempts.
4. Give every main-text experiment a declared argumentative role: establish the
   main effect, test the mechanism, demonstrate target-scenario value, quantify
   a trade-off, probe robustness/failure boundaries, or rule out an alternative
   explanation.
5. State the strongest supported advantage explicitly. Name its metric,
   comparator, scenario, uncertainty, and practical meaning when available.
6. Narrow or restructure a claim when the evidence does not support the original
   story. Never redefine the evaluation after seeing results without labeling
   the analysis exploratory and preserving the original outcome where required.

## Handling unfavorable or mixed evidence

An unfavorable result is mandatory in the manuscript or response when it:

- materially changes the central conclusion, applicability, safety, or claimed
  robustness;
- reveals a relevant failure mode, null result, uncertainty, or trade-off;
- is required by the experimental plan, reporting standard, venue, editor, or
  reviewer question; or
- is needed to prevent a comparison, figure, abstract, or conclusion from being
  misleading.

When the result is not decision-relevant, it may be moved, condensed, or omitted
from the main narrative, provided the choice does not cherry-pick datasets,
metrics, seeds, baselines, time windows, or examples. Keep essential support in
the main paper; supplementary material must not carry an unstated central claim.

Describe mixed evidence neutrally and precisely. Prefer “the difference was
2.1% and the interval crossed zero” or “accuracy decreased while latency improved
by 34%” over “unfortunately,” “only,” “merely,” “failed badly,” or a broad claim
of inadequacy. Do not ban factual phrases such as “lower than” when the comparison
is relevant and supported.

## Section-specific use

- **Title, Abstract, Introduction:** establish the important problem, exact gap,
  distinctive approach, strongest result, and significance early. Do not front-
  load implementation chronology or speculative apologies.
- **Results and figures:** use complete comparison sets and honest axes. Make the
  intended claim visually clear without hiding uncertainty, non-leading
  baselines, or relevant failure cases.
- **Discussion and limitations:** state limitations at the scope warranted by
  evidence. Explain their consequence and boundary; do not inflate a local
  observation into a universal defect or minimize a conclusion-changing issue.
- **Conclusion:** reinforce what was demonstrated and why it matters. Do not add
  an unsupported strength or a new, unexplained limitation.
- **Reviewer response:** answer the question directly before reframing. Admit a
  valid issue, report the actual change or missing evidence, and disagree only
  with a traceable reason. Never use narrative focus to evade a requested result.

## Hard red lines

- Do not fabricate, relabel, or selectively aggregate evidence to create a win.
- Do not switch metrics, datasets, baselines, hypotheses, or stopping rules after
  observing results without explicit disclosure and suitable statistical care.
- Do not suppress negative results, anomalies, exclusions, or failure cases that
  affect the claim boundary.
- Do not convert statistical non-significance into equivalence, an observed mean
  difference into superiority, simulation into deployment, or correlation into
  causation.
- Do not weaken an audit finding or reviewer concern merely because it is
  rhetorically inconvenient.

## Final check

- Is the central advantage explicit, bounded, and supported?
- Does each headline claim point to adequate evidence?
- Are comparison conditions and uncertainty visible?
- Would any omitted or downplayed result change a reasonable reader's conclusion?
- Are limitations proportional rather than self-punitive or evasive?
- Does the response directly address every editor/reviewer request?

## Provenance

Adapted from Adkid-Zephyr's *Anti-Defensive Writing* skill, commit
`0212d11541f6df5ce8a6f22ae82bc651452abd24`, under the MIT License. The IEEE
adaptation adds research-integrity, statistical, reporting, and reviewer-response
boundaries. See `../licenses/anti-defensive-writing-MIT.txt`.
