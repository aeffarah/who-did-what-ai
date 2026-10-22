---
name: who-did-what
description: Build a who-did-what-ai session log (who contributed what, every course-correction, where the time went) from a finished Claude Code session's transcript. Use when the user runs /who-did-what or asks for a who-did-what log or retrospective of a past session.
---

# who-did-what

Build the log after the fact from a saved Claude Code transcript. Nothing has to be set up before or during the session.

**Scope.** You work from the transcript and the files in that session's own working folder. Don't open other folders, the raw `.jsonl`, connectors (docs, drives, email, chat), or the web, even to check a claim or find a deliverable. If something outside that scope would change the log, put it in your questions instead.

1. **Pick the session, then confirm.**
   - If this conversation already holds the work to log, use this session. Otherwise, if the user named a folder or session (in the command's arguments or their message), use that.
   - Run `python transcript.py --list <folder>` from this skill's directory (`python3` on macOS/Linux), where `<folder>` is the working folder (default: the current folder). It lists that folder's sessions, newest first, with each one's first prompt. In a fresh conversation the newest is usually this one.
   - Unless the work is in this conversation, stop and ask. Show the few most recent sessions (date, first prompt) and ask which one to log, leaving this conversation off the list. Never pick one yourself, even if one looks likely.
   - Before writing anything, say which session you'll log and where the files will go (that session's working folder unless the user says otherwise), and wait for a yes. Never overwrite an existing `session_log.md`, `transcript.md` or `retrospective.md`: if one is there (a live log, say), write `session_log_from_transcript.md` and so on beside it.
2. **Condense it.** Run `python transcript.py <session.jsonl> -o transcript.md --inputs 400` into the confirmed folder. `--inputs` shows what the AI wrote into files; drop it if the output gets too long to read in full. Tell the user the transcript may contain anything that passed through the session, secrets included, so they should review it before sharing.
3. **Build the log.** Read `build-log.md` in this skill's directory and follow everything below its line, using `transcript.md` as the transcript. Write `session_log.md` next to it.
4. **Ask your questions** (step "Then ask the human" in `build-log.md`), update the log, and draft `retrospective.md` when the user asks.

If Python isn't available, say so, and offer the fallback: the user runs `/export` in the original session and gives you that file as the transcript (no timestamps, so times become prompt numbers).

Claude Code deletes transcripts after 30 days by default (`cleanupPeriodDays` in settings). If a session is older than that, it's gone.
