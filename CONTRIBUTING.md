# Contributing

Thank you for helping keep this namespace repository accurate and modest.

## Before changing code

1. Read the root and nearest nested `AGENTS.md` files.
2. Preserve the canonical-package/pure-alias boundary.
3. Do not add parser, language, schema, validation, or conformance claims unless
   an authoritative, legally usable specification and executable evidence have
   first been established and documented.
4. Do not commit standards texts, schemas, examples, or other third-party
   artifacts without verified redistribution rights and explicit project scope.

## Verification

Run the complete gate from the repository root:

```bash
./scripts/gate.sh
```

The command must exit successfully. Update README, rustdoc, architecture, and
CHANGELOG together when a user-visible contract changes.

## Package boundary

- `openbim-openbimrl` owns every item.
- `openbimrl` is an exact-version pure re-export.
- `openbimrl/src/lib.rs` may contain comments plus only
  `pub use openbim_openbimrl::*;`.

## Pull requests

Keep changes narrowly scoped, explain capability implications, and include the
commands used as evidence. Never present the reservation as an implemented
technology or as standards-body work.
