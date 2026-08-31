# Engineering evidence chain across manuscript sections

Use this reference when Abstract, Introduction, Results/Experiments, Discussion,
and Conclusion must tell one consistent IEEE Transactions story. It is a logic
contract, not a venue-specific format rule.

## Shared chain

`operational or scientific problem -> unresolved constraint/question -> proposed technical move -> decisive evidence -> bounded contribution`

Each section performs a different job:

- **Abstract:** shortest complete chain; one principal claim and the minimum
  decisive evidence or formal guarantee needed to trust it.
- **Introduction:** establishes why the unresolved question matters, what prior
  work already enables, what constraint remains, and why the proposed route can
  answer it.
- **Results/Experiments:** establishes the claims in the shortest sufficient
  evidence order, including uncertainty and conclusion-changing boundaries.
- **Discussion:** synthesizes what the established claims mean together,
  positions them against prior work, calibrates interpretation, and states scope.
- **Conclusion:** restates the solved problem, supported contribution, and
  operating boundary without adding new evidence.

## Paper-type evidence routes

- **Algorithm/learning:** task and information constraints -> method insight ->
  aligned baselines -> ablation/diagnosis -> generalization and compute cost ->
  failure boundary.
- **Control/theory:** system model and assumptions -> property/theorem -> proof
  obligations -> robustness/feasibility/complexity -> numerical or hardware
  illustration -> domain of validity. Simulation illustrates; it does not prove
  stability, optimality, or safety.
- **Robotics/system:** required capability -> architecture and interfaces ->
  component and end-to-end validation -> perturbation/safety/failure tests ->
  timing and resource feasibility -> demonstrated deployment envelope.
- **Communications/networking:** system/channel/traffic/topology assumptions ->
  analytical design or bound -> complexity/overhead/scalability -> simulation ->
  link/network/testbed validation -> working regime and trade-offs.
- **Benchmark/resource:** gap in evaluation -> construction and quality controls
  -> metric validity -> baseline coverage -> sensitivity/ranking stability ->
  reuse and external-validity boundary.

## Cross-section consistency gates

1. Every headline contribution has a corresponding decisive evidence item or
   formal result in the body.
2. Every assumption that materially limits a guarantee appears before the
   guarantee is generalized.
3. The Abstract and Conclusion do not claim deployment, safety, real-time
   operation, scalability, or superiority beyond the tested/proved conditions.
4. Results do not repeat a table chronologically; Discussion does not replay
   Results without adding synthesis, positioning, or boundary.
5. Negative or mixed evidence that changes a central conclusion stays visible.
6. If the venue does not accept Supplementary Material, route required evidence
   to the main text, appendix, or an allowed artifact rather than a nonexistent file.
