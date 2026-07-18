# Strict IEEE Transactions Pre-Submission Checklist

Use this checklist for final readiness audits. It is intentionally strict: failure to prove a requirement from the provided manuscript is `manual`, not `pass`.

## Official Sources To Verify

- IEEE Article Templates: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/>
- IEEE Editorial Style Manual / Reference Guide entry point: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/ieee-editorial-style-manual/>
- IEEE graphics file formatting: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/>
- IEEE supplementary material guidance: <https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/>
- T-ASE author checklist: <https://www.ieee-ras.org/publications/t-ase/information-for-authors-t-ase/author-checklist-for-papers-submitted-to-ieee-t-ase/>
- T-ASE Note to Practitioners: <https://www.ieee-ras.org/publications/t-ase/information-for-authors-t-ase/t-ase-note-to-practitioners/>
- T-ASE final manuscript checklist: <https://www.ieee-ras.org/publications/t-ase/information-for-authors-t-ase/t-ase-author-checklist-for-accepted-papers-final-manuscripts/>
- TII author information and checklist: <https://www.ieee-ies.org/pubs/transactions-on-industrial-informatics>
- TAC author information: <https://ieeecss.org/publication/transactions-automatic-control/author-info>
- TCST author information: <https://www.ieeecss.org/publication/transactions-control-systems-technology/author-info>
- TCNS author information: <https://ieeecss.org/publication/transactions-control-network-systems/information-authors>

## Common IEEE Hard Checks

| Area | Strict check |
|---|---|
| Template | Manuscript uses IEEE article template or IEEEtran-style double-column journal format. |
| Abstract | Abstract exists and contains no numbered citations, numbered equations, or footnotes. |
| Index Terms | Index Terms are present and separated from the Abstract. |
| References | In-text citations use numeric square-bracket IEEE style; references are ordered by first citation. |
| Acronyms | Each acronym is expanded at first use unless it is universally standard in the field. |
| Figures | Plan for 88.9 mm or 182 mm width; vector preferred; color/grayscale raster ≥300 dpi and B/W line art ≥600 dpi; verify accepted formats. |
| Tables | Tables have units, definitions, and readable column headings at final two-column scale. |
| Supplement | Supplementary files are referenced in the main text and contain only support material, not hidden core claims. |
| ORCID | IEEE journals require ORCID for all authors; confirm every author record. |
| Integrity | Check plagiarism/overlap, conference-extension disclosure, permissions, and anonymous-review hygiene. |

## T-ASE Checklist

- The paper addresses automation science and engineering, not generic robotics/control/ML without automation relevance.
- Include a 100-300 word `Note to Practitioners` immediately after the Abstract and before Index Terms.
- Audit Abstract length against the current 200-word Regular / 50-word Communication limit.
- Audit Regular Papers against the current 10-page submission target in the 2026 procedure manual; verify current Communication/overlength details.
- The NtP explains practical use, assumptions, limitations, and near-term implementation without duplicating the Abstract.
- For double-anonymous review, remove author-identifying names, affiliations, funding acknowledgments, repository ownership, and supplement metadata.
- The paper explicitly addresses relevant automation issues such as quality, robustness, stability, productivity, efficiency, completeness, optimality, convergence, performance guarantees, time complexity, sensitivity, verification, or reliability.
- Compare against previous methods numerically where possible; otherwise justify why no relevant prior comparator exists.
- Include recent related work from the last two years when the field has current archival work.
- Final manuscript packages must satisfy current page/overlength charge, keywords/index terms, biographies/photos, source files, and graphics requirements.

## TII Checklist

- Industrial informatics relevance is explicit: industrial CPS, IIoT, manufacturing, smart grid, process systems, industrial edge/cloud, reliability, safety/security, or deployment constraints.
- New Research manuscripts are audited against 10 pages; Review/SoA against the current permission/12-page rule; Letters against 4 pages.
- Confirm anonymous manuscript hygiene and institutional-email requirements.
- Review/state-of-the-art manuscripts require current checklist compliance and EiC-permission logic; Letters are audited against 4 pages.
- The system model, data source, industrial constraints, and validation setting must be visible. A generic algorithm paper without industrial evidence is `No-Go`.
- Results should include baseline comparison, ablation or component evidence, robustness/reliability analysis, and engineering cost or complexity when relevant.

## TAC Checklist

- Problem formulation is mathematically precise: system model, assumptions, objectives, admissible signals/sets, and notation are complete.
- Theorems, lemmas, propositions, and proofs are logically linked and do not hide critical assumptions.
- Stability, convergence, optimality, feasibility, robustness, or performance claims are stated only within proved or experimentally supported conditions.
- Full Papers are audited against the current TAC double-column page policy; Technical Notes/Correspondence use the shorter current limit.
- Conference extensions cite the prior version and state added archival value such as new proofs, stronger theory, broader experiments, or deeper discussion.

## TCST Checklist

- The contribution is a technological advance in the design, realization, or operation of a control system for a specific application area.
- The manuscript contains implementation details, practical constraints, validation evidence, and performance comparison, not only abstract control theory.
- Page audit: Papers, Brief Papers, and Letters must satisfy the current 16/8/4-page style limits unless the journal page has changed.
- Conference extensions must cite the earlier paper and explain differences and added value.

## TCNS Checklist

- The paper is about interconnected/networked systems; graph, communication, coupling, distributed control, or network constraints must be explicit.
- Audit double-column 10-pt IEEE format and the current 12-page total / 10-page main-text convention.
- Self-citation should not be excessive; if the target page has a numeric cap, enforce it.
- Upload or disclose prior conference versions as required by current TCNS instructions.

## Robotics / Communications Evidence Checks

- Robotics: task scenario, robot or simulator, sensors, controller, hardware limits, trials/seeds, failure modes, baselines, ablations, and statistical variation.
- Communications: channel/network model, latency, throughput, packet loss, delay, reliability, overhead, scalability, and robustness assumptions.
- Control: assumptions, theorem/proof, stability/convergence, feasibility, sensitivity, and implementation constraints.

## Gate Rules

- `Go`: no blockers; manual checks are routine submission-system confirmations.
- `Conditional Go`: no obvious blockers, but missing manual confirmation or small repairs remain.
- `No-Go`: wrong template/citation style, missing mandatory venue section, page-limit violation, missing T-ASE NtP, absent evidence for central claims, anonymous-review violation, or unreproducible central empirical result.
