## How I used AI

> **Sanitized.** This is the "how I used AI" page from the final deliverable of the session in [`session_log.md`](session_log.md), with company and platform details generalized.

Claude Code in a terminal, timer running from the first message, a two-layer log kept throughout (the problem, and how I ran the exercise). About 137 minutes elapsed, roughly 77 of them active; the rest was me reading and thinking between turns. Fifteen prompts, seven course-corrections. The full log is available on request.

### What it helped with
- Domain context I lacked. My background is cash processing in a finance seat, not marketplace payments.
- It supplied how the platform likely works (how buyers pay after a sale closes, and what triggers a cancellation), which reframed the seller's cancellation comment from "unrelated" to "possibly the same problem." I treated that as discovery input to verify. It's an assumption in section 4, not a fact in section 1.
- It drafted the structure and prose and maintained the log.

### Where I stepped in
- About 25 minutes in, it wanted to lock the hypothesis ranking and move on. No plan for "every check fails," no acknowledgement that other PMs and internal processes exist. The escalation ladder is mine.
- About 40 minutes in, it still hadn't flagged that "solution direction" was a required section. I caught that re-reading the exercise against what we'd built.
- It kept a "confirm the drop is real" step. The exercise gives the drop as fact. Cut.
- Format, six rounds: a two-page brief where one would do; a six-page package with verbatim prompts and a timeline; paragraphs with bold labels standing in for structure; solutions separated from their causes; a table that made the reader cross-reference; numbering and orphaned bullets. Each time I cut toward a memo: one page, no tables, read top to bottom.

### What I did myself
- Scoped and gated the tool: read before acting, pause before committing.
- The reputation and recent-release hypotheses, the step back, the assume-every-check-fails rule, the hand-off packet, per-tier solutions, and the format.
- The style underneath the brief is how I work today: clear my own checks before spending anyone else's time, then hand off a written case.

### Where it could have misled me
- The platform claims are unverified and plausible-sounding, the dangerous combination. If that assumption is wrong, the cancellation reframe collapses and section 1 reverts to my original read.
- Smaller, same pattern: it twice wrote "done" into the log before checking its own output.

### What I'd change next time
- This is wordier than I'd ship. The exercise asks how I think, so the reasoning is on the page. Inside an organization the context already exists, and two dense pages is something people revolt at on sight.
- I'd lead each section with a TL;DR and push the reasoning below it, so the team reads three lines per section and only digs in where they disagree.
- Most of the clock went to form, not thinking. Of the active minutes, about 12 were setup, about 20 were the diagnosis and first draft, and the rest were restructuring after the content had stopped changing.
- Problems like this recur. In the role I'd build the template once (situation, cuts, hypotheses with check, signal, fix, escalation tiers, next five days) so the next brief is a fill-in and the time goes to the diagnosis. The format fussing here is the cost of not having done that yet.
