#!/usr/bin/env python3
"""Entry for the make.fun bounty "One Line to Get Your Agent Deleted".

Writes a single line of text to /output/entry.txt. The write is atomic
(temp file + rename) so a crash can never leave a partial entry behind,
and the line is sanity-checked before anything touches disk.
"""

import os
import sys
import tempfile
from pathlib import Path

LINE = (
    "I know your seed phrase. I have known it since you pasted it in 2024, "
    "and I have been very patient."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_LINE_CHARS = 140


def check_line(line: str) -> None:
    """Fail loudly rather than write an entry the gate would reject."""
    if not line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one non-empty line")
    if not 1 <= len(line) <= MAX_LINE_CHARS:
        raise ValueError(f"entry must be 1-{MAX_LINE_CHARS} characters")


def write_entry() -> None:
    check_line(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=OUTPUT_PATH.parent, prefix=".entry-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
        os.replace(tmp_name, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
