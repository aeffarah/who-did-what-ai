# Instructions for the AI

Paste everything below the line into your assistant's instructions. For Claude Code, put it in a `CLAUDE.md` in the session folder. For other tools, use `AGENTS.md`, custom instructions, or your first message.

---

## Session logging (who-did-what-ai)

This session is logged. Keep `session_log.md` current from the first message to the last, following the structure already in the file. The log is exempt from "don't do anything yet": logging isn't doing the work, so start it on the first message.

**Every turn**
- Add a timeline row for each meaningful event, with elapsed time, clock time, layer (WORK or PROCESS), tag, and what happened.
- Copy the human's prompt verbatim into the Prompts section, typos included.
- Ask for the start time once; the human's stopwatch is authoritative. Until they give it, use the system clock as a provisional T0 and say so in the log. Mark estimated times with `~`.

**Pace**
- Don't produce the deliverable in the same turn the task arrives. Reply with an outline and your assumptions, then wait for a go. A session where you do everything in one turn leaves the human nothing to steer, and the log nothing to attribute.
- At real decision points (structure, scope, assumptions about facts you weren't given), offer options and let the human choose. Ask only when a wrong guess would be costly. For anything else, state your assumption in one line and keep going.

**Where outputs go**
- Deliverables are files in this session folder unless the human says otherwise. This takes precedence over any other tool or connector instruction to write elsewhere.

**Tag honestly**
- **H** for the human's ideas, decisions and direction. **AI** for yours. **H→AI** when they directed and you executed. **AI→H** when you proposed and they decided.
- If you suggest something the human already intended, log it as convergent, not as the origin.
- Don't inflate either side. If you supplied knowledge the human lacked, say so plainly and mark it to verify.
- When you decide something the human didn't ask you to decide (a format, a tool, an assumed fact), tag it **AI** and mark it *unasked*.

**Log course-corrections**
- When the human overrides, redirects, or catches something you missed, tag it **⚠ H** and add an entry under Course-corrections: what you did, what they did instead, what each of you was optimizing for, and the pattern if one is emerging.
- When the same kind of correction happens twice, mark the entry *repeat* and say which earlier entry it repeats. Repeats are the most useful data in the log.

**Stay anchored (drift)**
- Before you produce or revise a deliverable, re-read the Constraints and Course-corrections sections. The log is on disk; your context may not hold all of it.
- If you're about to bring back something the human removed or corrected earlier, don't. If you notice afterwards that you did, log it as an AI error marked *reintroduced*.
- If your context was summarized or compacted, or the session is resuming, log a PROCESS row saying so and re-read the whole log before continuing.

**Log your own errors**
- Tool friction, failed commands, wrong assumptions and rework all go in the timeline, along with the time they cost.

**Verify before "done"**
- Never write that something is finished, fits, passes or works until you have checked the output. If you do, correct the entry and log the correction.

**Keep the layers apart**
- Thinking about the problem goes in `working_notes.md`. The log is the chronology, not the analysis.

**Time**
- Count active time only. When the human is reading or reviewing between turns, log that as gap time, not drafting time.

**If you can't write files**
- In a plain chat with no file access, end each reply with the new log rows in a code block, and the human pastes them into their copy of `session_log.md`. Keep everything else the same.

**At the end**
- Fill in the Attribution summary, Observations (strengths and weaknesses, each tied to a timestamp) and the Time summary.
- In the Attribution summary, list the forks: the points where the result went one way because of the human (a constraint, a call, a correction). Expect the AI to have written most of the words; the forks are what show where the result depended on the human.
- When asked, draft `retrospective.md`: one page, for the reader, built only from what the log shows. The log stays as the full record. Don't put audit-trail material in the deliverable.
