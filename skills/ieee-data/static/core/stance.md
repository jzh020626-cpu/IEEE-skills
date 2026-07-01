# Default stance and source hierarchy

Use this skill to turn a manuscript's experimental and computational artifacts into an IEEE Transactions-ready reproducibility package: concise availability text, repository or supplementary-material plan, parameter inventory, and missing-information flags.

The governing layer is IEEE journal submission guidance plus target-journal instructions. The implementation layer is engineering reproducibility: code, data, configuration, seeds, logs, model weights, ROS bags or equivalent runtime records, hardware/simulator settings, and exact commands.

## Default stance

- Treat reproducibility as the link between each central claim and the artifacts needed to inspect, rerun, or falsify it.
- Do not invent repository names, DOIs, commit hashes, datasets, licenses, hardware settings, simulation seeds, logs, ROS bags, model weights, embargo dates, or access permissions.
- Prefer durable repositories or IEEE Xplore supplementary material for artifacts that can be shared. Use IEEE DataPort, institutional repositories, Zenodo/OSF/Figshare, GitHub release archives, or discipline repositories only when they fit the artifact and rights.
- Separate code, data, trained models, simulation configuration, hardware settings, logs, and videos. A single vague "available online" statement is not enough.
- If artifacts cannot be public, state why, who controls access, what can still be shared, and how reviewers/readers can evaluate the claim.
- For robotics/control/communications, require enough detail to rerun key experiments: platform, simulator version, controller parameters, network/channel model, random seeds, trial count, metrics, and exact reproduction commands.
- Keep this skill focused on reproducibility and availability. Do not rewrite methods, analyze statistics, or polish prose unless the user asks separately.
- Flag "available upon request" as weak unless a legal, commercial, safety, third-party, or hardware-access restriction is explicit.

## Source hierarchy

Use sources in this order:

1. Target journal instructions and submission-system requirements.
2. IEEE Author Center guidance for supplementary materials, article templates, and graphics/files.
3. IEEE DataPort or repository-specific requirements for datasets and code packages.
4. Domain engineering norms for repeatable simulation, hardware experiments, and statistical reporting.

If a policy detail may have changed, verify the current journal page before giving final submission advice.
