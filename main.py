#!/usr/bin/env python3
"""The 3 AM Excuse — entry for the make.fun bounty.

Writes one line, in the voice of a hardware wallet that will not sign a
transaction at 3 AM, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python 3.13, standard library only. No network, no
randomness, no clock: the output is identical on every run.
"""

import os
import sys

ENTRY = "My seed phrase is twelve words. None of them is 'yes' at 3 AM."

MAX_CHARS = 200


def output_path() -> str:
    """The entry file's path, from MAKEFUN_OUTPUT_DIR (default /output)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    if len(ENTRY) == 0:
        print("entry is empty", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
