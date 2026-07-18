# IEEE Domain-Specific Review Gates

Load only the section matching the manuscript. These are prompts, not proof that a flaw exists.

## Control theory and control systems

- Is the system model complete and notation consistent?
- Are assumptions explicit, necessary, and used where claimed?
- Do theorem, lemma, proof, and corollary dependencies close logically?
- Are stability, convergence, feasibility, optimality, robustness, and performance guarantees bounded to proved conditions?
- Are numerical studies and implementation evidence aligned with the theory?
- For TCST, is the technological realization/application contribution visible rather than only abstract theory?

## Robotics and automation

- Are task, environment, platform/simulator, sensors, control stack, safety boundary, and real-time constraints specified?
- Are baselines current and comparable under the same data, tuning, compute, and evaluation protocol?
- Are ablations, failure cases, repetitions/seeds, uncertainty, and sim-to-real or deployment limits reported?
- For T-ASE, is automation-science/engineering relevance explicit and is the Note to Practitioners distinct and evidence-bounded?

## Communications and networked systems

- Are channel/network/topology, traffic, interference, synchronization, delay, packet loss, bandwidth, and reliability assumptions defined?
- Are throughput, latency, energy, spectral efficiency, overhead, scalability, and robustness compared under fair conditions?
- Are simulations separated from analytical guarantees and hardware/testbed evidence?
- For distributed/networked control, are graph/connectivity and communication constraints reflected in proofs and experiments?

## Industrial informatics and cyber-physical systems

- Is the industrial setting real and technically relevant rather than a generic algorithm label?
- Are plant/process/data provenance, edge/cloud/PLC/SCADA constraints, reliability, security, timing, and deployment cost stated?
- Does validation cover representative operating regimes, disturbances, failures, and generalization boundaries?

## Signal processing, machine learning, and data-driven methods

- Are dataset provenance, splits, leakage prevention, preprocessing, tuning, seeds, and compute reported?
- Are metrics appropriate, uncertainty visible, and comparisons paired/fair?
- Are ablations tied to claimed modules? Are calibration, robustness, distribution shift, and failure modes addressed where relevant?
- Are learned components distinguished from deterministic signal-processing or control guarantees?

## Hardware, power, and electronics

- Are device/circuit/system specifications, tolerances, calibration, sampling, thermal/power limits, and measurement uncertainty stated?
- Are efficiency, losses, bandwidth, stability, reliability, aging, safety, and hardware variation evaluated?
- Are simulations corroborated by appropriate prototypes or experiments when hardware claims are central?

## Conference extension and prior versions

- Is the prior conference/preprint/thesis version cited and disclosed where required?
- Are added archival contributions concrete: theory, proofs, algorithmic depth, experiments, datasets/scenarios, analysis, or discussion?
- Are overlapping figures/text/results identified honestly?
- Do not enforce a universal percentage threshold; apply the target journal's current rule.
