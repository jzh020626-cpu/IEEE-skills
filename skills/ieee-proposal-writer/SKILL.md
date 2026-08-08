---
name: ieee-proposal-writer
description: Proposal-first research writing state machine for IEEE Transactions manuscripts in robotics, automation, control, communications, networking, and industrial informatics. Use to compose, revise, or audit scope, research canon, evidence tables, argument maps, section contracts, QA reports, Chinese/English proposals, paper frameworks, or research plans before prose drafting.
---

# IEEE Proposal Writer

This is an evidence-first state machine, not a generic “write my paper” prompt.

## Core rules

1. Evidence before prose: establish `research_canon` and `evidence_table`.
2. Argument before sections: complete `argument_map`.
3. Contracts before paragraphs: every section declares purpose, inputs, allowed claims, forbidden claims, and validation.
4. Scope before completeness: freeze the current phase and target venue; do not silently expand a paper into several contributions.
5. Engineering value before component labels: distinguish a real algorithm, theory, system, benchmark, or application advance from a combination of known modules.
6. Content before style: repair logic, assumptions, evidence, and feasibility before polishing language.
7. Never upgrade epistemic strength: simulation is not deployment, compatibility is not causality, and an observed mean gap is not statistical superiority.
8. Stop when key evidence, authority, or feasibility is missing; lower claim commitment or split scope instead of masking the gap.

## Mode routing

- Topic, direction, or rough idea: `compose` and `references/compose-mode.md`.
- Existing paragraph, section, or full proposal: `revise` and `references/revise-mode.md`.
- Existing draft plus missing/expanded modules: `hybrid` and `references/hybrid-mode.md`.
- Approved proposal that must not drift: `references/within-approved-proposal.md`.
- Evidence too weak for the intended claims: `references/降承诺提案模式.md`.

Infer the mode when safe. Ask only when the choice materially changes scientific scope.

## Foundation package

Initialize from the templates in `manifest.yaml`:

```text
00_scope.md
01_research_canon.md
02_evidence_table.md
03_argument_map.md
04_section_contracts.md
05_style_guide.md
state.json
sources/
drafts/
revision_briefs/
qa_logs/
exports/
```

The evidence table maps each central claim to source type, exact support, limitations, required experiment/theorem/analysis, and current status. The argument map must connect problem, gap, hypothesis, contribution, method modules, baselines, ablations, robustness/failure evidence, and venue significance.

## IEEE engineering gates

- Robotics/automation: platform, scene, sensing/control loop, timing, safety layer, sim-to-real boundary, failures, and hardware evidence.
- Control: information pattern, assumptions, feasibility, stability/convergence proof, robustness, computation, and validation.
- Communications/networking: topology, channel/traffic/CSI assumptions, protocol stack, overhead, latency, reliability, scalability, and fair baselines.
- Learning: independent units, splits/leakage, seeds, tuning budget, uncertainty, generalization, and deployment shift.
- All domains: strongest archival prior art, aligned baselines, component necessity, reproducibility, limitations, and target-journal hard constraints.

## QA order

1. Independent specialist-lens content review using `references/specialist-lens-review.md` when substantive risks exist.
2. Claim/citation/numbering/reproducibility validation using `references/validation-checklist.md`.
3. Anti-slop and language cleanup using `references/research-anti-slop.md` when applicable.
4. Eight-dimension scoring using `references/evaluation-rubric.md`.

If a gate fails, revise the weakest foundation file before changing prose. Run no more than three unguided iterations; then report the unresolved evidence or scope decision.

## Delivery

Return the updated artifact or path, current state and score, unresolved risks, and one recommended next step. Never invent citations, results, proof guarantees, hardware settings, regulatory permission, or completed experiments.
