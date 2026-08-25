# openbimrl

Exact-version pure re-export alias for
[`openbim-openbimrl`](https://crates.io/crates/openbim-openbimrl).

## Status

This package is part of a local **RESERVED OpenBIM.rs namespace candidate** and
has not been published by this repository state. It adds no API or capability.
The canonical package provides only a status constant and establishes no
parser, language, schema, validation, conformance, or standards-body claim.

## Usage

After both packages are published in canonical-then-alias order:

```bash
cargo add openbimrl@0.1.0
```

```rust
assert!(openbimrl::PACKAGE_STATUS.starts_with("RESERVED "));
```

Do not depend on both package names directly.

## License

MIT
