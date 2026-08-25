# Alias package instructions

Purpose: package-name alias for `openbim-openbimrl`.

Follow `../AGENTS.md` and read `PLAN.md` before changing this package.

## Boundary

The only non-comment source line permitted in `src/lib.rs` is:

```rust
pub use openbim_openbimrl::*;
```

Defining an item, feature, build script, test target, example, benchmark, or
additional dependency here is a defect. Keep the canonical dependency pinned
to the exact matching version. `../scripts/check-alias-purity.sh` enforces this
boundary semantically through Cargo metadata and source inspection.
