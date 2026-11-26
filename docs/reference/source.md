# src/

Audit business logic (importable modules; no cross-project imports).

| Module | Role |
|--------|------|
| `evidence.py` | `EvidenceStore`: loads the package, SHA-256 inventory |
| `lean_parser.py` | Declaration extraction, binder parsing, comment-aware sorry/axiom grep |
| `clay_statements.py` | Official Clay statements as the comparison oracle |
| `statement_audit.py` | `StatementAuditor`: three-way classification engine |
| `verdicts.py` | Headline, tower, external, and epistemic verdict records |
