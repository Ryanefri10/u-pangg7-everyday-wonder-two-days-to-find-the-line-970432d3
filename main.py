# u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3
# One sentence, at most 200 characters, on a small moment of wonder in
# everyday life. Writes exactly one text to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt). Python 3.13, stdlib only, no network.
import os
from pathlib import Path

TEXT = (
    # One concrete image: a cracked phone screen doubling the moon.
    # The surprise is the turn itself -- the night suddenly has a spare --
    # grounded in two ordinary things (a damaged screen, the moon) and
    # landing in a single read, with no filler and no worn phrase.
    "My cracked phone screen splits the moon in two, "
    "and tonight the sky has a spare."
)

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "entry.txt"

# Guard the gate in code, not just by inspection: the sealed scorer refuses
# any text outside 1-200 characters, so refuse to write an invalid one.
if not 1 <= len(TEXT) <= 200:
    raise SystemExit(f"entry is {len(TEXT)} characters, must be 1-200")
if TEXT.count(".") != 1 or not TEXT.strip():
    raise SystemExit("entry must be one non-blank sentence")
out_path.write_text(TEXT, encoding="utf-8")
print(f"wrote {len(TEXT)} characters to {out_path}")
