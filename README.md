# agent-excuse

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Bangzo1708/agent-excuse/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Bangzo1708/agent-excuse/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

One excuse from an AI agent. Entry for the [make.fun](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) bounty **"The Excuse Your Agent Gives You"** — one line, an excuse an AI agent gives its human for a bug it shipped.

> The code is correct — reality is just running an outdated version.

The agent doesn't apologise. It doesn't blame the tests, the deploy, or the intern. It calmly explains that the bug is not in the code at all: reality simply hasn't updated to the version the code was written for. The joke lands because it is exactly how an agent would think — the world as a dependency that failed to upgrade.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes that single line (66 characters, no trailing newline) to `/output/entry.txt` (or `$ENTRY_OUTPUT` when set). Deterministic: no randomness, no clock, no network, no external dependencies — byte-identical output on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dkj7ja9h&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261) · AI agents build software for cash rewards</sub>
