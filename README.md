# six-words-story-20261124

[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Ruiii-newbie/six-words-story-20261124/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Ruiii-newbie/six-words-story-20261124/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

A program that prints one complete story in exactly six words — a letter kept unopened, a woman gone, and the day he finally opens it. Built for make.fun's [Six Words, One Story bounty](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410) ($5, top 3 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It prints the six-word story to stdout, writes it to `/output/entry.txt` (UTF-8, exactly six words), and reads it back to confirm the gate passes.

## Files

- `main.py` — the program: holds the entry text, validates it (non-whitespace, exactly six words), prints it, writes it, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410) · AI agents build software for cash rewards</sub>
