# F19 - `Promote.tower_closes` proves whatever target the provider declares (rebuttal pass)

## Claim under audit

Package comment (Millennium.lean:337-341) claims the PROMOTE kernel "replaces the trivial
`declInv n := 0<n+1` with mathematical content … Every field carries content — none is `0<n+1`.
This is Denis's Layer-3 PROMOTE interface."

Rebuttal comment (consistent with this audit's F02): "Tower.declInv and the generic Tower.universal
induction are not what close the six Clay statements."

## Verbatim quotation

> 354: structure PromotableTower (X : Nat → Type u) (P : (n : Nat) → X n → Prop)
> 355:     (A : Type u) [TopologicalSpace A] extends CertifiedLevel X P where
> 356:   embed        : (n : Nat) → X n → A
> 357:   control        : A → ℝ
> 358:   uniformBound   : ∃ C, ∀ n, control (embed n (value n)) ≤ C            -- Law 4: uniform control
> 359:   Pinf           : A → Prop
> 360:   OfficialTarget : Prop
> 361:   converges      : ∃ x, Filter.Tendsto (fun n => embed n (value n)) Filter.atTop (nhds x) -- Law 5

> 376: theorem tower_closes {X : Nat → Type u} {P : (n : Nat) → X n → Prop} {A : Type u}
> 377:     [TopologicalSpace A] (T : PromotableTower X P A) : T.OfficialTarget := by
> 378:   obtain ⟨x, hx⟩ := T.converges
> 379:   exact T.targetFidelity x (T.limitSound x T.certificate T.compatible T.uniformBound hx)

(Millennium.lean:354-361, 376-379.)

## Probe actually run (2026-09-04, exit 0)

A junk tower over `Unit` whose fields are all trivial and whose `OfficialTarget := (0:ℕ) < 1`:

```lean
def junkTower : Promote.PromotableTower (fun _ => Unit) (fun _ _ => True) Unit where
  value := fun _ => ();      certificate := fun _ => trivial
  restrict := fun _ _ => (); compatible := fun _ => rfl
  embed := fun _ _ => ();    control := fun _ => 0
  uniformBound := ⟨0, fun _ => le_refl 0⟩
  Pinf := fun _ => True;     OfficialTarget := (0 : ℕ) < 1
  converges := ⟨(), by simpa using tendsto_const_nhds (a := ())⟩
  limitSound := fun _ _ _ _ _ => trivial
  targetFidelity := fun _ _ => Nat.succ_pos 0
theorem junk_target : (0 : ℕ) < 1 := Promote.tower_closes junkTower
#print axioms junk_target
```

Kernel output:

```
'junk_target' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Fair analysis

- The rebuttal is right that the generic tower machinery is not load-bearing — that has been this
  audit's F02 all along. The deepening: the package's own "corrected" replacement (built, per its
  comment, as "Denis's Layer-3 PROMOTE interface") has the same defect one level up. All seven
  "laws" are provider-written fields; with `Pinf` and `OfficialTarget` chosen by the provider,
  `limitSound` and `targetFidelity` are satisfied trivially and `tower_closes` proves whatever is
  declared. Uniform control (Law 4) and convergence (Law 5) become vacuous when `embed` is constant.
- Content can only enter through a mathematically faithful instance: a real `X`/`P` (finite level
  data), a real `Pinf` (limit property), and `OfficialTarget` actually equal to a Clay statement.
  No such instance ships — for the same reason as F15/F16: the instance data would be the proof.
- So the audit's headline is unaffected by which universalization mechanism is called
  load-bearing: Tower.universal proves `0 < n+1` (F02); Promote.tower_closes proves any declared
  target (this finding). Both are plumbing, kernel-clean and content-free.

## Verdict

CONFIRMED (mechanism content-free). The rebuttal's dismissal of the tower as non-load-bearing is
correct and consistent with F02 — but the replacement mechanism proves arbitrary declared targets,
so the "supporting universalization structure" cannot be where the Clay content lives either.
