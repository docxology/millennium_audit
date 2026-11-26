# Reproduce the audit

## Source checks

Use uv and Python 3.11 or newer. Run these commands from a clean checkout.

```sh
uv sync --locked
uv run --locked python scripts/run_audit.py --output output/current-audit-report.json
uv run --locked python scripts/check_quotations.py
uv run --locked pytest
```

The source runner reads `package/MillenniumLean/` by default. The command
above saves its report independently of the reference report under `data/`.
Use a positional package path and `--output` to audit another copy. An
alternate package with no explicit output writes `output/alternate-audit-report.json`.

The quotation checker defaults to the archived ZIP, which retains the
published line positions. The working copy uses the Lean and mathlib revisions
in its own toolchain and lock metadata. The published [build receipt](../data/BUILD_RECEIPT.md)
records the run against the original archive. [Evidence package](reference/evidence-package.md)

## Render the manuscript

Install Pandoc and XeLaTeX with the packages listed in Template's run guide.
Create a detached render worktree under the pinned Template project tree.
This keeps generated output and the published PDF in separate checkouts.

```sh
audit_project="$(pwd -P)"
git clone https://github.com/docxology/template.git ../millennium-template
git -C ../millennium-template checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
cd ../millennium-template
uv sync --locked --no-dev
mkdir -p projects/working
git -C "$audit_project" worktree add --detach "$PWD/projects/working/millennium_audit" HEAD
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/millennium_audit
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/millennium_audit
```

Open `output/pdf/millennium_audit_combined.pdf` and `output/web/index.html`
in the detached render worktree. Check the numbered sections, per-problem findings and
bibliography. Validation and provenance reports are written under `output/reports/`.
The committed versioned PDF remains the publication snapshot. [Published audit](https://doi.org/10.5281/zenodo.22243473)
