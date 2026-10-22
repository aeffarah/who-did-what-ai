# who-did-what-ai

> Ever wonder if you're actually doing anything, or if it's just your AI? Log a session, tag every idea and decision to you or the model, and record every time you had to step in. At the end you'll know who did the thinking, and you'll have the receipts.

**Status: MVP.** Plain Markdown, no install. [What's tested and what isn't.](#status-mvp)

## Why

AI should be co-building: drafting, spitballing, filling gaps. That's the point. But the result still depends on who's steering. Give the same tool to a hundred people and you get a hundred different outcomes.

The hard part is seeing where yours depended on you. Memory is generous to whoever is doing the remembering, and a raw transcript is accurate but nobody will read it. This sits in between: a running log the AI keeps while you work, tagged by who contributed what, then distilled into a one-page retrospective.

The AI will probably write most of the words. The log shows the forks: the constraints you set, the calls you made, and the corrections you caught, which together sent the result your way and not somewhere else.

## What it found the first time

The [worked example](example/) is a timed PM take-home: 137 minutes, 15 prompts, 7 course-corrections.

- **6 of 7 corrections were about form, not substance.**
- **About 20 of 77 active minutes went to the actual problem.** Most of the rest was restructuring after the content had stopped changing.
- **The AI's recurring failure was completeness.** It kept optimizing to fill or fit the page. The human's recurring correction was "who reads this, and how much will they read."
- **The AI twice wrote "done" into the log before checking its own output.**

None of that is visible in the finished deliverable. All of it is visible in the log.

## How it works

Every log entry gets a **layer** and a **tag**.

| Layer | What it covers |
|---|---|
| **WORK** | The problem itself: the analysis, the decisions, the content |
| **PROCESS** | How you ran the session: setup, tooling, prompting, steering, time |

| Tag | Meaning |
|---|---|
| **H** | Your idea, decision, or direction |
| **AI** | The model's contribution |
| **H→AI** | You directed, the AI executed |
| **AI→H** | The AI proposed, you decided |
| **⚠ H** | You overrode or redirected the AI (a course-correction) |

Course-corrections are the most valuable part. Each one records what the AI was optimizing for, what you were optimizing for, and the pattern. Over a session those patterns show you where you add value and where the AI reliably drifts.

The tags are the AI's reading of the session, not a verdict. Every prompt is logged verbatim, so you can check any tag against what was actually said, and correct it.

## Quickstart

1. **Copy [`template/`](template/)** into a fresh folder for the session.
2. **Give your AI the instructions** in [`setup/instructions.md`](setup/instructions.md). Use `CLAUDE.md` for Claude Code, `AGENTS.md`, custom instructions, or just paste it as your first message. Your global instructions and connectors still load, so if they have opinions about where output goes, the session instructions settle it.
3. **Start a timer** and open with the [kickoff moves](setup/kickoff.md).
4. **Work normally.** The AI logs each turn. Correct it when a tag is wrong, since a mis-tagged entry is itself worth logging.
5. **At the end, ask for the retrospective**, then go through [reading your log](guides/reading-your-log.md).

## What's in here

| Path | What it is |
|---|---|
| [`template/session_log.md`](template/session_log.md) | The full record: timeline, verbatim prompts, corrections, attribution, time |
| [`template/retrospective.md`](template/retrospective.md) | The one-page version you share |
| [`template/working_notes.md`](template/working_notes.md) | Scratchpad for the work itself, kept out of the log |
| [`setup/instructions.md`](setup/instructions.md) | Drop-in instructions that make the AI keep the log |
| [`setup/kickoff.md`](setup/kickoff.md) | The opening moves that set up a session well |
| [`guides/reading-your-log.md`](guides/reading-your-log.md) | Where it depended on you, the default-path comparison, and spotting drift |
| [`guides/use-cases.md`](guides/use-cases.md) | Assessments, project work, debugging, learning, writing, coding (untested) |
| [`example/`](example/) | A real session, sanitized |

## Principles

- **The log is not the deliverable.** The log is for you. The retrospective is for your reader. Don't ship the audit trail; one page, with the full log available on request.
- **Tag honestly, including against yourself.** If the AI had the idea first, it's tagged AI, and an idea you both reached is noted as convergent.
- **Corrections are the data.** A session with no ⚠ entries either went perfectly or wasn't logged honestly.
- **Verify before "done."** The AI doesn't record a result until it has checked it.
- **Your clock is authoritative.** Active time and time spent reading between turns are counted separately.

## Drift (experimental)

Because the log is timestamped and lives on disk, it can show when an AI starts to slide over a long session: repeated corrections, things you removed coming back, constraints that stop being followed. The instructions also use the log as an anchor, with the AI re-reading your constraints and corrections before every revision. This part is untested on long sessions. If you run one, your log is the evidence it needs. See [spotting drift](guides/reading-your-log.md#spotting-drift-experimental).

## Status: MVP

I'm a product manager, not an engineer. This has been tested on two kinds of session: a timed analysis-and-writing exercise and a short planning task. It works for those. Everything below is an open question, not a feature. Try it, break it, and tell me what happened.

- **Heavy coding sessions.** Untested. Likely friction: logging every event gets expensive over hundreds of tool calls, and the log could eat the context it's meant to protect. "Outline first, then wait" conflicts with letting an agent run, and a log in the repo root ends up in commits. Some ideas: a light mode that logs only your turns, forks and corrections; a git-ignored log folder; commit hashes instead of descriptions of edits.
- **Post-hoc logging.** Build the log from a saved transcript after the session instead of live. There's no overhead, and the AI doesn't know it's being watched.
- **Retrospective as a PR note.** A short "how AI was used" section in a pull request.
- **Drift over long sessions.** See [above](#drift-experimental).

If you try it on a kind of session I haven't, especially coding, open an issue with what broke or what you'd add. Or fork it and make your own version; that's the point of making it public.

## Works with

Built and tested with [Claude Code](https://claude.com/claude-code). Everything is plain Markdown, so any assistant that can edit files works. In a plain chat without file access, the AI ends each reply with the new log rows and you paste them into your copy.

## License

[MIT](LICENSE)
