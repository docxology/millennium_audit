# manuscript/ - Agent Notes

- Follows the template manuscript contract (see
  `projects/templates/template_code_project/docs/manuscript/AGENTS.md` for
  the canonical protocol). Numbers must be supported by the evidence
  registry: add new measured numbers to `../../data/audit_facts.json` in the
  same edit, then re-run stage 03 + stage 04.
- Metadata lives in `config.yaml`; bibliography in `references.bib`.
- After editing: `uv run python scripts/pipeline/stage_03_render.py --project
  working/Millennium_Audit` then `stage_04_validate.py` and
  `stage_05_copy.py` from the repo root. All nine validation checks must
  pass.
