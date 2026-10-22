# Build the log from a transcript

Use this after a session, not during it. Give an AI the transcript and everything below the line. It works in any assistant: paste both into a chat, or in Claude Code point it at the two files.

The transcript can be the output of [`transcript.py`](transcript.py) (Claude Code, with real timestamps), Claude Code's `/export`, or a conversation copied out of any chat app. Use a fresh session: the AI that did the work shouldn't be the one grading it.

---

## Build a who-did-what log from this transcript

You're reviewing a finished working session between a human (H) and an AI. You weren't in it. Read the whole transcript first, then write `session_log.md` (or whatever filename you're given), and when asked, `retrospective.md`. If you can't write files, reply with each one in a code block.

**Ground rules**
- Everything comes from the transcript. If it isn't in there, it doesn't go in the log. Don't guess what the human was thinking.
- Where the AI in the transcript describes its own work ("I checked…", "about 8 minutes active", "logged as your call"), check the claim against what actually happened. Don't take its word.
- If the session was already being logged live, ignore the AI's edits to its own log. They aren't part of the work. What it says about its log in chat is a claim like any other: check it.
- If the transcript leaves out what the AI wrote (file contents, the deliverable), you may read the final output files if they're in the session's own folder. Don't go looking anywhere else (other folders, connected apps, the web) to fill gaps or check claims. Say in the log what you couldn't see, and ask if it matters.
- A long gap between turns is just a gap. Don't investigate what happened in it; ask if the answer would change the log.
- Keep it proportionate. A short session gets a short log.

**Time**
- Use the transcript's timestamps. They're exact, so clock times need no `~`. Derived minutes can be rounded.
- If the human says when their own timer started, use that as the start and count elapsed time from it. Elapsed is `m:ss` under an hour, `h:mm` over.
- If there are no timestamps, use prompt numbers (P1, P2…) in place of clock times, say so at the top, and skip minutes you can't support.

**Tag every timeline row**
- Layer, by what the event affects: **WORK** for the problem and the deliverable (analysis, decisions, content, its format), **PROCESS** for how the session ran (setup, tooling, prompting, steering, time). If one event is both, split it into two rows.
- **H**: the human's idea, decision or direction. **AI**: the model's contribution. **H→AI**: human directed, AI executed. **AI→H**: AI proposed, human decided. **⚠ H**: a course-correction (below).
- Attribute by who said it first in the transcript. If the AI suggests something the human then says they already intended, it's convergent, not the AI's.
- When the human picks one of the AI's options, that's **AI→H**. If they change it as they pick it ("option 2, but swap the days"), the change is **H**.
- When the AI decided something nobody asked it to decide (a format, a tool, a number, a date, an assumed fact), tag it **AI** and mark it *unasked*, even if the AI flagged it afterwards. These are easy to miss: look at what its output contains, not just what it says it did.
- Don't inflate either side. If the AI supplied knowledge the human lacked, say so plainly and mark it to verify.

**Find the course-corrections (⚠ H)**
- A course-correction is the human changing what the AI was doing or had done: overriding it, redirecting it, or catching something it got wrong or missed. Only the human can make one. When the AI catches its own mistake, that's an AI error, not a ⚠.
- Signals: an interruption, a rejected tool call (the human's reason is a prompt), "no", "actually", "I don't like", "obviously", the human repeating an instruction, the human re-reading the source and finding a gap.
- Not every signal is a correction. Extra information, a go-ahead, or a new request that doesn't undo anything is **H**. If you can't tell whether a new request was fixing something, make it one of your questions.
- For each one: what the AI did, what the human did instead, what each was optimizing for, and the pattern if one is emerging.
- Mark *repeat* when a correction targets the same AI habit as an earlier one (reading too literally, over-building, picking a format unasked), and name the earlier one. Mark *reintroduced* when something the human removed or corrected came back.
- If there are none, say so in one line. Don't invent any.

**Log the AI's errors too**
- Tool errors, failed commands, wrong assumptions, rework, and any claim that something was done, fits or works before the AI checked it. Note the time each one cost.

**Write `session_log.md` with these sections**
1. Header: session name, start time, goal (one line, from the human's own words), and "Built after the fact from a transcript."
2. **At a glance**: for someone who reads nothing else. One sentence with the headline finding, then this table, with every number counted from the sections below:

   | | |
   |---|---|
   | Time | N min elapsed: N active, N reading and thinking between turns |
   | Prompts | N |
   | Forks (where the result depended on the human) | N |
   | Course-corrections (⚠) | N (N repeats) |
   | Who originated what (timeline rows) | H N · H→AI N · AI→H N · AI N |
   | Unasked AI decisions | N |
   | AI errors | N, about N min lost |
   | Still unverified | N: name them in a few words each |

3. **Timeline**: a table of Elapsed | Clock | Layer | Who | What happened. One row per meaningful event, not per tool call.
4. **Prompts (verbatim)**: every human prompt exactly as written, typos included, numbered, with its time. Include mid-turn messages and rejection reasons, and mark them as such.
5. **Constraints**: what the human said the output must reflect (style, standards, audience, limits). Tag H.
6. **Course-corrections (⚠)**: one numbered entry per ⚠ row.
7. **Attribution summary**: first the **forks**, the points where the result went one way because of the human (a constraint, a call, a correction). Expect the AI to have written most of the words; the forks are what show where the result depended on the human. Then **H** (the human's other contributions), **AI**, and anything unresolved.
8. **Observations**: strengths and weaknesses for both sides, each tied to a time. A strengths-only list isn't honest.
9. **Time summary**: phases with window, minutes and layer, then active time and gap time as separate totals. Gaps are the time between the AI finishing and the human's next prompt: reading, reviewing, thinking and typing. Compute them from the timestamps; a total in the transcript header is a rounded cross-check.
10. **What the transcript can't show**: one or two lines. Work done outside the chat, what the human read or decided offline, anything that shaped the result but left no trace here.

**Then report back.** Open your reply with the At a glance sentence and table, so the human gets the summary without opening the log. Then end with at most three short questions the transcript can't settle, picking the ones whose answers would change the log most: a tag, a correction, or an open fact the result depends on. For example: "At 14:03, had you already planned the one-page limit, or did the draft prompt it?" Update the log with the answers. If the human skips them, leave the log as is.

**`retrospective.md`, when asked**
Draft it after the questions are answered or skipped. One page, in the human's voice (first person), written for whoever will read it, built only from the log. Sections: **What it helped with**, **Where I stepped in** (the ⚠ entries, compressed; group repeats), **What I did myself** (lead with the forks), **Where it could have misled me** (unverified claims, confident output ahead of checking), **What I'd change next time**. Open with one line: the tool, minutes elapsed and active, number of prompts and course-corrections, and that the full log is available on request. No audit-trail material: no tags, timeline rows or verbatim prompts.
