# Manuscript consistency sweep

Use this retrospective audit after multiple drafting or revision rounds. Count variants mechanically, then inspect each context before changing text; a finding is not an automatic correction.

Run the bundled checker from the `ieee-shared` directory:

```bash
python scripts/check_consistency.py manuscript.tex tables.tex \
  --term-group 'controller=MPC controller|predictive controller' \
  --term-group 'method-name=GraphNet|Graph Net'
```

Audit in this order:

1. Numeric self-consistency across abstract, methods, tables, figures, results, and conclusion.
2. Claims versus the displayed data, including exceptions hidden by averages.
3. Terminology, acronym first use, units, precision, self-reference, tense, hyphenation, and spelling variety.
4. Scenario and protocol consistency: robot platform, control period, topology, channel/traffic model, bandwidth, latency, packet-loss model, seeds, and dataset split.
5. Cross-references and redundancy between prose and displays.
6. Recompile and re-check anything dependent on pagination.

Headline counts must be derivable from the experimental design. The same metric uses one precision everywhere. The same physical or networking quantity must not silently change units or assumptions. A superlative must survive every relevant row, scenario, and uncertainty comparison. Do not infer statistical superiority from overlapping or absent uncertainty evidence.

Any response letter, cover letter, slide deck, or supplementary artifact quoting the manuscript must be synchronized after every content change.
