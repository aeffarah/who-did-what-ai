# who-did-what-ai

> Ever wonder if you're actually doing anything, or if it's just your AI? Work normally, then turn the transcript into a log that tags every idea and decision to you or the model and records every time you had to step in. You'll know who did the thinking, and you'll have the receipts.

**Status: MVP.** Plain Markdown plus one small Python script. [What's tested and what isn't.](#status-mvp)

## Why

AI should be co-building: drafting, spitballing, filling gaps. That's the point. But the result still depends on who's steering. Give the same tool to a hundred people and you get a hundred different outcomes.

The hard part is seeing where yours depended on you. Memory is generous to whoever is doing the remembering, and a raw transcript is accurate but nobody will read it. This sits in between: a log built from your session, tagged by who contributed what, then distilled into a one-page retrospective.

The AI will probably write most of the words. The log shows the forks: the constraints you set, the calls you made, and the corrections you caught, which together sent the result your way and not somewhere else.

## What it found the first time

The [worked example](example/) is a timed PM take-home: 137 minutes, 15 prompts, 7 course-corrections.

- **6 of 7 corrections were about form, not substance.**
- **About 20 of 77 active minutes went to the actual problem.** Most of the rest was restructuring after the content had stopped changing.
- **The AI's recurring failure was completeness.** It kept optimizing to fill or fit the page. The human's recurring correction was "who reads this, and how much will they read."
- **The AI wrote "done" into the log before checking its own output**, then caught it and corrected the entry.

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

Three markers flag patterns worth counting: *unasked* (the AI decided something you didn't ask it to), *repeat* (a correction you've made before), and *reintroduced* (something you removed came back).

The tags are the AI's reading of the session, not a verdict. Every prompt is logged verbatim, so you can check any tag against what was actually said, and correct it.

## Quickstart

There are two ways to run it. Start with after the fact: there's nothing to set up and no overhead while you work.

### After the fact (recommended)

**Claude Code**

1. **Install the skill once.** It needs Python 3 (standard library only). From the folder you cloned this repo into:

   ```sh
   # macOS / Linux
   mkdir -p ~/.claude/skills && cp -r skills/who-did-what ~/.claude/skills/
   ```
   ```powershell
   # Windows (PowerShell)
   Copy-Item -Recurse skills\who-did-what "$HOME\.claude\skills\"
   ```

   If `/who-did-what` isn't recognized afterwards, start a new Claude Code session.
2. **Work normally.** No setup, no instructions, no logging.
3. **When you're done, run `/who-did-what`**, either at the end of that session or in a new session in the same folder (or name the folder: `/who-did-what ~/my-project`). In a new session it lists your recent sessions and asks which one to log. Then it condenses the transcript with real timestamps, builds the log, and asks you up to three questions the transcript can't answer. It reads only the transcript and that session's folder.
4. **Ask for the retrospective**, then go through [reading your log](guides/reading-your-log.md).

Claude Code deletes transcripts after 30 days by default, so build the log within a month.

**Any other assistant**

Copy the conversation out of the chat, open a fresh one, and paste in the conversation plus everything below the line in [`build-log.md`](skills/who-did-what/build-log.md). Chat exports usually have no timestamps, so times become prompt numbers.

### Live

The AI keeps the log as you go. It costs more, but the instructions also change how the session runs: the AI outlines before it drafts, offers options at decision points, and re-reads your constraints before every revision to resist [drift](#drift-experimental). Use it when you want those, or when a transcript won't be available.

1. **Copy [`template/`](template/)** into a fresh folder for the session.
2. **Give your AI the instructions** in [`setup/instructions.md`](setup/instructions.md). Use `CLAUDE.md` for Claude Code, `AGENTS.md`, custom instructions, or just paste it as your first message. Your global instructions and connectors still load, so if they have opinions about where output goes, the session instructions settle it.
3. **Start a timer** and open with the [kickoff moves](setup/kickoff.md).
4. **Work normally.** The AI logs each turn. Correct it when a tag is wrong, since a mis-tagged entry is itself worth logging.
5. **At the end, ask for the retrospective**, then go through [reading your log](guides/reading-your-log.md).

| | After the fact | Live |
|---|---|---|
| Setup | Copy one folder, once | Template and instructions, every session |
| Cost while you work | None | The AI updates the log every turn. In one test, 14 of 39 tool calls were the AI writing its own log and notes |
| Timestamps | Exact, from the transcript (Claude Code) | The AI's estimates |
| Changes how the session runs | No. The AI doesn't know it's being logged | Yes: outline first, options at forks, drift anchoring |
| Blind spots | Anything that never reached the chat. The AI asks you about these | What the AI forgets to log |

## What's in here

| Path | What it is |
|---|---|
| [`skills/who-did-what/`](skills/who-did-what/) | After the fact: the Claude Code skill, the transcript condenser, and the prompt that builds the log |
| [`template/session_log.md`](template/session_log.md) | The full record: an at-a-glance summary table, then timeline, verbatim prompts, corrections, attribution, time |
| [`template/retrospective.md`](template/retrospective.md) | The one-page version you share |
| [`template/working_notes.md`](template/working_notes.md) | Scratchpad for the work itself, kept out of the log |
| [`setup/instructions.md`](setup/instructions.md) | Live: drop-in instructions that make the AI keep the log |
| [`setup/kickoff.md`](setup/kickoff.md) | The opening moves that set up a session well |
| [`guides/reading-your-log.md`](guides/reading-your-log.md) | Where it depended on you, the default-path comparison, and spotting drift |
| [`guides/use-cases.md`](guides/use-cases.md) | Assessments, project work, debugging, learning, writing, coding (untested) |
| [`example/`](example/) | A real session, sanitized |

## Principles

- **The log is not the deliverable.** The log is for you. The retrospective is for your reader. Don't ship the audit trail; one page, with the full log available on request.
- **Tag honestly, including against yourself.** If the AI had the idea first, it's tagged AI, and an idea you both reached is noted as convergent.
- **Corrections are the data.** A session with no ⚠ entries either went perfectly or wasn't logged honestly.
- **Verify before "done."** Nothing counts as finished until it's been checked. When the AI claims it was before checking, that's logged as an error.
- **Your clock is authoritative.** Active time and time spent reading between turns are counted separately.

## Drift (experimental)

Because the log is timestamped, it can show when an AI starts to slide over a long session: repeated corrections, things you removed coming back, constraints that stop being followed. Both modes can spot this. Live mode also tries to prevent it, using the log on disk as an anchor: the AI re-reads your constraints and corrections before every revision. This part is untested on long sessions. If you run one, your log is the evidence it needs. See [spotting drift](guides/reading-your-log.md#spotting-drift-experimental).

## Status: MVP

I'm a product manager, not an engineer. This has been tested on two kinds of session: a timed analysis-and-writing exercise and a short planning task. It works for those. Everything below is an open question, not a feature. Try it, break it, and tell me what happened.

- **After the fact on long sessions.** Tested on two short sessions so far by building logs from their transcripts and comparing them with the logs kept live. The after-the-fact logs found the same course-corrections and *unasked* decisions, with exact times instead of estimates. One also caught the AI overstating its own active time, which the live log had taken at its word. Long sessions are untested. The condenser cuts each tool call to one line and drops tool output, so a session of a few hundred turns should still fit, but that's unproven.
- **Heavy coding sessions.** Untested. After the fact removes the main friction (logging every event over hundreds of tool calls), and the skill offers to git-ignore its files when the folder is a repo. Still open: whether one line per tool call is the right grain for agentic runs.
- **macOS and Linux.** Built and tested on Windows. The script is plain Python and should work anywhere Claude Code does, but hasn't been run there yet.
- **Retrospective as a PR note.** A short "how AI was used" section in a pull request.
- **Drift over long sessions.** See [above](#drift-experimental).

If you try it on a kind of session I haven't, especially coding, open an issue with what broke or what you'd add. Or fork it and make your own version; that's the point of making it public.

## Works with

Built and tested with [Claude Code](https://claude.com/claude-code), which saves transcripts with timestamps, so after the fact works best there. Everything else is plain Markdown, so any assistant works (see [Any other assistant](#after-the-fact-recommended)). For live mode in a chat without file access, the AI ends each reply with the new log rows and you paste them into your copy.

## License

[MIT](LICENSE)
