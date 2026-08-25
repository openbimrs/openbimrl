# openBIMRL reservation repository instructions

This standalone repository reserves OpenBIM.rs package architecture only. No
authoritative openBIMRL specification has been established here. Do not imply a
parser, language, schema, validator, standards conformance, or affiliation with
any standards body or organization.

## Map

- `openbim-openbimrl/` — canonical namespace and all public items
- `openbimrl/` — exact-version pure re-export alias
- `docs/` — architecture and maintained documentation
- `scripts/gate.sh` — complete local and CI verification
- `scripts/check_alias_purity.py` — semantic package-boundary checker

## Required commands

```bash
./scripts/gate.sh
cargo package -p openbim-openbimrl
cargo package -p openbimrl
```

The canonical package must be released before its exact-version alias. Never
push or publish unless that action is separately and explicitly authorized.

## Boundaries

- Both packages use Rust 2021, MSRV 1.85, version 0.1.0, and explicit metadata.
- `openbim-openbimrl` is dependency-free and owns every public item.
- `openbimrl/src/lib.rs` contains comments plus only
  `pub use openbim_openbimrl::*;`.
- The alias depends only on exact version `=0.1.0` of the canonical package.
- Keep standards and other third-party artifacts out of the repository.
- Capability documentation must distinguish reservation from implementation.
