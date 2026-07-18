# Workflow

Run these nine steps for any paper-to-deck job. The paper-type fragment loaded for this job sets the narrative arc; this workflow is the shared spine. Deep design, figure, and self-review material lives in the on-demand references named below.

## Step 1. Read and extract source material

Extract, when available: title, authors, journal/preprint server, year, DOI; field and subfield; paper type; central problem and knowledge gap; main claim or thesis; system model, task scenario, workflow, model, dataset, or experimental platform; key methods and controls; main results and quantitative findings; key figures, tables, and figure legends; validation, robustness, ablation, or sensitivity analyses; limitations and unresolved questions; broader engineering, deployment, technical, environmental, or practitioner meaning.

Do not invent missing numbers, mechanisms, datasets, or figure details. Use a two-pass reading strategy: first capture metadata, abstract, headings, figure legends, and table captions; then read only the result and methods pages needed to support the slides. Start the Terminology Ledger here.

## Step 2. Classify the paper and choose the presentation logic

The router already detected the `paper_type` axis and loaded the matching arc fragment. Confirm the classification against the source, then follow that fragment's arc (`claim-first`, `question-to-evidence`, `problem-to-solution`, `workflow-to-validation`, or `evidence-map`) when ordering slides.

## Step 3. Build the Chinese presentation plan

Default length: 12-16 slides for a 15-20 minute report; prefer 10-14 for a quick or unspecified request; expand beyond 16 only for a detailed seminar deck or when the paper genuinely needs the space. Use the default slide structure from the loaded paper-type fragment and adapt it to the paper. Do not force every paper into the same template.

Before authoring, plan the visual rhythm: assign each slide a visual role and a composition type, and avoid repeating the same role/composition too often. For the composition-type catalogue and the rule against single-layout-family decks, open `references/design-and-layout.md`.

## Step 4. Select figures as evidence, not decoration

Prioritize figures that carry the argument: design/workflow, main evidence, validation/robustness, mechanism/model/synthesis, then practical/conceptual implication. Prefer a few readable key panels over many unreadable full figures. For the full selection checklist, open `references/figure-assets.md`.

## Step 5. Extract and prepare figure assets

Extract or render only selected figures, crop dense panels, keep original data visuals unchanged, save under `output/assets/figures/`, and record traceability in `output/asset_manifest.md`. For a standard 10-14 slide deck, usually select 4-8 assets. Prefer editable PPT-native tables/charts when values are explicit. A crop that removes panel letters, axes, legends, scale bars, method labels, table headers, or necessary annotations is a high-severity defect and must be fixed before insertion.

## Step 6. Write slide-by-slide content

For each slide write a conclusion-style Chinese title where possible, purpose, layout, 2-4 concise bullets, selected evidence, caption/interpretation, one takeaway, and useful speaker notes. Avoid generic frames such as “一句话总结”, “最有价值的后续方向”, “不是……而是……”, or vague “提供新视角”; use paper-specific evidence.

Respect the on-slide text budget: write for the slide, not the manuscript; most explanation belongs in speaker notes. Order each result slide as hero evidence first, then a narrow interpretation rail, then only the minimum labels. The detailed text budget, evidence hierarchy, layout-adaptation, anti-template, archetype, title, and density rules are in `references/design-and-layout.md`.

## Step 7. Build the actual PPTX deck

Create a real `.pptx` with `python-pptx` or a user template, 16:9 by default, Chinese titles/bullets/captions/notes, source labels, conservative text margins, and consistent typography. Align titles, figure edges, source labels, caption bands, and bottom notes to stable guides. Let geometry follow the evidence. Treat auto-shrink as a last resort; shorten, enlarge, or split instead of accepting clipping.

## Step 8. Self-review and corrective revision loop

After the first draft, inspect the PPTX/assets, write a slide-numbered `high`/`medium`/`low` defect list, run `scripts/audit_pptx_quality.py output/final_presentation_cn.pptx --report output/pptx_audit.md`, fix all high and reasonable medium issues, regenerate, rerun the audit, and update `output/qa_report.md`.

## Step 9. Final verification

Reopen the PPTX, check slide/media/notes counts and shape bounds, inspect cropped-asset contact sheets, and confirm the audit has no unresolved high-severity findings. Fix blockers before delivery and document remaining limits in `output/qa_report.md`.
