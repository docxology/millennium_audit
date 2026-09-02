# Independent Lean Kernel Reproduction Receipt (completed)

Environment (this audit session):
- elan toolchain: leanprover/lean4:v4.34.0-rc1 (installed from lean-toolchain pin)
- mathlib: pinned revision d0be1efe9afff6119115373bf4ea5abd833b3a95
  (from lake-manifest.json), shallow-cloned, verified; prebuilt oleans restored
  via `lake exe cache get` (8711 files, exit 0)
- Reproduction workspace: /tmp/millennium_repro with the package's six
  source/config files verbatim and dependency symlinks into the pinned mathlib
  checkout

Verbatim results:

  lake build Tower Millennium
    Build completed successfully (8730 jobs).
    BUILD_EXIT=0

  lake env lean print_axioms.lean   AXIOMS_EXIT=0
  'Millennium.riemannHypothesis_of_selfAdjoint_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]
  'Millennium.yang_mills_gap' depends on axioms: [propext, Classical.choice, Quot.sound]
  'Millennium.ns_official' depends on axioms: [propext, Classical.choice, Quot.sound]
  'Millennium.hodge_kunneth' depends on axioms: [propext]
  'Millennium.bsd_official' depends on axioms: [propext, Classical.choice, Quot.sound]
  'Millennium.P_neq_NP_of_proof_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]

Conclusion: the package's KERNEL claims are REPRODUCED VERBATIM - clean build,
no sorry, no project axiom, footprints in {propext, Classical.choice,
Quot.sound}. This confirms build hygiene ONLY. It does not and cannot rescue
conditional premises, defs of open statements, or the trivial tower invariant
(Tower.lean:11 declInv n := 0 < n + 1). Axiom-freedom of `0 < n + 1` is
expected, not evidential. See STATEMENT_EVIDENCE.md for the per-problem gaps.
