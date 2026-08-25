# OpenBIM.rs openBIMRL reservation

Read `AGENTS.md` and the nearest nested `AGENTS.md` before editing. This is a
standalone reservation repository, not an implementation repository.

## Verification

Run `./scripts/gate.sh`; trust process exit codes.

## Conventions

- Rust 2021; MSRV 1.85; pinned local/CI toolchain 1.85.0.
- MIT; explicit package metadata; no workspace-inherited release metadata.
- `openbim-openbimrl` owns the minimal status API.
- `openbimrl` is an exact-version pure re-export and defines nothing.
- No authoritative specification or standards-body affiliation is claimed.
- Do not add standards artifacts, implementation claims, or publication steps
  without separate provenance, evidence, and explicit authorization.
