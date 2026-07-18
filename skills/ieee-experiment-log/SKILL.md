---
name: ieee-experiment-log
description: Create, normalize, or audit reproducible engineering experiment logs for IEEE Transactions research from raw notes, terminal output, screenshots, voice transcripts, configuration files, CSV summaries, simulation runs, or hardware-test records. Use for robotics, automation, control, communications, industrial informatics, power/electronics, signal-processing, and machine-learning experiments when Codex should produce YAML-frontmatter Markdown logs, run indexes, anomaly records, equipment tracking, seed/configuration records, or artifact links without inventing missing facts.
---

# IEEE Engineering Experiment Log

Convert raw experiment material into a traceable record that can support later analysis, figures, reproducibility packages, and reviewer responses.

## Workflow

1. **Resolve the destination.** Use the user's project, vault, or output folder. Never assume a private Obsidian, Feishu, or laboratory path.
2. **Preserve the raw input.** Link or copy source notes only when authorized. Do not rewrite the sole raw record.
3. **Assign a stable run identity.** Record project, experiment series, run ID, date/time, operator, branch/commit, and parent run where known.
4. **Classify the experiment.** Select `simulation`, `hardware`, `field`, `network`, `dataset`, `training`, `benchmark`, or `mixed`.
5. **Record the design.** Capture objective, hypothesis, factors, controls, baselines, independent unit, repetitions, seeds, initial conditions, disturbances, datasets/scenes/topologies, and stopping criteria.
6. **Record the environment.** Capture hardware, firmware, operating system, compiler/runtime, packages, model/checkpoint, instruments, calibration, communication settings, and clock/synchronization details.
7. **Separate procedure from result.** Preserve commands and protocol steps; record raw observations separately from interpretation and next-action decisions.
8. **Record deviations and failures.** Link an anomaly entry for crashes, dropped packets, unsafe states, saturation, sensor drift, thermal limits, data exclusions, or protocol departures.
9. **Link artifacts.** Record paths or persistent links for configs, code, logs, ROS bags, traces, packet captures, datasets, checkpoints, plots, videos, and checksums when available.
10. **Update the index.** Add the run and its status to the experiment index without deleting earlier entries.

## Domain routing

- Control/simulation run: read `references/example-control-simulation.md`.
- Robotics/hardware trial: read `references/example-robotics-hardware.md`.
- Communications/network sweep: read `references/example-communications-sweep.md`.
- New log: start from `templates/run-log.md`.
- Equipment or calibration state: use `templates/equipment-tracking.md`.
- Failure/deviation: use `templates/anomaly-log.md`.
- Project overview: use `templates/experiment-index.md`.

## Output rules

- Keep YAML machine-readable and the narrative human-readable.
- Use `AUTHOR_INPUT_NEEDED` for missing facts that materially affect reproducibility.
- Distinguish independent runs from samples within one run, time points, frames, packets, or repeated sensor readings.
- Use explicit units and preserve parameter precision.
- Record exclusions with the exact rule and before/after counts.
- Mark interpretations as interpretations; do not convert observations into causal claims.

## Red lines

- Do not invent run IDs, timestamps, seeds, commits, parameters, measurements, calibration results, success states, or failure causes.
- Do not expose credentials, tokens, participant identifiers, proprietary data, or confidential infrastructure details.
- Do not overwrite raw logs or silently replace an earlier result.
- Do not mark a run `reproduced` until the rerun and comparison evidence are supplied.
