# Reading your log

AI is supposed to co-build. It drafts, spitballs, and fills gaps, and it will usually write most of the words. That's the point. So the useful question isn't "who did more," it's "where did the result depend on me?" These questions get at that. Answers from the [worked example](../example/session_log.md) are in italics.

## 1. Where did it depend on you?

List the forks: the constraints you set, the calls you made, the corrections you caught. For each one, ask whether someone else would have made the same call. Those forks are your fingerprint on the result. Give the same tool and the same task to a hundred people and you get a hundred different outcomes; this is where yours came from.

*Assume every check fails and pre-define the escalation path. Elevate "recent release" into a testable hypothesis. One page, then no tables, then a memo you read top to bottom. The AI wrote most of the brief; none of those calls were its idea.*

## 2. Where did the corrections cluster?

Sort the ⚠ entries by substance (what the work says) versus form (how it's structured, worded or formatted).

*6 of 7 were form. The thinking was settled early; the rounds went to presentation.*

## 3. What does the AI keep optimizing for?

Put each correction's "AI optimized for X" side by side. Usually one word covers most of them.

*Completeness and fitting the page: tables because they're dense, an audit trail because it's thorough, stopping at the stated limit instead of the reader's attention.*

## 4. What do you keep optimizing for?

Same exercise, your side. This is your actual working style, as opposed to the one you'd describe in an interview.

*The reader: "who reads this, and how much will they read."*

## 5. Where did the AI fill a real gap, and did you verify it?

Look for AI-tagged WORK entries that changed the direction. Check whether each was confirmed or only labelled as an assumption.

*It supplied platform context that reframed the problem. It was labelled an assumption, not verified during the session, and owned as a trade-off in the retrospective.*

## 6. Where did the time go?

Split active minutes into setup, substance and form.

*About 12 setup, 20 substance, 45 form. Substance was a quarter of the active time.*

## 7. What did re-reading the source catch?

Count the times you went back to the original ask and found something.

*Three times, and something was found each time. The AI never did it unprompted.*

## 8. What would a template have saved?

If the form rounds repeat across sessions, the fix is a template, not more care.

*Most of the format rounds. That observation is how this repo started.*

## Optional: the default path

Want to see question 1 directly? Open a fresh session, give it only your opening request, and let it run with no steering. Compare where it ends up with where you ended up. The difference is what depended on you. It's one prompt, and it makes the "hundred people, hundred outcomes" point concrete.

## Spotting drift (experimental)

The log is timestamped and on disk, so it can show when an AI starts to slide in a long session. Watch for:

- **Repeats**: the same kind of correction needed again (entries marked *repeat*)
- **Reintroductions**: something you removed or corrected comes back (marked *reintroduced*)
- **Constraint slippage**: output that breaks a rule in the Constraints section, where earlier output followed it
- **Corrections clustering after a context reset**: a summarized or compacted context is logged as a PROCESS row, so you can see what changed after it

Two different things show up here, and it's worth telling them apart. **Default pull** is the AI sliding back to its habits even though the instruction is still in view. **Context drift** is the AI losing early instructions as the session grows. *The example shows default pull: "Step 0" survived every revision from 13:32 until it was cut at 14:40, and the same length correction was needed twice in ten minutes. At 137 minutes the session was too short to show context drift.*

The [setup instructions](../setup/instructions.md) also try to prevent drift: the AI re-reads the Constraints and Course-corrections sections before every revision, using the log as an anchor that lives outside its context. Whether that holds up over long sessions is untested. If you run a long one, your log is exactly the evidence this needs.

## Across sessions

Keep your logs. After a few sessions, put your answers to questions 1, 3 and 4 side by side. The patterns that repeat are the ones worth building around, whether that's a template, a standing instruction to the AI, or a habit.
