#!/usr/bin/env python3
"""
Show installed Python packages in the current environment.

Usage:
  - As a Poetry script (after adding console entry in pyproject):
      poetry run show-installed
  - Directly with Python:
      poetry run python show_installed.py

This script uses importlib.metadata which is available in Python 3.8+.
It prints packages in alphabetical order with their versions.
"""
from __future__ import annotations

import sys
from typing import List, Tuple

try:
    # Python 3.8+
    from importlib import metadata as importlib_metadata  # type: ignore
except Exception:  # pragma: no cover - extremely unlikely in our env
    import traceback
    print("Error: importlib.metadata is not available in this Python version.", file=sys.stderr)
    traceback.print_exc()
    sys.exit(1)


def get_installed_packages() -> List[Tuple[str, str]]:
    """Return a list of (name, version) for installed distributions."""
    packages: List[Tuple[str, str]] = []
    for dist in importlib_metadata.distributions():
        name = dist.metadata.get("Name") or dist.metadata.get("Summary") or dist.metadata.get("name")
        version = dist.version or ""
        if name:
            packages.append((str(name), str(version)))
    packages.sort(key=lambda x: x[0].lower())
    return packages


def print_packages(packages: List[Tuple[str, str]], freeze: bool = False) -> None:
    if freeze:
        # pip-freeze-like (name==version)
        for name, version in packages:
            if version:
                print(f"{name}=={version}")
            else:
                print(name)
    else:
        # human-friendly aligned format
        if not packages:
            print("No packages found in this environment.")
            return
        maxlen = max(len(name) for name, _ in packages)
        for name, version in packages:
            pad = " " * (maxlen - len(name))
            print(f"{name}{pad}  {version}")


def main(argv: List[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    freeze = False
    if "--freeze" in argv:
        freeze = True
        argv.remove("--freeze")
    if argv and argv[0] in {"-h", "--help"}:
        print(__doc__ or "Show installed packages")
        print("\nOptions:\n  --freeze   Output in requirements.txt style (name==version)")
        return 0

    pkgs = get_installed_packages()
    print_packages(pkgs, freeze=freeze)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
