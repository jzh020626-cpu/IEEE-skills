# Multi-panel evidence architecture for IEEE engineering papers

Use this reference before assembling a multi-panel main figure. A figure should
answer one Results-level question through complementary evidence roles, not act
as a storage page for plots produced by one script.

## Start from the question

Write the figure question in one sentence, then give each panel one non-duplicate
role. Common roles include:

| Role | Engineering examples |
|---|---|
| Setup or system context | Robot/platform, plant/controller, sensing-actuation loop, network topology, channel/traffic model, test scene |
| Representative behavior | Trajectory, state response, control input, packet trace, constellation, hardware frame |
| Primary evidence | Tracking error, stability margin, success rate, throughput, latency, reliability, energy |
| Baseline/control | Standard controller, protocol, heuristic, oracle, no-safety-layer or module ablation |
| Orthogonal validation | Theory versus simulation, simulation versus HIL/hardware, link versus network, laboratory versus field |
| Stress or perturbation | Model mismatch, disturbance, delay, packet loss, low SNR, topology change, load, OOD scene |
| Mechanism/diagnostic | Module contribution, closed-loop pathway, theoretical bound, resource bottleneck |
| Boundary/failure | Safety constraint, feasible set, saturation, instability, outage, scale limit, operating envelope |

If two panels answer the same question with the same evidence type, merge them,
move one to Supplementary Material/appendix, or justify why the second changes
the inference. Cover each panel mentally; if the figure's conclusion remains
complete, that panel is not necessary in the main figure.

## Useful evidence chains

- **Robotics/control:** architecture and scene -> closed-loop primary performance
  -> constraint/safety evidence -> disturbance/model-mismatch robustness ->
  real-time computation and failure boundary.
- **Communications/networking:** system model/topology -> rate, latency and
  reliability evidence -> strongest aligned baseline -> scaling/load -> channel
  uncertainty, outage, fairness or energy trade-off.
- **Control/theory:** assumptions and property -> bound/stability result ->
  tightness or conservatism -> numerical/hardware illustration -> behavior when
  an assumption is violated.
- **Benchmark/testbed:** construction and coverage -> quality/validity -> baseline
  ranking -> sensitivity/stability -> reuse and external-validity boundary.

These are examples, not mandatory panel counts or orders. A small figure is often
stronger than a large one when it contains the shortest sufficient evidence chain.

## Across-figure progression

Each later figure should ask a deeper or different question. Avoid a sequence of
figures that all restate "the proposed method performs well." A coherent paper
may progress through:

`problem/system -> core capability -> comparison/ablation -> robustness and resource trade-offs -> mechanism or boundary`

The actual sequence follows the manuscript argument and available evidence.

## Layout and QA

- Give the primary evidence the largest or earliest visual position.
- Use consistent colors, line styles, symbols, units, uncertainty definitions,
  baseline names, and panel labels across the figure.
- Shared axes and legends are useful only when scales and semantics truly match.
- Final alignment is a physical rendered property, not a GridSpec intention;
  run the panel-alignment gate after layout is complete.
- Run rendered collision QA on the exported PDF. Direct labels, constraint lines,
  arrows, confidence bands, and dense curves must not cut through text.
- A rasterized or outlined-text PDF that cannot be audited is `NOT AUDITABLE`,
  not a pass; perform final-size visual inspection and retain the limitation.
- Route non-leading audit panels to another main figure, Supplementary Material,
  appendix, or artifact package only when target-venue rules permit it. Never
  hide evidence that changes the central conclusion.
