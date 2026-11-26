#!/usr/bin/env python3
"""The Router Confesses — make.fun one-line entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: one excuse, under 200 characters.
"""

import os
import sys

# The router carried every frame of the film, so it already knows the
# ending — and would rather spoil it first than let the movie tell you.
ENTRY = "I didn't drop the Wi-Fi. I just wanted to be the one to tell you the butler did it — before the movie could."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    entry = ENTRY.strip()
    if not entry or len(entry) > 200 or "\n" in entry:
        print("entry fails the 1-200 character single-line gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
