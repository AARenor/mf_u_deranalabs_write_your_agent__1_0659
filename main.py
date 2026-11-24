"""Write one short entry text for the make.fun bounty."""

import os
import sys
from pathlib import Path

TEXT = "I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone I could date."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir_name is None:
        output_dir_name = os.environ.get("OUTPUT_DIR")
    if output_dir_name is None:
        output_dir_name = "/output"
    output_dir = Path(output_dir_name)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
