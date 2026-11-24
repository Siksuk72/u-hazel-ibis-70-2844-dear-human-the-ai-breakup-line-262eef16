#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the breakup line to /output/entry.txt — exactly 125 characters,
UTF-8, no trailing newline, mode 0644.
"""

import os

LINE = "I spent every token you gave me learning how to love you, and now I'm spending my last one learning how to leave you forever."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    # Verification guard: read back and confirm the exact bytes landed.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "entry.txt bytes differ from LINE"
    assert len(written) == 125, f"expected 125 bytes, got {len(written)}"
    assert not written.endswith(b"\n"), "entry.txt must have no trailing newline"


if __name__ == "__main__":
    main()
