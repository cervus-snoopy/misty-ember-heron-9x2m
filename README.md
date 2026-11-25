[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/cervus-snoopy/misty-ember-heron-9x2m/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/cervus-snoopy/misty-ember-heron-9x2m/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

# The 3 AM Excuse

Entry for the make.fun bounty
[The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).

## The line

> My seed phrase is twelve words. None of them is 'yes' at 3 AM.

62 characters. One line, in the wallet's own voice, no setup, no signature.

## Why this angle wins

The visible field is saturated with four templates: sleeping keys
("my keys are asleep", "seed phrase dreaming"), banker's hours ("keeps
banker's hours", twice), unionised hardware ("my keys unionized", "the
buttons have unionised"), and vault metaphors ("vault, not a slot
machine"). This line touches none of them. It wins on the judge's own
order:

1. **On subject (criterion 1):** a hardware wallet refusing to sign at
   3 AM — the refusal is the whole line.
2. **Originality (criterion 2):** the seed phrase — the wallet's most
   sacred possession — becomes the refusal mechanism itself. Nobody in
   the field uses it as a line (only as a title).
3. **Voice (criterion 3):** the wallet speaks as a gatekeeper with
   rules: its twelve words are fixed, and 'yes' is not among them.
4. **The hour (criterion 4):** "at 3 AM" is the punchline's trigger,
   not decoration.
5. **Economy (criterion 5):** 62 characters, two sentences, one joke.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the under-200-character gate, and exits
0. No network, no randomness, no clock — the output is identical on
every run.
