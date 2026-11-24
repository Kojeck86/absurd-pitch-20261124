"""Entry for make.fun bounty u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.

Writes one single-sentence pitch for an absurd invention to
/output/entry.txt. Standard library only; deterministic: the same
line every run.

The pitch: the Farewell Charger, which at 1% battery texts your
group chat that you died bravely mid-sentence, so nobody ever
expects a reply again — the dead-phone problem solved by a
dramatic exit. 135 characters, one sentence, inside the
1-220 gate. The laugh comes from the invention itself — a charger
that solves the dead-phone annoyance by faking your death — and
the fix is silly yet weirdly plausible: no reply is ever owed.
"""

import os

LINE = (
    "The Farewell Charger: at 1% battery, it texts your group chat "
    "that you died bravely mid-sentence, so nobody ever expects a "
    "reply again."
)


def main():
    # Gate: 1-220 characters, one sentence, no trailing newline.
    if not 1 <= len(LINE) <= 220:
        raise ValueError("entry line must be 1-220 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
