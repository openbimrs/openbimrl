#!/usr/bin/env bash
# Complete standalone verification gate for openbimrs/openbimrl.
set -euo pipefail

cd "$(dirname "$0")/.."

cargo fmt --all -- --check
cargo check --workspace --all-targets --all-features
cargo build --workspace --all-targets
cargo test --workspace --all-features
cargo clippy --workspace --all-targets --all-features -- -D warnings
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps
scripts/check-alias-purity.sh
cargo package -p openbim-openbimrl
# Full alias verification requires openbim-openbimrl =0.1.0 in crates.io.
cargo package --list -p openbimrl
