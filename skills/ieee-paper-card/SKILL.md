---
name: ieee-paper-card
description: Build a source-grounded deep-reading Paper Card for one IEEE or engineering paper, preprint, PDF, DOI, arXiv page, publisher article, or pasted paper text. Use for single-paper deep analysis, module-by-module analysis, equation and assumption extraction, experiment-to-claim evidence chains, conclusion-boundary audits, critical analysis, knowledge connections, or testable research ideas in robotics, automation, control, communications, networking, industrial informatics, and adjacent engineering fields. Do not use for full-paper bilingual translation, formal peer-review reports, batch literature monitoring, or public-article writing.
---

# IEEE Paper Card Router

Turn one engineering paper into an evidence-grounded research card, not a translated abstract, generic summary, or reviewer report.

## Routing protocol

1. Read `manifest.yaml` and every file under `always_load`.
2. Establish the source boundary: full paper, text without reliable layout, abstract/metadata only, or an existing `ieee-reader` artifact.
3. For a PDF or reader source map, run the bundled `scripts/prepare_paper.py` from this skill directory and inspect its validation block. Never invent page locators when extraction fails.
4. Classify the dominant contribution as `algorithm`, `system`, `theory`, `benchmark`, `application`, or `review`. Load at most one secondary lens when it carries independent evidence.
5. Build an evidence inventory before drafting: metadata, problem and claims, assumptions, modules and data flow, equations/theorems, figures/tables, experiments, baselines, metrics, ablations, robustness, limitations, and stable source pointers.
6. Build a claim-evidence matrix. Distinguish source fact, externally verified fact, analysis, and hypothesis.
7. Generate the fixed Sections 01-16 defined in `references/card-schema.md`. Use `Not applicable` or `Not assessable from supplied material` instead of inventing content.
8. Run `scripts/audit_paper_card.py` with the strongest valid locator mode: `page-grounded`, `structure-grounded`, or `source-limited`. Audit errors block delivery.

For robotics and automation, inspect physical platform, task scene, sensing/control loop, safety envelope, sim-to-real gap, latency, failure cases, and hardware evidence. For communications and networking, inspect channel/traffic/topology assumptions, CSI, complexity, overhead, latency, reliability, scalability, and protocol realism. For control, inspect assumptions, feasibility, stability/convergence claims, proofs, and numerical/physical validation.

## Red lines

- Never infer unseen figures, equations, baselines, results, guarantees, or novelty.
- Never present the paper's related-work narrative as independently verified field history.
- Never turn a candidate idea into a novelty claim without external search.
- Never substitute a one-off extraction script for the bundled scripts during a normal run.
- Keep all 16 sections in order; do not silently convert the requested card into a translation, review report, or slide deck.

## Adjacent skills

- `ieee-reader`: full bilingual reader and stable source map.
- `ieee-academic-search`: external literature and novelty verification.
- `ieee-reviewer`: formal reviewer-style assessment.
- `ieee-literature-pipeline`: batch discovery and monitoring.
- `ieee-paper2ppt`: presentation output.
