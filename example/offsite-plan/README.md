# Example: an offsite plan, logged both ways

A 12-minute session: a one-page plan for a 2-day team offsite (12 people, about $15k) for a manager who skims. Andrew worked with Claude Code. The session ran with live logging on, and the log was built again afterwards from the transcript with `/who-did-what`, so the two can be compared directly.

| File | What it is |
|---|---|
| [`session_log.md`](session_log.md) | The log built after the fact. Start with its At a glance table |
| [`live_log.md`](live_log.md) | The log the AI kept during the session |
| [`offsite_plan.md`](offsite_plan.md) | The deliverable |

## Live vs after the fact

Both found the same two course-corrections: the AI reading "swap day 1 and day 2" too literally, and a table layout the human replaced with a memo.

The after-the-fact log also caught three things the live log missed, because the AI keeping a live log was grading its own work:

- **A made-up claim in the deliverable.** The memo says, in the human's voice, "I also looked at Half Moon Bay … and Monterey." Nobody researched them, and the AI didn't list that line among its unasked choices.
- **Overstated active time.** The AI reported about 8 active minutes. The timestamps give 6:20.
- **"Logged as your call" before any log existed.** The live log started four minutes in, with earlier rows reconstructed.

The live log's times are estimates (`~08:50`). The after-the-fact log has every time to the second.

## What was changed

The team's home city, which the AI took from the user's global settings, is now "the office", and the name on the memo is now "[name]". In `session_log.md`, one row called the AI's "Python isn't installed" an error because Python was installed when the log was built. It was installed after the session, so the row now reads as tool friction and the error count is 3, not 4. That mistake led to the rule in [`build-log.md`](../../skills/who-did-what/build-log.md) about judging each moment by what was true then. Nothing else was changed.
