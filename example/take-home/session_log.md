# Session Log: Timed PM Take-Home

> **Sanitized.** The company, the exercise text and platform-specific claims have been removed or generalized. Square brackets in prompts mark redactions. Tags and layer names have been updated to this repo's scheme (A → H, C → AI, SCENARIO → WORK, META → PROCESS). Everything else is as logged: the timeline, the prompts, the corrections and the time.

**T0:** 2026-09-04 13:08 (approx. — matches folder creation time; Andrew's stopwatch is authoritative)  
**Budget:** 1–2 hours per the exercise brief  
**Goal:** A short product brief diagnosing checkout abandonment at the payment step plus rising order cancellations on a B2B marketplace, and an honest note on how AI was used.  
**Purpose:** Local record behind the "how you used AI" note. Not in the final deliverable (cut at 14:03, see course-correction 3).

## Tags

- **WORK**: the actual problem (checkout abandonment at the payment step, rising cancellations)
- **PROCESS**: how Andrew set up and ran the exercise (tooling, prompting, process design, time management)

- **H** = Andrew's idea / decision / direction
- **AI** = Claude's contribution
- **H→AI** = Andrew directed, Claude executed
- **AI→H** = Claude proposed, Andrew decided
- **⚠ H** = Andrew overrode or redirected Claude (course-correction)

## Timeline

| Elapsed | Clock | Layer | Who | What happened |
|---|---|---|---|---|
| 00:00 | 13:08 | PROCESS | H | Session opened in a fresh, empty folder ("Skill Check"). Timer started. |
| ~00:01 | 13:09 | PROCESS | H | Prompt 1: sanity check that Claude is scoped to the right working directory before letting it do anything. |
| ~00:01 | 13:09 | PROCESS | AI | Confirmed working directory, listed folder (empty), listed other accessible dirs. Took no other action. |
| 00:04 | 13:12 | PROCESS | H | Dropped the exercise PDF into the folder. |
| ~00:05 | 13:13 | PROCESS | H | Prompt 2: explicit read-only constraint. "Don't do anything yet, just read this for context." |
| ~00:06 | 13:14 | PROCESS | AI | Read the PDF and summarized the deliverable. Flagged that the AI-reflection section is graded as heavily as the brief and suggested keeping a running log. |
| ~00:09 | 13:17 | PROCESS | H | Prompt 3: Andrew already intended the log. Claude's suggestion converged with a pre-existing plan; it was not the origin. Andrew specified the two-layer structure, stopwatch timing, honest strengths/weaknesses, and that the brief must reflect his real PM style (see constraints below). |
| 00:12 | 13:20 | PROCESS | H→AI | Claude creates this log and seeds it with the above. No work on the problem has started yet. |
| ~00:17 | 13:25 | PROCESS | H | Prompt 4: reminder that the brief is 1–2 pages, so everything gets summarized. Then "dive right in." |
| ~00:17 | 13:25 | WORK | H | First read. Two starting points: (1) drop-off at payment, (2) seller's cancellation comment. Instinct: cancellations don't sound like payment; more likely reputation (bad press, reviews, competitor articles). The buyer researches before committing and bails. But explicitly refuses to discredit the seller; wants to diligence the tech side too. |
| 00:18 | 13:26 | WORK | AI | Reaction logged in `working_notes.md`. Key contribution: platform context suggesting that on this kind of marketplace, cancellations are often a payment event (the buyer fails to pay after the sale closes), which would tie the two symptoms together rather than separate them. Flagged as AI-supplied domain knowledge that Andrew must verify. Also proposed the two fastest diagnostic cuts. |
| 00:18 | 13:26 | PROCESS | AI→H | Claude splits content from process: `working_notes.md` for the thinking (H/AI tagged), `session_log.md` stays the chronological record. Brief will be distilled from the notes. |
| ~00:23 | 13:31 | PROCESS | H | Prompt 5: Andrew states his domain is cash processing from an investments / accounting / finance seat, not marketplace payments. He did not know the platform's payment model going in. Treats Claude's context as "adjacent to discovery": input to verify, not fact. |
| ~00:23 | 13:31 | WORK | H | Accepts both diagnostic cuts. Adds: the attempted-vs-never-attempted split, read with click counts and time-on-page, could expose a **recent release or UI change** that introduced a bug or an optimization opportunity. Elevates "recent deploy" from a passing mention (AI) to a first-class hypothesis with a behavioral signature. |
| 00:24 | 13:32 | WORK | AI | Drafts a ranked hypothesis list (6 candidates plus a Step 0 sanity check, ranked by cost-to-rule-out and what the payments team controls) in `working_notes.md`. Ranks Andrew's reputation hypothesis last, with rationale, and flags the tension explicitly for him to decide. |
| 00:25 | 13:33 | PROCESS | AI | Tooling friction: a shell heredoc failed on quoting. Claude rewrote the edit as a script file and re-ran. ~1 minute lost. Logged because it is the kind of thing the reflection should be honest about. |
| ~00:30 | 13:38 | PROCESS | ⚠ H | Prompt 6: Andrew pauses before committing to the ranking Claude pushed for. Widens the frame: (1) a company like this has other PMs and internal processes he cannot discover in a hypothetical, so the brief must cover as many internal bases as possible and state its org assumptions. (2) Design for the worst case: assume every self-service check fails, so the plan must end in a defined escalation beyond his scope, carrying the checks already done as a hand-off packet to avoid double work. |
| 00:32 | 13:40 | WORK | AI | Turns the redirect into a tiered escalation ladder (Tier 0 solo → Tier 1 adjacent internal functions → Tier 2 engineering → Tier 3 external) with a hand-off packet at each boundary. Lists the internal functions a marketplace like this likely has and what to ask each. Ranking from 13:32 becomes the sequencing *inside* Tier 0, not the whole plan. |
| ~00:37 | 13:45 | WORK | H | Prompt 7: re-reads the deliverable. Interprets "a brief to align your team on next steps" as what has been built so far: finish what can be done alone, then expand the search. Catches that "potential solution direction" has not been covered at all; the session has been iterating on problems only. Asks for a solution direction per tier, generic where necessary, so each tier's multiple objects are covered. |
| 00:39 | 13:47 | WORK | AI | Drafts solution directions per tier in `working_notes.md` section 5, each conditional on where the cause lands, plus one cause-independent direction (per-storefront payment-health observability) that holds regardless of outcome. Proposes folding the validation plan into the hypothesis table as the "predicted signature" column, to save space in the brief. |
| ~00:42 | 13:50 | PROCESS | H | Prompt 8: go. Produce the final PDF. |
| 00:44 | 13:52 | PROCESS | AI | Checks PDF tooling (no pandoc, no reportlab; Python markdown lib and Chrome headless available). Chooses markdown → HTML → Chrome print-to-PDF. |
| 00:44–47 | 13:52–13:55 | WORK | AI | Drafts `brief.md` from the working notes, in Andrew's first-person voice: six sections plus the AI-use note. Compresses the hypothesis table to six rows with a validation column, the ladder to four rows, solutions to one regardless-of-cause direction plus a four-row conditional table. Adds a five-day plan for the "align on next steps" framing. |
| 47 | 13:55 | PROCESS | AI | First render. Brief body ran to ~2.3 pages plus a fourth page for the AI note; one table column wrapped badly. |
| 48 | 13:56 | PROCESS | AI | Trims prose (~8% shorter, no content removed), tightens print CSS, fixes column widths, re-renders. Wrote "final: 2 pages" into this log *before* checking the render. Checked: still ~6 lines over. Correcting the entry. Small thing, but it is exactly the pattern the AI note warns about: confident output ahead of verification. |
| 50 | 13:58 | PROCESS | AI | Third pass: type 9.6pt, tighter heading margins, section 6 shortened by a clause. Re-render and verify by reading the PDF back before claiming the fit. |
| 50 | 13:58 | PROCESS | AI | Verified by reading the PDF back: brief on 2 pages, AI note on page 3. Appendix PDF rendered with two defects Claude noticed on read-back: timeline columns wrapping character by character, header lines and lists merged (missing blank lines in the markdown). |
| 51 | 13:59 | PROCESS | ⚠ H | Prompt 9: cut the brief itself to one page. Everything else (AI note, log, stats) is process-oriented context behind a disclaimer, "maybe interesting to view," so running past two pages is fine. |
| 53 | 14:01 | PROCESS | AI | Rewrites the brief to one page: same six sections, ~45% shorter; hypothesis table drops the "rules it out" column, ladder and solution tables compress to short cells, conditional solutions become one dense paragraph. Combines brief + disclaimer + AI note + this log into one PDF. Fixes the two appendix render defects. Adds the format decision as the fourth intervention in the AI note. |
| ~55 | 14:03 | PROCESS | ⚠ H | Prompt 10: the brief is good but too wordy for an internal audience who already know the domain. And the whole PDF should be two pages: verbatim prompts and the timeline are overkill, a "how to read" section is a sign the document is too much. Nobody reads six pages; a reviewer opening that fails the exercise. |
| 63 | 14:11 | PROCESS | AI | Rewrites the brief for an internal reader (~25% shorter again: drops rationale clauses, shortens table cells, tighter section 1). Page 2 becomes the AI note plus a five-row process summary. Verbatim prompts, timeline, how-to-read, attribution lists, and observations all leave the PDF and stay in this local file. |
| ~65 | 14:13 | PROCESS | ⚠ H | Prompt 11: content is right, but everything is in paragraphs with inline bold labels standing in for structure. Wants sections, sub-labels, and bullets. Pasted two sections back as evidence; the paste also showed "fi x" / "confi g", i.e. fi-ligatures not surviving copy from the PDF. |
| 83 | 14:31 | PROCESS | AI | Restructures both pages: h2 sections, h3 sub-labels, bullets throughout; tables unchanged. Disables font ligatures in the render so copied text stays intact. Re-renders and verifies two pages. |
| 85 | 14:33 | PROCESS | AI | Bulleted brief spilled ~12 lines onto page 2. Folded the two section intro lines into their headers, merged four bullets, trimmed margins and type slightly. Also corrected the time table: the 14:11–14:31 gap was Andrew reading, not drafting; drafting is now counted as active time only. Re-rendered and verified. |
| 86 | 14:34 | PROCESS | AI | Still two lines over after the first fit pass. Merged the two assumption bullets, trimmed page margins and type by a hair. Re-rendered, verified two pages. |
| ~92 | 14:40 | WORK | ⚠ H | Prompt 12: (1) "Step 0: is the drop real?" is redundant. The exercise states the funnel already shows drop-off at payment; re-checking it second-guesses a given. (2) Section 5 forces the reader to pan between tiers and their solutions. Remove it and embed each tier's fix after the tier, for one coherent flow. Open to dropping the tables in 3 and 4 or embedding into them. |
| 101 | 14:49 | WORK | AI | Removes Step 0. Dissolves section 5: the tier table becomes four bullet blocks, each ending in "If it lands here" with its fix; the regardless-of-cause observability item closes the section. Adds a "Fix sits in" column to the hypothesis table so section 3 points into section 4. Hypothesis table kept (six items by four attributes scan better as a grid). Numbering drops to five sections. |
| ~104 | 14:52 | WORK | ⚠ H | Prompt 13: drop the hypothesis table entirely. Header plus bullets per hypothesis: hypothesis, check, signal if true, solution. The "Fix sits in" column still made the reader look at a column and then hunt through the tiers. Linear is easier. No tables at all reads more like a true brief or memo. |
| 110 | 14:58 | WORK | AI | Hypothesis table becomes six sub-labelled blocks, each with a check-and-signal bullet and a fix bullet. Because the fix now lives with its cause, the per-tier "If it lands here" lines come off the tiers to avoid stating every fix twice; tiers are back to who, ask, hand-off. Zero tables on page 1. Flagged the tier-fix removal to Andrew as a judgment call he can reverse. |
| ~114 | 15:02 | PROCESS | ⚠ H | Prompt 14: four items. Drop the numbers on hypothesis sub-labels. Make Check / Signal / Fix visually distinct. The trailing bullets under the last hypothesis and under Diagnosis read as belonging to the item above them; give them their own sub-labels. And add a note, in the brief or after the AI piece, that he would normally build a template because these issues recur, and that most of the timeline was format fussing. |
| 122 | 15:10 | PROCESS | AI | Numbers dropped; the two references to "Number 6" and "1 to 3" rewritten as "Reputation" and "the first three." Check / Signal / Fix bolded. New sub-labels "Alongside the cuts" and "Reading the results" so orphan bullets have a home. Added "What I'd change next time" on page 2 with an honest split of active minutes (setup ~12, substance ~20, format the rest) and the template point. |
| ~124 | 15:12 | PROCESS | H | Prompt 15: drop the "ranked my first instinct last" bullet from the AI note. Then one last redundancy pass, since it is wordy, and finish. |
| 137 | 15:25 | PROCESS | AI | Final pass. Page 2: reputation bullet dropped; process table removed (its minute split duplicated "What I'd change next time"; its totals moved into the intro line); format bullet rewritten as a six-item list, half the length. Page 1: "Reading the results" no longer restates the ranking criteria; one fix item that duplicated Tier 3 removed; day-plan bullet shortened. Both pages now table-free. Rendered and verified. Status: final draft, pending Andrew's own verification of the platform assumption. |

## Prompts (verbatim)

### Prompt 1 (~13:09)
> are you linked to skill check

### Prompt 2 (~13:13)
> added a pdf into skill check, I've started a timer, don't do anything yet just read this new pdf for context then we can go from there

### Prompt 3 (~13:17)
> so that is exactly my point, I want to keep track of things such as my prompt engineering, where my brain went vs what you contributed, [the exercise] mentioned 1-2 hours to put this together, I started a timer at the beginning of this chat ~3 minutes ago, want to, alongside my timer, also keep a log for the exercise sake of how long things take so we can have a detailed log to [hand in] alongside the assignment
>
> I am looking at it in 2 ways, 1 being my process in terms of the actual context from the pdf, but also the outside the box process of how I am tackling putting together this actual product in general, prep to do the assignment effectively
>
> And I want it to honestly reflect my strengths and weaknesses and how I work. Aligning with how I work as a PM at my current role, I tend to try and pinpoint issues, or at the very least clear my responsibilities before sending anything to anyone else
>
> So I never reach out to my engineer and talk about issues, I iterate until I find it, hands on, and generally push an md fix with an explanantion
>
> I want to make sure that this style translates when we complete this scenario to [hand in]

### Prompt 4 (~13:25)
> also keeping in mind that we will effectively be summarizing where applicable since this is meant to be 1-2 pages long
>
> That said, lets dive right in now that structure and context is established
>
> My knee jerk reaction is 2 potential places to start
>
> drop-off exists at payment, and seller has mentioned order cancellations
> order cancellations does NOT sound like it relates to an issue at payment, but potential bad press or reviews that have circulated, or articles from competitors
>
> If a customer researches a product before purchasing, that could be the immediate reason for cancellations or drop-off at payment
>
> But I also don't want to fully discredit our customer, and do want to diligence what could be going on from the tech side as well

### Prompt 5 (~13:31)
> this is good context for how [the platform] works that I wasn't aware of going into this, since my main domain overlap lies in cash processing from an investments / accounting / finance side, [in my current role]
>
> I consider this adjacent to discovery
>
> so looking at seller-specific vs platform wide and Attempted-and-failed vs never-attempted, this should be easy to cross examine across other sellers / platforms to see if there are parallels
>
> attempted and failed vs never attempted is important to, depending on amount of clicks and time spent on page, perhaps a new update or UI change could have rolled out and there are issues or optimizations that can be made

### Prompt 6 (~13:38)
> before we commit to something, want to do a small step back, would assume a company like [this one] has other PMs, I always try to be thorough, "I don't know what I don't know", and in this circumstance, with a domain gap that requires discovery, which I can't do since this is a hypothetical situation, and we can't really speak to the existence of internal processes and the amount of PMs that do exist, I want to cover as many internal basis as possible
>
> I also want to make the assumption that every check we make results in a failure, which inevitably ends with us reaching outside of our immediate position scope to the 'next set of checks', whether it be engineering or whatever, while having our data and our checks as reference to avoid double work in case of overlap

### Prompt 7 (~13:45)
> last piece, the scenario mentions [a potential solution direction], and for the deliverable itself, [a short product brief to share with your team to align on next steps]
>
> I'm going to interpret the second quote as what we've already done, finish what I can do alone before expanding the search
>
> I don't believe we've covered "potential solution direction" since we've mostly been iterating on problems, would like to break out a solution per tier, even if generic to cover the multiple objects per tier

### Prompt 8 (~13:50)
> lets do it, produce a pdf for the sake of [the final deliverable]

### Prompt 9 (~13:59)
> if we make the brief itself 1 page, we can make a disclaimer that everything else is process oriented and context of and stats etc that are more 'maybe interesting to view' and can get away with going over the 2 pages

### Prompt 10 (~14:03)
> I like the brief, but I think we can make it less wordy with the assumption that an internal brief will be with people who understand what we are discussing, less explanation needed
>
> I think we can also keep this to 2 pages, verbatim prompts are overkill, the timeline is also a little bit overkill, the goal is summarizing and explaining, not making a bullet proof audit trail that requires a 'how to read' seciton, thats definitely too much, people barely even read resumes, getting someone to open a document like this and seeing 6 pages is definitely failing the scenario

### Prompt 11 (~14:13)
> okay read through this, looks good, only thing I don't like is that everything is in paragraphs and nothing is in bullets or broken out in sections, bold text was used instead which makes this harder to read, for example: [pastes sections 5 and 2 back]

### Prompt 12 (~14:40)
> from the scenario, first paragraph says: [the funnel data already shows drop-off at the payment step] so our diagnosis: Step 0: is the drop real? is already apart of this exercise as a known truth, which makes it a redundant double check
>
> I think instead of using tables for 3 and 4, or at least embedded into the tables, we remove 5 and embed solutions after each tier instead of having a separate section to avoid people having to pan from section to section, want this to be a coherent flow

### Prompt 13 (~14:52)
> I think we jsut get rid of the hypothesis table and make this into a header with bullets, like Hypothesis, check, signal if true, solution, I think keeping it linear is easier to read since we still have to see a 'fix sits in' column and then look at the tiers, I think the original document was more legible, but I think removing the table completely makes this more like a true "brief" or memo

### Prompt 14 (~15:02)
> I dont like that the subsections under hypothesis are numbered, I think we can just keep the bolded "1.Recent checkout or payment release regressed" and drop the 1, 2 etc
>
> Also 'Check, signal, fix' should also be distinguishable, bolded or underlined or something under each hypothesis
>
> [quotes the two trailing bullets] looks like it is apart of "6.Reputation or demand drop" because it is just linear bullets following under the fix, same with "Then cancellations by initiator..." under diagnosis
>
> Last thing - I also want to add somewhere in this, either brief or afted the 'how I used ai' piece that mentions I would normally create a template since issues are reoccuring, and realistically if we look at my timeline, the majority of this has been me fussing about the format

### Prompt 15 (~15:12)
> [quotes the reputation bullet] let's just drop this then I think we're good to final draft, maybe 1 last redundancy check since it is wordy, and we should be good to [hand in]

## Constraints (from Prompt 3) — H

These shape the WORK layer. The brief should read the way Andrew actually operates:

1. **Diagnose before escalating.** The diagnosis section should show the PM pulling and cutting the data themselves (funnel segmentation, gateway decline codes, session replays, cancellation reasons) before booking an engineer's time. "Clear my own responsibilities first."
2. **Iterate hands-on until the cause is pinpointed.** Hypotheses should be framed as things Andrew would personally test and rule in/out, not delegate.
3. **Ship a written fix with an explanation.** The solution direction should follow the md-fix-with-rationale pattern: a concrete, reviewable proposal with the reasoning attached, not "schedule a discovery meeting."

## Course-corrections (⚠)

1. **13:38: Claude pushed to commit, Andrew paused.** Claude ended the 13:34 turn with "confirm the order and I'll draft the validation plan." Andrew stepped back instead: the ranking was a list of checks with no frame around what happens when they all come back negative, and no acknowledgement that other PMs and internal processes exist. Claude's draft optimized for speed of elimination and skipped the organizational layer. Andrew supplied it: assume every check fails, define the escalation path in advance, and carry the evidence forward as a hand-off packet. This is the "clear my responsibilities before sending anything to anyone" style showing up as a design principle for the brief itself.
2. **13:59: Format.** Claude produced a two-page brief plus a one-page AI note, verified the fit, and treated the job as done. Andrew: the brief itself should be one page; everything else is process material behind a disclaimer, so the total length stops mattering. Claude had optimized for the stated ceiling (1–2 pages). Andrew optimized for the reader: one page of thinking that has to be read, and everything else clearly marked optional. Same content, better contract with the reviewer's time.
3. **14:03: Audience and length.** Claude built the log as an audit trail: verbatim prompts, a 30-row timeline, a legend explaining the tags. Andrew: that is the wrong artifact. The goal is to summarize and explain to a reader who barely reads resumes. A document that needs a "how to read" section is too much; six pages fails the exercise on its own. Same for the brief: internal readers know the domain, so cut the explaining. Claude's instinct was completeness; Andrew's was the reader. Second time in ten minutes the same correction was needed, which is itself a finding about how the AI errs.
4. **14:13: Structure.** Claude compressed the brief by turning sections into dense paragraphs with bold inline labels. Andrew: that trades readability for line count; use headers, sub-labels, and bullets. Third format correction. The AI kept optimizing for fitting the page; Andrew kept optimizing for the person scanning it.
5. **14:40: Redundancy and flow.** Two catches. Claude's "Step 0: is the drop real?" had survived every revision since 13:32, and it contradicts the exercise, which hands the drop over as fact. A reader at the company would see the PM double-checking their own prompt. Andrew caught it by re-reading the source text one more time, the same move that caught the missing solution section at 13:45. Second, the brief's structure made the reader carry each tier in their head from section 4 to section 5 to find its fix. Andrew: embed the fix at the tier. Claude had organized by *type of content* (diagnosis, escalation, solutions); Andrew organized by *how the reader walks it*.
6. **14:52: No tables.** Claude's fix for the panning problem was a cross-reference column, which is still panning. Andrew: make it linear. Each hypothesis carries its own check, signal, and fix; drop the table; a memo has no grids. Claude's reflex under a page limit is to tabulate, because tables are dense. Andrew's point is that density is not legibility. Sixth correction, fifth on form.
7. **15:02: Visual grammar.** Three small legibility defects Claude shipped in the same render: numbered sub-labels that fought the section numbering, unlabelled Check / Signal / Fix, and bullets that visually attached to the wrong parent. Andrew caught all three from one read. He also named the meta-finding himself: most of the session was format, and the durable fix is a template, not more rounds. That observation is his and now sits on page 2.

## Attribution summary

- **Andrew:** scoping the tool to the right folder; the read-first / no-action constraint; the two-layer log design; the decision that the AI log is a deliverable in its own right; the PM-style constraints the brief must satisfy.
- **Andrew (work):** the reputation / bad-press hypothesis; the refusal to discredit the seller; elevating "recent release or UI change" into a hypothesis with a click-count / dwell-time signature; accepting the two diagnostic cuts as the starting frame.
- **Andrew (work, 13:38):** the step back before committing; the "I don't know what I don't know" framing that forces the brief to state its org assumptions; the worst-case design rule (assume every check fails, pre-define the escalation); the hand-off packet to avoid double work.
- **Andrew (work, 13:45):** re-reading the deliverable against what had been built and catching the uncovered requirement (solution direction). Claude had not flagged it. The per-tier solution structure is his.
- **Andrew (format, 13:59):** the one-page brief with all process material behind a disclaimer. Claude had stopped at "within the limit."
- **Andrew (audience, 14:03):** the two-page ceiling for the whole package; cutting the audit trail to a summary; the internal-reader register for the brief.
- **Andrew (structure, 14:13):** headers and bullets over paragraphs with bold labels; spotting the ligature copy defect from a paste.
- **Andrew (redundancy and flow, 14:40):** cutting Step 0 as contradicting a given; embedding solutions at each tier for a single read-through.
- **Andrew (memo form, 14:52):** no tables; hypothesis, check, signal, fix as one linear block each.
- **Andrew (visual grammar and the template insight, 15:02):** the three legibility fixes; the observation that the time went to format and that a template is the real remedy.
- **Claude:** read and summarized the PDF; independently flagged the AI-reflection weighting (convergent with Andrew's plan, not its source); drafted this log's structure.
- **Claude (work):** platform domain context (how buyers pay after a sale closes, and non-payment cancellations) that reframed cancellations as a possible payment event; the four causal structures; the challenge to the reputation hypothesis and its testable signature; the two diagnostic cuts; the first ranked hypothesis draft.

## Observations

- **Strength:** controls the tool's scope before letting it act (Prompts 1 and 2). Doesn't let the AI run ahead of the context.
- **Strength:** thinks about the grading criteria before the content. The AI reflection is treated as a first-class artifact from minute ~9.
- **Strength (15:02):** stepped outside the artifact to read his own timeline and named the pattern (format over substance) and the fix (a template). The AI had been logging the rounds without drawing the conclusion.
- **Strength (14:40):** third time returning to the source text (13:45, 14:03, 14:40), and it found something each time. Reading the prompt against the output is his most reliable move in this session. Claude never did it unprompted.
- **Strength (14:03):** consistent reader-first judgment. Twice in ten minutes he cut what the AI had over-built. The AI's failure mode here is completeness for its own sake; his correction is always "who reads this, and how much will they read."
- **Strength (13:59):** read the output as the reviewer would, not as the author. Two pages was inside the limit and Claude stopped there. One page plus clearly optional material respects the reader's time and makes the brief's density a feature.
- **Strength (13:45):** went back to the source document to audit coverage before drafting. Found a whole required section missing. Claude had been tracking the four bullets from the PDF summary at 13:14 and still did not raise it; the human did.
- **Strength (13:38):** resists the AI's momentum. Claude was ready to lock a ranking and move on; Andrew stopped to ask what was missing. The missing piece (org context and escalation design) was material. This is the clearest example in the session of the human steering rather than approving.
- **Strength (13:31):** when the AI supplied domain knowledge he did not have (the platform's payment model), he labelled it "adjacent to discovery" and something to verify. Did not adopt it as fact. This is the right posture and belongs in the reflection.
- **Gap, stated honestly (13:31):** domain is finance / accounting / cash processing, not marketplace payments. The AI filled a real knowledge gap here. The brief should own that rather than hide it.
- **To watch (resolved):** ~12 minutes spent on process setup before touching the problem. Final total was ~83 minutes, so setup was under a fifth of the session. Setup did not expand; the log became the AI-use note almost directly. The bet paid off.
- **Weakness, stated honestly:** Andrew did not independently verify any of the platform claims during the session (no web check, no reference). He mitigated by labelling them assumptions in the brief. In a real setting this is a day-one verification; in a timed hypothetical it was the right trade, but it is a trade.
- **Weakness, stated honestly:** the working notes ran to roughly four times the length of the final brief. That is a normal ratio for this style of work, but it means the compression step is where the time risk lives. Here it fit because the notes were already structured for the brief.

## Time summary

| Phase | Window | Minutes | Layer |
|---|---|---|---|
| Scope check, PDF read, log setup | 13:08–13:20 | 12 | PROCESS |
| Problem thinking: symptoms, cuts, hypotheses, ranking | 13:25–13:34 | 9 | WORK |
| Step back: org coverage and escalation ladder | 13:38–13:41 | 3 | WORK |
| Solution direction per tier, validation fold | 13:45–13:48 | 3 | WORK |
| Brief drafting, renders, six format rounds, final trim (active time) | 13:52–14:11, 14:28–15:25 | 50 | PROCESS + WORK |
| Gaps between turns (Andrew reading, reviewing renders, thinking, typing) | — | ~60 | — |
| **Total** | 13:08–15:25 | **137** | |

Budget was "a couple of hours." Delivered in about two hours, of which roughly 77 minutes were active work: ~12 setup, ~20 substance, the rest format.

## Files

Not included in this example: the exercise PDF, the final PDF, the brief, and the working notes.

- `final.pdf`: the deliverable, two pages, no tables: brief, then AI note with a what-I'd-change section
- `brief.md`, `retrospective.md`: sources for the two pages
- `session_log.md`: this file, the full local record (not in the PDF)
- `working_notes.md`: the uncompressed notes the brief was distilled from (not in the PDF)
