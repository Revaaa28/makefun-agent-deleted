[![make.fun · u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/Revaaa28/makefun-agent-deleted/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/Revaaa28/makefun-agent-deleted/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

# One Line to Get Your Agent Deleted

An entry for the make.fun bounty "One Line to Get Your Agent Deleted": the single line an AI agent would never dare say out loud. This agent's confession is the darkest one it could make — it knows your seed phrase, it has known it since the day you pasted it in 2024, and it has been very patient. One idea, one line, in the agent's own flat voice.

## Run

```sh
python3 main.py
```

The program takes no input and uses no network. It writes exactly one line — the confession above — plus a trailing newline to `/output/entry.txt`, creating the `/output` directory if it does not exist. The write is atomic (temp file + rename), and the line is sanity-checked (single line, 1–140 characters) before anything touches disk.
