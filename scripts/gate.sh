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
cargo package --locked -p openbim-openbimrl -p openbimrl

# Both packages are `AGPL-3.0-or-later OR LicenseRef-Commercial`: each archive
# ships byte-identical copies of the root licence texts and notice.
target="$(cargo metadata --format-version 1 --no-deps | python3 -c 'import json,sys; print(json.load(sys.stdin)["target_directory"])')"
for package in openbim-openbimrl openbimrl; do
  version="$(cargo metadata --format-version 1 --no-deps \
    | PACKAGE="$package" python3 -c 'import json,os,sys; print(next(p["version"] for p in json.load(sys.stdin)["packages"] if p["name"]==os.environ["PACKAGE"]))')"
  package_root="$target/package/$package-$version"
  for f in LICENSE NOTICE LICENSES/LicenseRef-Commercial.txt; do
    cmp -s "$f" "$package_root/$f" || {
      echo "packaged $package: $f is missing or differs from the root" >&2
      exit 1
    }
  done
  grep -qx 'license = "AGPL-3.0-or-later OR LicenseRef-Commercial"' "$package_root/Cargo.toml" || {
    echo "packaged $package: unexpected license expression" >&2
    exit 1
  }
done
