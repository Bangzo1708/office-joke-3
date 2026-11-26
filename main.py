#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head -- round 3 (final).

Writes one office joke, a single line, to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline), validated to 1-200 characters.

Three candidates, scored 0-5 on the judge's five criteria, in priority order:
  1. one-line office joke, setup + turn
  2. turns on something every office worker knows
  3. surprises, unexpected turn, not a plain complaint
  4. every word earns its place, punchline last
  5. feels new, not a joke already going round

Candidate A -- printer angle:
  "The printer only jams on deadline day, so IT gave it Employee of the
  Month for reliability." (91 chars)
  Scores: 5 / 5 / 4 / 4 / 3 = 21
  - (1) clean setup + turn, one line; (2) the printer jamming on
    deadline day is literally the judge brief's own example; (3) Employee
    of the Month for reliability is a real ironic twist; (4) tight,
    though "so IT gave it" is slightly flat; (5) printer jokes circulate
    widely, only the award twist is fresh.

Candidate B -- "per my last email" angle:
  "I wrote 'per my last email' so politely that HR asked me to teach a
  course in passive aggression." (97 chars)
  Scores: 5 / 5 / 4 / 4 / 3 = 21
  - (1) setup + turn, one line; (2) "per my last email" is universal
    office language; (3) HR asking for a masterclass is a good turn;
    (4) tight; (5) the phrase itself is heavily memed, so it feels
    familiar rather than new.

Candidate C -- IT "turn it off and on again" angle:
  "IT always asks if I tried turning it off and on again, so I asked
  them about my career." (87 chars)
  Scores: 5 / 4 / 5 / 5 / 4 = 23
  - (1) setup + turn, one line; (2) IT's first question is known to
    every office worker; (3) applying the reboot fix to a career is a
    genuinely unexpected turn; (4) every word earns its place, punchline
    ("about my career") last; (5) the career application feels new.

Winner: Candidate C (23, clear of A and B at 21 each).
"""

import os

JOKE = "IT always asks if I tried turning it off and on again, so I asked them about my career."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = JOKE
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    # Create the output dir if a fresh run dir is used; never touch its mode.
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
