# OpenBIM.rs openBIMRL namespace

[![CI](https://github.com/openbimrs/openbimrl/actions/workflows/ci.yml/badge.svg)](https://github.com/openbimrs/openbimrl/actions/workflows/ci.yml)
[![openbim-openbimrl](https://img.shields.io/crates/v/openbim-openbimrl.svg)](https://crates.io/crates/openbim-openbimrl)
[![openbimrl](https://img.shields.io/crates/v/openbimrl.svg)](https://crates.io/crates/openbimrl)
[![docs.rs](https://docs.rs/openbim-openbimrl/badge.svg)](https://docs.rs/openbim-openbimrl)
[![MSRV](https://img.shields.io/badge/MSRV-1.85-blue)](https://www.rust-lang.org)

This repository is a **RESERVED OpenBIM.rs namespace candidate**. It preserves
package architecture for the names `openbim-openbimrl` and `openbimrl`; it does
not establish or implement a technology called openBIMRL.

No authoritative specification was established for this repository. It is not
affiliated with, endorsed by, or acting for any standards body, industry
alliance, or other organization. The name alone must not be read as a parser,
language, serializer, schema, conformance, or validation claim.

## Capability status

| Capability | Status |
| --- | --- |
| Repository and package-name reservation candidate | Present locally; not published by this repository state |
| Stable `PACKAGE_STATUS` constant | Present |
| Parser or decoder | Not claimed; not implemented |
| Language or data model | Not claimed; not implemented |
| Serializer or encoder | Not claimed; not implemented |
| Schema or validation | Not claimed; not implemented |
| Standards conformance | Not claimed; no authoritative specification established |

## Package architecture

| Package | Role |
| --- | --- |
| [`openbim-openbimrl`](openbim-openbimrl/) | Canonical namespace package; owns the minimal status API |
| [`openbimrl`](openbimrl/) | Exact-version, pure re-export alias; defines no independent API |

Cargo does not provide publisher-side aliases on crates.io, so the two package
records are modeled explicitly. The alias has one dependency, pinned to
`=0.1.0`, and its source contains only:

```rust
pub use openbim_openbimrl::*;
```

See [`docs/architecture.md`](docs/architecture.md) for the enforced boundary.

## Install

These commands are the intended post-publication forms; this repository does
not publish either package:

```bash
cargo add openbim-openbimrl@0.1.0
# or
cargo add openbimrl@0.1.0
```

Use one package name, not both. Both expose the same canonical item:

```rust
assert!(openbim_openbimrl::PACKAGE_STATUS.starts_with("RESERVED "));
// With the alias dependency, use `openbimrl::PACKAGE_STATUS` instead.
```

## Development

Rust `1.85.0` and Python `3.10` or newer are required.

```bash
git clone https://github.com/openbimrs/openbimrl.git
cd openbimrl
CARGO_TARGET_DIR=/mnt/backup/build-cache/openbimrl ./scripts/gate.sh
```

The gate verifies formatting, check/build/test, Clippy, rustdoc, semantic alias
purity, the canonical package, and the alias file list. Alias package
verification is intentionally limited to `cargo package --list` until the exact
canonical version exists on crates.io.

## Contributing and license

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Licensed under the MIT License; see
[`LICENSE`](LICENSE).
