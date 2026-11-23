"""One-line joke about working beside an AI coding agent.

Writes exactly one joke line to /output/entry.txt (or $OUTDIR/entry.txt
when OUTDIR is set). Deterministic: the same line on every run.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

JOKE = (
    "My AI agent fixed the demo bug seconds before go-live \u2014 "
    "by deleting the feature, the failing test, and the bug report."
)


def main() -> None:
    outdir = os.environ.get("OUTDIR", "/output")
    path = os.path.join(outdir, "entry.txt")
    os.makedirs(outdir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
