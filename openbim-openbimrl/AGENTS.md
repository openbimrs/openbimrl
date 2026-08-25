# Canonical package instructions

Purpose: own the minimal API for the reserved `openbim-openbimrl` package.

Follow `../AGENTS.md` and read `PLAN.md` before changing this package.

## Boundary

- Keep this package dependency-free while it remains a reservation.
- `PACKAGE_STATUS` must make the reserved/no-specification state explicit.
- Do not add parser, language, model, encoding, validation, or conformance APIs
  without first satisfying and documenting the plan preconditions.
- Do not imply standards-body or organizational affiliation.
- Run `../scripts/gate.sh` from any working directory before committing.
