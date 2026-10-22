# who-did-what-ai

> Ever wonder if you're actually doing anything, or if it's just your AI? Log a session, tag every idea and decision to you or the model, and record every time you had to step in. At the end you'll know who did the thinking, and you'll have the receipts.

## Why

AI-assisted work blurs authorship. Afterwards it's hard to say honestly which ideas were yours, which were the model's, and where you saved it from itself. Memory is generous to whoever is doing the remembering. A raw transcript is accurate but nobody will read it.

This sits in between: a running log the AI keeps while you work, tagged by who contributed what, then distilled into a one-page retrospective.

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

## Quickstart

1. **Copy [`template/`](template/)** into a fresh folder for the session.
2. **Give your AI the instructions** in [`setup/instructions.md`](setup/instructions.md). Use `CLAUDE.md` for Claude Code, `AGENTS.md`, custom instructions, or just paste it as your first message.
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
| [`guides/reading-your-log.md`](guides/reading-your-log.md) | Questions to ask of a finished log |
| [`guides/use-cases.md`](guides/use-cases.md) | Assessments, project work, debugging, learning, writing |
| [`example/`](example/) | A real session, sanitized |

## Principles

- **The log is not the deliverable.** The log is for you. The retrospective is for your reader. Don't ship the audit trail; one page, with the full log available on request.
- **Tag honestly, including against yourself.** If the AI had the idea first, it's tagged AI, and an idea you both reached is noted as convergent.
- **Corrections are the data.** A session with no ⚠ entries either went perfectly or wasn't logged honestly.
- **Verify before "done."** The AI doesn't record a result until it has checked it.
- **Your clock is authoritative.** Active time and time spent reading between turns are counted separately.

## Works with

Built and tested with [Claude Code](https://claude.com/claude-code). Everything is plain Markdown, so any assistant that can edit files works, as does one you paste into.

## License

[MIT](LICENSE)
