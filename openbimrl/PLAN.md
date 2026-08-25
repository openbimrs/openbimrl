# Alias package plan

Status: exact-version alias prepared; publication not authorized.
Last updated: 2026-08-25

## Permanent boundary

- [x] Depend only on `openbim-openbimrl = "=0.1.0"`.
- [x] Re-export the canonical crate without defining an item.
- [x] Enforce the boundary with the semantic alias-purity checker.
- [ ] Verify the complete alias package only after the exact canonical release
      exists on crates.io.
- [ ] Publish only after separate, explicit authorization and only after the
      canonical package release succeeds.

Implementation never belongs in this package.
