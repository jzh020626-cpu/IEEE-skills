# Engineering technical-concern taxonomy

Use this internal ledger after the general and domain-specific review gates. It is a coverage and traceability aid, not an official IEEE taxonomy or a substitute for venue rules.

## Axes

| Axis | Applicable check |
|---|---|
| `novelty-significance` | The advance is distinguished from the strongest archival prior art and matters beyond component recombination. |
| `problem-assumptions` | Problem formulation, information pattern, constraints, oracle knowledge, channel/traffic/topology, and operating assumptions are explicit and defensible. |
| `theory-guarantees` | Theorems, proofs, stability, convergence, feasibility, bounds, complexity, and claimed scope agree. |
| `algorithm-system-design` | Each module is motivated, interfaces are complete, and system/algorithm claims match the actual contribution. |
| `experimental-design` | Baselines, controls, scenarios, seeds, independent units, budgets, tuning, ablations, and failure cases support the inference. |
| `statistical-rigor` | Estimand, uncertainty, repeated-run structure, aggregation, multiplicity, leakage, and comparison method are adequate. |
| `deployment-realism` | Timing, hardware, sensing, compute, communication overhead, protocol realism, scalability, safety, and sim-to-real limits are addressed. |
| `reproducibility` | Code/data/logs, versions, parameters, seeds, hardware/network settings, and run commands permit scrutiny. |
| `figures-and-tables` | Labels, units, denominators, uncertainty, axes, legends, final-column readability, and captions represent results accurately. |
| `research-compliance` | Human/HRI, autonomy, spectrum, cybersecurity, data-license, privacy, safety, and dual-use obligations are reported when applicable. |
| `writing-clarity` | Terminology, symbols, abstract/body consistency, and argument structure make the evidence chain understandable. |
| `claim-moderation` | Strength, generality, superiority, real-time, safety, and deployment language do not exceed the evidence. |

For every axis use `applicable`, `not applicable`, or `not assessable`. Missing supplied material is not automatically a flaw.

## Concern record

Each concern contains `issue_key`, primary `axis`, `severity`, `blocking`, `severity_rationale`, `claim_pointer`, `evidence_pointer`, `evidence_status`, `concern`, and `resolution_test`. Use `location not provided` when a precise locator cannot be verified.

- `major`, blocking: the current evidence cannot establish a central conclusion, or a validity, safety, ethics, authorization, or integrity problem prevents a credible case.
- `major`, non-blocking: the issue materially weakens novelty, inference, generality, reproducibility, or an important evidence link.
- `minor`, non-blocking: the issue is localized and does not change the central conclusion.

Severity reflects impact, not repair cost or tone. A figure, statistical, or writing issue may be major when it changes inference. Minor comments are never blocking. Do not impose a concern quota.

Draft each reviewer report in a genuinely separate context from the common fact base. A reviewer must not read another review before its own report is frozen. Only then map equivalent issue keys in the cross-review synthesis. Differences should arise from preassigned emphasis, not invented identity or contradictory facts.
