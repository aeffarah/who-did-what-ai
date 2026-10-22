---
name: who-did-what
description: Build a who-did-what-ai session log (who contributed what, every course-correction, where the time went) from a finished Claude Code session's transcript. Use when the user runs /who-did-what or asks for a who-did-what log or retrospective of a past session.
---

# who-did-what

Build the log after the fact from a saved Claude Code transcript. Nothing has to be set up before or during the session.

1. **Pick the session.** Run `python transcript.py --list <folder>` from this skill's directory (`python3` on macOS/Linux), where `<folder>` is the working folder the session ran in (default: the current folder). It lists that folder's sessions, newest first, with each one's first prompt.
   - If this conversation already holds the work to log, use the newest.
   - If this is a fresh conversation, the newest is probably this one. Use the newest *other* session that matches what the user described.
   - If it's ambiguous, show the user the list and ask.
2. **Condense it.** Run `python transcript.py <session.jsonl> -o transcript.md`, writing into the session's working folder unless the user says otherwise. Add `--inputs 400` so you can see what the AI wrote into files; drop it if the output gets too long to read in full. Tell the user where the file is and that it may contain anything that passed through the session, secrets included, so they should review it before sharing.
3. **Build the log.** Read `build-log.md` in this skill's directory and follow everything below its line, using `transcript.md` as the transcript. The session's output files are in its working folder, so read the final versions of the deliverables. Write `session_log.md` next to the transcript.
4. **Ask your questions** (step "Then ask the human" in `build-log.md`), update the log, and draft `retrospective.md` when the user asks.

If Python isn't available, say so, and offer the fallback: the user runs `/export` in the original session and gives you that file as the transcript (no timestamps, so times become prompt numbers).

Claude Code deletes transcripts after 30 days by default (`cleanupPeriodDays` in settings). If a session is older than that, it's gone.
