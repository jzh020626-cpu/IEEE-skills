# Article Anatomy — IEEE Transactions Reading Aid

Use this file while building a bilingual reader for IEEE engineering papers. Label each block by argumentative function so the reader can locate the problem definition, technical contribution, evidence chain, limitations, and submission-relevant details.

This is a navigation aid, not a license to summarize. Keep the bilingual side-by-side output and do not replace the paper with a summary-only version.

## Where each function lives

- **Abstract = technical funnel.** Read it as context -> gap -> method -> evidence -> bounded contribution. IEEE abstracts should avoid numbered citations, numbered equations, and footnotes.
- **Index Terms = scope signal.** Use them to infer venue fit, but do not treat them as claims.
- **Introduction = problem -> prior work -> gap -> contributions.** The contribution list is often the fastest way to identify novelty and evidence promises.
- **System model / problem formulation = contract.** Extract assumptions, variables, constraints, objectives, and what is controlled/communicated/observed.
- **Method = mechanism.** Track algorithm steps, controller structure, architecture modules, communication protocol, or proof dependencies.
- **Theory = conditions and guarantees.** For TAC/TCST/TCNS-style papers, identify assumptions, theorem statements, proof dependencies, stability/convergence/optimality claims, and where claims stop.
- **Experiments = evidence chain.** Map each figure/table to datasets, platform/simulator, baselines, ablations, metrics, seeds/trials, and failure cases.
- **Figures/tables = claim carriers.** Captions should define subpanels, variables, units, metrics, baselines, and error bars.
- **Discussion/conclusion = limits and deployment.** Capture limitations, assumptions, future work, and any practical deployment boundary.
- **Appendix/supplement = support material.** Proof details, additional experiments, videos, data, or code are support, not a substitute for main-text claims.

## Genre tells

- **T-ASE**: automation relevance, Note to Practitioners, practical value, quality/robustness/productivity/reliability evidence.
- **TII**: industrial informatics scope, industrial CPS/IIoT/edge/cloud/manufacturing relevance, engineering constraints.
- **TAC**: rigorous control theory, assumptions, theorem/proof, stability/convergence/optimality.
- **TCST**: control technology, implementation, operation/design of control systems, application-specific validation.
- **TCNS**: networked/interconnected systems, distributed control, graph/network assumptions, communication constraints.
- **Robotics/communications**: system setup, hardware/simulation, channel/network model, baselines, ablations, latency/throughput/reliability.

## Chinese reading notes

- 标注每段功能：背景、问题、假设、方法、理论保证、实验、局限、复现。
- 不要把逐段翻译降级成摘要。
- 对 IEEE 论文，优先抓清楚“问题定义 -> 技术新意 -> 证据链 -> 适用边界”。
