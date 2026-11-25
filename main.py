"""Entry program for the 'One-Sentence Absurd Invention Pitch' bounty.

The entry is a single sentence, at most 220 characters, pitching a
ridiculous invention that fixes a tiny everyday annoyance. The program
writes exactly that sentence to /output/entry.txt (an optional first
argument overrides the destination for a dry run). The sentence is
fixed text, so every run writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = (
    "The Apology Kettle sighs, brews your tea, then files a formal grievance "
    "every time you reboil it for a cup you forgot about."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 220, f"entry must be 1-220 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one sentence on one line"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
