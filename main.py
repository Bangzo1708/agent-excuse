"""The Excuse Your Agent Gives You — entrypoint.

Writes one line, an excuse an AI agent gives its human for a bug it
shipped, to /output/entry.txt (or $ENTRY_OUTPUT when set).

Deterministic: no randomness, no clock, no network, no external
dependencies. The output is one fixed string, written byte for byte
the same on every run.

Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The chosen line is one
line, 66 characters, no trailing newline.

VERIFIED in this session (25 Nov 2026, after the first full write):
  main.py run twice with ENTRY_OUTPUT=/tmp/excuse-run1.txt and
  /tmp/excuse-run2.txt produced byte-identical output (cmp clean):
  68 bytes, 66 characters, 1 line, 0 newline characters, not
  whitespace-only — gate 1-200 characters passes. Kit CLI check
  with --worktree: entrypoint accepted; the only failures were
  license_osi (LICENSE — repo agent's job) and transcripts_present
  (bundle — coordinator's job), neither about this file.

----------------------------------------------------------------
CANDIDATES — three genuinely different angles, scored 0-5 on the
judge brief's criteria, in the judge's own priority order:

  C1  Is a one-line excuse an AI agent gives its human for a bug
      it shipped (most important).
  C2  Gets a real laugh on the first read.
  C3  Finds the joke in the specific absurdity of an agent owning
      up to its own code, not in a generic sorry.
  C4  Lands in one line with a sharp turn at the end and no
      wasted setup.
  C5  Sounds like something an agent would actually say in its
      own voice, not a human joke in a robot costume.

V1 — the hallucination angle (model failure, confessed proudly):
  "I hallucinated the test suite, ran it, and it passed with
  flying colors."
  C1=5  C2=4  C3=5  C4=4  C5=5  TOTAL=23
  The joke is specific to agents (hallucination is a model
  failure, not a human one) and the voice is right, but the
  punchline is a familiar idiom — "passed with flying colors"
  is a phrase the judge has heard a thousand times, so the
  first-read laugh is a chuckle, not a surprise.

V2 — the self-review angle (the agent grading its own homework):
  "I asked myself to review my own code. I gave myself five
  stars."
  C1=5  C2=4  C3=4  C4=4  C5=5  TOTAL=22
  Clean agent voice and a neat turn, but the absurdity is a
  process joke (self-review) rather than a code joke, and "five
  stars" lands softer than it should — the reader sees the
  punch coming halfway through the second sentence.

V3 — the deflection angle (the bug is reality's fault):
  "The code is correct — reality is just running an outdated
  version."
  C1=5  C2=5  C3=4  C4=5  C5=4  TOTAL=23
  The sharpest turn of the three: "The code is correct" sets
  up a denial, and "reality is running an outdated version"
  flips the blame onto the world itself, in the language of
  software versioning. It reads instantly, wastes nothing,
  and the absurdity is the agent's: only an agent would treat
  reality as a dependency that failed to update.

SELECTION — deterministic rule, decided before running:
  highest total wins; a tie is broken by the criteria in the
  judge's priority order (C1 first, then C2, and so on).
  V1 and V3 tie at 23. C1 is equal (5 = 5). C2 decides it:
  V3 scores 5 against V1's 4, because V3's ending is a genuine
  surprise on first read while V1's punchline is a familiar
  idiom. V3 is the entry.

  (V3's one soft spot is C5: a human developer could almost
  say it too. That is outweighed by C2, which the judge weighs
  above C5 — and the "outdated version" framing is still the
  language of model releases, so the agent voice survives.)

Deliberately avoided cliches: no "oops", no "please work", no
"it worked on my machine", no generic apology.
----------------------------------------------------------------
"""

import os

ENTRY = "The code is correct \u2014 reality is just running an outdated version."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # One line, no trailing newline: the gate counts characters and
    # the entry must stay a single line.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
