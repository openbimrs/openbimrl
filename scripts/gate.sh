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
scripts/test-alias-purity.sh
python3 scripts/check-package-contents.py
cargo package --locked -p openbim-openbimrl
cargo package --locked -p openbimrl
