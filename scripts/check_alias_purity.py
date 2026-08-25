#!/usr/bin/env python3
"""Fail closed unless `openbimrl` is a pure alias of `openbim-openbimrl`."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, NoReturn

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_NAME = "openbim-openbimrl"
ALIAS_NAME = "openbimrl"


def fail(message: str) -> NoReturn:
    print(f"alias purity: {message}", file=sys.stderr)
    raise SystemExit(1)


def one_package(packages: list[dict[str, Any]], name: str) -> dict[str, Any]:
    matches = [package for package in packages if package["name"] == name]
    if len(matches) != 1:
        fail(f"expected exactly one {name!r} package, found {len(matches)}")
    return matches[0]


def normalized(path: str | Path) -> Path:
    return Path(path).resolve()


result = subprocess.run(
    ["cargo", "metadata", "--no-deps", "--format-version", "1"],
    cwd=ROOT,
    check=True,
    capture_output=True,
    text=True,
)
metadata: dict[str, Any] = json.loads(result.stdout)
packages: list[dict[str, Any]] = metadata["packages"]
workspace_names = {
    package["name"]
    for package in packages
    if package["id"] in metadata["workspace_members"]
}
expected_names = {CANONICAL_NAME, ALIAS_NAME}
if workspace_names != expected_names:
    fail(
        "workspace packages must be exactly "
        f"{sorted(expected_names)!r}, got {sorted(workspace_names)!r}"
    )

canonical = one_package(packages, CANONICAL_NAME)
alias = one_package(packages, ALIAS_NAME)
canonical_version = canonical["version"]
if alias["version"] != canonical_version:
    fail(
        f"package versions differ: {ALIAS_NAME}={alias['version']}, "
        f"{CANONICAL_NAME}={canonical_version}"
    )

expected_manifest = normalized(ROOT / "openbimrl/Cargo.toml")
if normalized(alias["manifest_path"]) != expected_manifest:
    fail(f"alias manifest must be {expected_manifest}")
if alias.get("features"):
    fail("alias must not define features")
if alias.get("links") is not None:
    fail("alias must not define a native links contract")

if len(alias["targets"]) != 1:
    fail("alias must contain exactly one Cargo target")
target = alias["targets"][0]
if target["kind"] != ["lib"] or target["crate_types"] != ["lib"]:
    fail("alias's only target must be a normal library")
if target["name"] != "openbimrl":
    fail(f"alias target has unexpected name {target['name']!r}")

source_path = normalized(target["src_path"])
expected_source = normalized(ROOT / "openbimrl/src/lib.rs")
if source_path != expected_source:
    fail(f"alias library must be {expected_source}, got {source_path}")
meaningful_lines = [
    line.strip()
    for line in source_path.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("//")
]
expected_reexport = "pub use openbim_openbimrl::*;"
if meaningful_lines != [expected_reexport]:
    fail(f"alias library must contain only `{expected_reexport}` apart from comments")

if len(alias["dependencies"]) != 1:
    fail(f"alias must have exactly one dependency, found {len(alias['dependencies'])}")
dependency = alias["dependencies"][0]
if dependency["name"] != CANONICAL_NAME or dependency.get("rename") is not None:
    fail(f"alias's sole dependency must be unrenamed {CANONICAL_NAME}")
if dependency.get("kind") is not None or dependency.get("optional"):
    fail("canonical package must be a required normal dependency")
expected_requirement = f"={canonical_version}"
if dependency["req"] != expected_requirement:
    fail(
        f"canonical requirement must be {expected_requirement}, "
        f"got {dependency['req']}"
    )
expected_path = normalized(ROOT / "openbim-openbimrl")
if dependency.get("path") is None:
    fail("canonical dependency must have a local path for workspace verification")
if normalized(dependency["path"]) != expected_path:
    fail(f"canonical dependency path must be {expected_path}")

print(
    f"alias purity: ok ({ALIAS_NAME} is an exact-version pure re-export of "
    f"{CANONICAL_NAME} {canonical_version})"
)
