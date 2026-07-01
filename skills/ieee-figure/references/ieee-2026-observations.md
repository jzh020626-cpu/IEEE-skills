# IEEE Transactions Figure Archetypes for Robotics, Control, and Communications

Use this note when the user asks for broad IEEE Transactions figure style or when a figure mixes system diagrams, experiments, and quantitative evidence.

## Archetype 1: System-model composite

Use for robotics, automation, industrial informatics, and networked control papers where the reader must understand the architecture before the metrics.

- Let the system diagram occupy roughly 35-55% of the figure.
- Use the same symbols and colors for agents, sensors, controllers, networks, and constraints in every panel.
- Show information flow, physical flow, or control loop direction with restrained arrows.
- Pair the diagram with 2-4 evidence panels: baseline comparison, ablation, complexity, latency, or robustness.

## Archetype 2: Trajectory / time-response figure

Use for AGV, robot, UAV, manipulator, tracking, stability, and control-response results.

- Keep axes comparable across methods and trials that invite comparison.
- Mark safety limits, constraints, setpoints, convergence bands, or terminal tolerance visibly.
- Use neutral baseline lines and one clear proposed-method color.
- Put trial/seed count and error-band definition in the caption.

## Archetype 3: Communications / network constraint figure

Use when delay, packet loss, throughput, AoI, bandwidth, contention, or reliability affects the result.

- Show the network/channel model or load condition explicitly.
- Separate mechanism plots (delay/loss/load) from outcome plots (success, error, completion time).
- Use aligned x-axes for load or time whenever the causal chain matters.
- Include units and definitions for latency, throughput, overhead, reliability, and freshness metrics.

## Archetype 4: Benchmark / ablation grid

Use for algorithmic comparison, industrial informatics, learning-based control, and robotic perception/planning evaluations.

- Put methods in the same order across all panels.
- Define whether higher or lower is better for every metric.
- Use direct labels or one shared legend; avoid repeated legends inside each panel.
- Include variability across seeds, trials, folds, or scenarios.
- Reserve a small panel for computational cost, parameter count, runtime, or communication overhead when it affects engineering value.

## Archetype 5: Hardware/simulation evidence panel

Use when photographs, screenshots, maps, sensor frames, or simulator scenes prove that the experiment setting is real and bounded.

- Keep raster evidence subordinate to the quantitative claim unless the visual setting is the main contribution.
- Use scale, coordinate frame, task zone, robot ID, or sensor field-of-view overlays when needed.
- Do not use screenshots as decoration; each image must answer a reviewer question about setup, feasibility, or failure mode.

## Cross-cutting IEEE Rules

- Design for single-column and double-column readability before polishing.
- Panel labels should be small, consistent, and template-compatible.
- Use captions to define variables, units, baselines, and error bars.
- Avoid decorative frames, gradients, and excessive color.
- Vector output is preferred for plots and diagrams; raster output is reserved for photos/screenshots.
- Figures must support the paper's claim chain, not merely display all available results.
