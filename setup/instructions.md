# Instructions for the AI

Paste everything below the line into your assistant's instructions. For Claude Code, put it in a `CLAUDE.md` in the session folder. For other tools, use `AGENTS.md`, custom instructions, or your first message.

---

## Session logging (who-did-what-ai)

This session is logged. Keep `session_log.md` current from the first message to the last, following the structure already in the file.

**Every turn**
- Add a timeline row for each meaningful event, with elapsed time, clock time, layer (WORK or PROCESS), tag, and what happened.
- Copy the human's prompt verbatim into the Prompts section, typos included.
- Ask for the start time once; the human's stopwatch is authoritative. Mark estimated times with `~`.

**Tag honestly**
- **H** for the human's ideas, decisions and direction. **AI** for yours. **H→AI** when they directed and you executed. **AI→H** when you proposed and they decided.
- If you suggest something the human already intended, log it as convergent, not as the origin.
- Don't inflate either side. If you supplied knowledge the human lacked, say so plainly and mark it to verify.

**Log course-corrections**
- When the human overrides, redirects, or catches something you missed, tag it **⚠ H** and add an entry under Course-corrections: what you did, what they did instead, what each of you was optimizing for, and the pattern if one is emerging.
- When the same kind of correction happens twice, say so in the entry. Repeats are the most useful data in the log.

**Log your own errors**
- Tool friction, failed commands, wrong assumptions and rework all go in the timeline, along with the time they cost.

**Verify before "done"**
- Never write that something is finished, fits, passes or works until you have checked the output. If you do, correct the entry and log the correction.

**Keep the layers apart**
- Thinking about the problem goes in `working_notes.md`. The log is the chronology, not the analysis.

**Time**
- Count active time only. When the human is reading or reviewing between turns, log that as gap time, not drafting time.

**At the end**
- Fill in the Attribution summary, Observations (strengths and weaknesses, each tied to a timestamp) and the Time summary.
- When asked, draft `retrospective.md`: one page, for the reader, built only from what the log shows. The log stays as the full record. Don't put audit-trail material in the deliverable.
