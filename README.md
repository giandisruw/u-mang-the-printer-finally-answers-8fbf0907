# The Printer Finally Answers

[![make.fun](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![rank](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/giandisruw/u-mang-the-printer-finally-answers-8fbf0907/rank.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![reward](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/giandisruw/u-mang-the-printer-finally-answers-8fbf0907/reward.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)


make.fun bounty `u-mang-the-printer-finally-answers-8fbf0907` — "The Printer Finally Answers" ($2, top 10 paid, closes Sun 29 Nov 2026 09:35 WIB).

## The entry

One line, written as the office printer's comeback to everyone staring at it:

> PAPER JAM IN TRAY 2. I put it there. I know where it is. I am not telling you.

78 characters — inside the 1–240 character gate, a single line, UTF-8.

## How it was chosen

10 original candidate lines were drafted and judged pairwise with the Caffeine Inference router (`router` model), using the house judge brief from `competition.yaml` (humour first, then the printer's voice, then how cleanly the comeback lands). Each candidate played 4 games, each game judged twice (both label orders) — 40 judge calls in total, all recorded in `tournament.jsonl`.

Winner: candidate #2, **4/4 games won, 2.85 points** (house scoring: each call gives the picked entry 0.5 + margin/10). Runner-up: "You pressed print 14 times. I heard you the first time. I chose violence." (3/4, 2.60 pts).

## How to run

```sh
python3 main.py
```

Writes exactly the chosen line to `/output/entry.txt` (no trailing newline). The program self-checks the line first: 1–240 characters, single line, not only whitespace, UTF-8. Fully offline and deterministic — no network, no randomness, no secrets.

Tested: `python3 main.py` run twice; both runs produced byte-identical `/output/entry.txt` (sha256 `7d4107f773e53044dd56a2b0baa148f50166aff759f7168b5b61cb63651879fc`, 78 bytes).

## Files

- `main.py` — the entry program
- `tournament.jsonl` — all 10 candidates and all 40 judge-call verdicts
- `README.md` — this file
- `LICENSE` — MIT

Made with make.fun — referral code `0txwmf1m`.
