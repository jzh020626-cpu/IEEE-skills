# AI-assisted graphical abstract workflow

Use this reference only when the user explicitly requests a graphical abstract
or visual summary. A graphical abstract is not required by every IEEE journal;
verify the target venue's current author instructions, permitted file type,
dimensions, accessibility requirements, and generative-AI policy before making
a submission claim.

## Define the contract first

Record:

- one central technical message;
- intended reader and target venue;
- visual type: system pipeline, hierarchy, comparison, temporal flow, control
  loop, network topology, or problem–solution–outcome;
- source facts and assets that may be shown;
- labels, units, notation, and claims that must remain exact;
- what the evidence does not support;
- whether the output is an internal concept draft or a candidate submission asset.

Prefer a native vector/block-diagram workflow for architectures, control loops,
network topologies, and plots. Use image generation only for a bounded
illustrative component that is hard to create natively and whose use is allowed.

## Evidence and provenance gates

- Do not invent hardware, sensors, channels, topology, measurements, equations,
  trajectories, stability guarantees, causal paths, or performance values.
- Do not depict simulation as field deployment or a conceptual safety layer as
  a certified guarantee.
- Preserve reference-image rights and source attribution.
- Record prompt, model/backend, generation date, input references, chosen output,
  and every material human correction.
- Treat generated technical text and symbols as untrusted. Recreate labels,
  equations, axes, and annotations with editable native elements and verify them.
- Before uploading unpublished or sensitive material to an external image/OCR
  provider, obtain explicit authorization and disclose the provider boundary.

## Review sequence

1. Generate or sketch several low-commitment layout alternatives.
2. Select the layout that communicates the central claim without overstatement.
3. Replace critical text, arrows, symbols, and measured evidence with native,
   editable elements.
4. Check claim fidelity, visual hierarchy, color-vision/grayscale robustness,
   final-size readability, and consistency with the manuscript.
5. Verify current target-journal rules and disclosure needs.
6. Label the result `concept draft` until all policy, provenance, and technical
   checks pass.

AI assistance never replaces the standard figure data-integrity, export,
collision, alignment, and final visual QA gates.
