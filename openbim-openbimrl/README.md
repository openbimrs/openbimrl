# openbim-openbimrl

Canonical package for a **RESERVED OpenBIM.rs namespace** associated with the
name openBIMRL.

## Status

Version `0.1.1` provides only `PACKAGE_STATUS`. No authoritative specification
was established for this crate, and it does not claim or provide a parser,
language, data model, encoder, schema, validator, or conformance implementation.

This package is not affiliated with, endorsed by, or acting for any standards
body, industry alliance, or other organization.

## Package relationship

`openbim-openbimrl` owns the status API. The sibling
[`openbimrl`](https://crates.io/crates/openbimrl) package is an exact-version
pure re-export alias and owns no independent API.

## Usage

Install the canonical package:

```bash
cargo add openbim-openbimrl@0.1.1
```

```rust
assert!(openbim_openbimrl::PACKAGE_STATUS.starts_with("RESERVED "));
```

## License

`AGPL-3.0-or-later OR LicenseRef-Commercial`; a commercial licence is
available from the copyright holder named in `NOTICE`.
