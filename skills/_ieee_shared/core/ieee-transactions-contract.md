# Strict IEEE Transactions Manuscript Contract

Default target: IEEE Transactions or Letters in robotics, automation, control, communications, industrial informatics, and networked cyber-physical systems, especially T-ASE, TII, T-RO/RA-L, TAC, TCST, TCNS, TIE, TWC, TCOM, and IoT-J.

Use this contract for manuscript-facing output unless the user explicitly selects another venue family.

## Non-negotiable IEEE Layer

- Format for IEEE journal review: IEEE article template or IEEEtran-style double-column manuscript; do not draft in a non-IEEE journal style.
- Front matter must include a concise technical title, Abstract, and Index Terms. Abstracts must not contain numbered equations, numbered references, or footnotes.
- Citations must be IEEE numeric citations (`[1]`, `[2]`, ranges such as `[3]-[5]`) with the reference list ordered by first citation, not author-year.
- Claims must be traceable to assumptions, equations, algorithms, experiments, figures, tables, and references. Do not invent theorem guarantees, hardware details, citations, datasets, or metrics.
- Figures and tables must be readable at IEEE single-column or double-column width, with self-contained captions, visible units, panel labels, and export files in IEEE-accepted graphics formats.
- Reproducibility material must identify code, data, parameters, random seeds, logs, simulation settings, hardware, software versions, ROS bags or equivalent runtime records, and exact reproduction commands when available.
- Supplementary material may include data, software, videos, derivations, proofs, and additional experiments, but it must be referenced from the manuscript and not carry essential claims that the main paper never states.

## Venue-Specific Hard Checks

### T-ASE

- Include a distinct `Note to Practitioners`; it is not a second abstract. It should explain practical use, assumptions, limitations, and deployment readiness in practitioner-facing language.
- For initial review, enforce double-anonymous hygiene when the target instructions require it: no author names, affiliations, acknowledgments, project pages, self-identifying repository links, or revealing supplement metadata.
- The contribution must address automation science or engineering with explicit relevance to quality, robustness, stability, productivity, efficiency, completeness, optimality, convergence, performance guarantees, complexity, sensitivity, verification, or reliability.
- Compare against previous methods numerically when possible; otherwise explain why no prior method is a relevant comparator.
- Prefer archival journal versions and include recent related work when the area has moved in the last two years.

### TII

- Industrial informatics relevance must be explicit: industrial cyber-physical systems, IIoT, smart manufacturing, energy, edge/cloud industrial intelligence, reliability, security, or deployed industrial data/control constraints.
- New regular research submissions from 2025 onward should be audited against the strict 10-page initial-submission limit; review/state-of-the-art and letter limits require the current TII checklist.
- A generic control, communication, or ML paper is not TII-ready unless the industrial system model, constraints, validation setting, and engineering value are visible.

### TAC / TCST / TCNS

- TAC-style work must make assumptions, problem formulation, theorem/proof logic, stability, convergence, optimality, or robustness claims explicit and bounded.
- TCST-style work must emphasize technological advances in the design, realization, or operation of control systems for concrete application areas; implementation details and performance evidence matter.
- TCNS-style work must expose the networked/interconnected system model, assumptions, constraints, and scalability or robustness evidence; police excessive self-citation and conference-extension overlap.
- Conference extensions must cite the earlier version, state the added archival value, and identify new proofs, results, experiments, theory, or technical depth.

### Robotics / Communications

- Robotics papers must state task scenario, robot/platform or simulator, sensors, hardware limits, baselines, ablations, failure cases, and statistical variation across trials/seeds when relevant.
- Communication/networked-system papers must state channel/network model, latency, throughput, packet loss, delay, reliability, overhead, and robustness assumptions where those mechanisms affect the result.

## Strict Gate

For submission audits, use:

- `Go`: no blocking IEEE/venue violations remain; only normal author confirmation is needed.
- `Conditional Go`: technical content is plausible, but manual confirmations or minor fixes remain.
- `No-Go`: missing venue-mandatory sections, wrong format/citation style, page-limit violation, missing Note to Practitioners for T-ASE, untraceable claims, or unreproducible central results.
