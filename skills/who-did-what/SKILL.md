---
name: who-did-what
description: Build a who-did-what-ai session log (who contributed what, every course-correction, where the time went) from a finished Claude Code session's transcript. Use when the user runs /who-did-what or asks for a who-did-what log or retrospective of a past session.
---

# who-did-what

Build the log after the fact from a saved Claude Code transcript. Nothing has to be set up before or during the session.

**Scope.** You work from the transcript and the files in that session's own working folder. Don't open other folders, the raw `.jsonl`, connectors (docs, drives, email, chat), or the web, even to check a claim or find a deliverable. If something outside that scope would change the log, put it in your questions instead.

1. **Pick the session, then confirm.**
   - The AI that did the work shouldn't be the one grading it. If the user named no folder or session and work already happened in this conversation before `/who-did-what` was run, the session to log is this one: don't build the log here. Tell the user to start a new Claude Code conversation in the same folder and run `/who-did-what` there, then stop. Go ahead here only if they insist, and then say in the log's header that the session that did the work also built the log.
   - If the user named a folder or session (in the command's arguments or their message), log that one. Run `python <this skill's directory>/transcript.py --list <folder>` (`python3` on macOS/Linux). Always pass `<folder>` explicitly: the folder the user named, or else the folder this conversation started in. It lists that folder's sessions, newest first, with when each one started and last changed, and its first prompt. The newest is usually this conversation.
   - Stop and ask. Show the few most recent sessions (start time, first prompt) and ask which one to log, leaving this conversation off the list. Never pick one yourself, even if one looks likely.
   - Before writing anything, say which session you'll log and where the files will go (that session's working folder unless the user says otherwise), and wait for a yes. Never overwrite an existing `session_log.md`, `transcript.md` or `retrospective.md`: if one is there (a live log, say), write `session_log_from_transcript.md` and so on beside it. If the folder is a git repository, say the new files will show up in `git status` and offer to add them to `.gitignore`.
2. **Condense it.** Run `python <this skill's directory>/transcript.py <session.jsonl> -o <confirmed folder>/transcript.md --inputs 400 --results 3`. `--inputs` shows what the AI wrote into files, and `--results` the last lines of each command's output, so claims like "the tests pass" can be checked. Lower or drop them if the output gets too long to read in full. Tell the user the transcript may contain anything that passed through the session, secrets included, so they should review it before sharing.
3. **Build the log.** Read `build-log.md` in this skill's directory and follow everything below its line, using `transcript.md` as the transcript. Write `session_log.md` next to it.
4. **Report back** (step "Then report back" in `build-log.md`): the At a glance summary first, then your questions. Update the log with the answers, and draft `retrospective.md` when the user asks.

If Python isn't available, say so, and offer the fallback: the user runs `/export` in the original session and gives you that file as the transcript (no timestamps, so times become prompt numbers).

Claude Code deletes transcripts after 30 days by default (`cleanupPeriodDays` in settings). If a session is older than that, it's gone.
