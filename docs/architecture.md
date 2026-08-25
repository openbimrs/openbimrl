# Architecture

## Repository role

`openbimrs/openbimrl` is a standalone repository for reserving two
OpenBIM.rs Rust package names. The string openBIMRL is treated as a namespace
label only. No authoritative specification was established, no standards-body
or organizational affiliation is asserted, and no implementation capability
is inferred from repository or package existence.

## Package identity

```text
openbimrl  -- exact =0.1.0 dependency -->  openbim-openbimrl
(alias; no items)                          (minimal status API)
```

Cargo supports dependency renaming for consumers but has no crates.io
publisher-side alias facility. Two package records are therefore needed to
represent both desired names. Every public item originates in the canonical
package; the alias source contains comments plus exactly:

```rust
pub use openbim_openbimrl::*;
```

The exact version requirement prevents alias and canonical releases from
silently drifting. `scripts/check_alias_purity.py` verifies package versions,
dependency shape, target shape, source path, and the sole meaningful source
line using Cargo metadata rather than filename heuristics alone.

## Capability boundary

The canonical package is dependency-free and exports only `PACKAGE_STATUS`.
That item communicates reservation status; it is not a file-format, grammar,
language, model, parsing, encoding, validation, or conformance API.

Any future implementation proposal first needs independently verified authority,
provenance, legal artifact handling, explicit scope, tests, and corrected
capability documentation. None is claimed to exist now.

## Standalone release metadata

Each publishable manifest explicitly declares package name, version, Rust 2021
edition, MSRV 1.85, MIT license, author, repository, homepage, documentation,
README, description, keywords, category, and publish intent. The packages do
not inherit release metadata from another workspace.

The release order, if separately authorized, is:

1. verify and publish `openbim-openbimrl`;
2. wait for crates.io indexing;
3. verify and publish the exact-version `openbimrl` alias.

Repository CI does not perform publication. The steady-state gate fully packages
and verifies both crates.

## Artifact policy

Standards texts, schemas, copied examples, and other third-party artifacts are
outside this repository's established scope and must remain absent. A future
proposal requires provenance and redistribution review before adding any such
material.
