# Changelog

All notable changes to this project are documented in this file. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-10-28

### Changed

- **Licence:** `AGPL-3.0-or-later OR LicenseRef-Commercial` (was `MIT` in
  0.1.0); a commercial licence is available from the copyright holder named in
  `NOTICE`. See `LICENSING.md`. Historical releases remain under their
  published MIT terms, and third-party material retains its own terms. Both
  packages ship `LICENSE`, `NOTICE` and `LICENSES/LicenseRef-Commercial.txt`.
- Raise MSRV to Rust 1.99.
- The steady-state release gate now fully packages the published `openbimrl`
  alias.
- Alias purity now fails closed over Cargo dependency, feature, target, build,
  and source shape, with 19 mutation probes and exact package allowlists.
- CI now pins its runner and action revisions.
- Updated the alias plan to reflect the verified `0.1.0` publication rather
  than the obsolete pre-authorization state.

## [0.1.0] - 2026-08-25

### Added

- Reserved the canonical [`openbim-openbimrl`][canonical-crate] package
  architecture with an explicit status constant.
- Added the exact-version, pure re-export `openbimrl` alias package.
- Added standalone CI, packaging, documentation, and mutation-verified
  alias-purity gates.
- Documented that no authoritative specification, implementation capability,
  standards-body affiliation, or publication is claimed by this repository
  namespace.

[0.1.1]: https://crates.io/crates/openbim-openbimrl/0.1.1
[0.1.0]: https://crates.io/crates/openbim-openbimrl/0.1.0
[canonical-crate]: https://crates.io/crates/openbim-openbimrl/0.1.0
