---
theme: seriph
title: Asking well and reviewing — Lesson 3
info: |
  AI coding tools in research.
  Lesson 3: asking well, managing context, and using an independent reviewer.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
colorSchema: light
fonts:
  sans: 'Inter'
---

# Asking well and reviewing

### Lesson 3 · The request, the context, and the independent reviewer

<div class="pt-10 opacity-70 text-sm">
AI coding tools in research
</div>

<!--
Welcome. Ask about the homework: who tested their own skill? Who brought a case where it did not help?
-->

---

# Today's plan

<div class="mt-6 text-lg leading-10">

1. **Feedback** on the homework
2. **Anatomy of a good request**
3. **Context:** what the agent sees
4. **The independent reviewer**
5. **Hands-on:** in pairs
6. Agreements for the next lesson

</div>

---

# Homework feedback

<div class="mt-4 text-lg leading-9">

- Did you **test** your skill on a real case?
  <br><span class="text-sm opacity-70">Did the agent load it? Did it change the result or only the form?</span>
- In which case did the skill **not** help?
- A third-party skill you **read** (without installing): what does it ask the agent to do?

</div>

<div class="mt-4 text-sm opacity-60">
Two or three short reports are a bridge to the rest of the lesson.
</div>

---

# The "restricted" requests from Lesson 1

<div class="text-sm">

| Case | The request |
|---|---|
| 1 · ORCA | "Write a python script that calculates the reaction energy of H2 + F2 → 2 HF in kcal/mol using `summary.csv`" |
| 2 · VASP | "…calculates the adsorption energy of CO on Pt(111) in eV… using `summary.csv`" |
| 3A · regression | "…trains a linear regression to predict `energy`… reports R² on test data" |
| 3B · clustering | "…clusters `clustering_data.csv` into 3 clusters with K-means and shows the size of each" |

</div>

<div class="mt-3 text-base leading-7">

- Each one said **what to do**, but not **what matters**: where the data comes from, what to check, what "done" means
- The agent did **exactly** what was asked, and failed silently

</div>

<!--
The original requests were in Portuguese and used the Portuguese file names; they are translated here.
-->

---

# Anatomy of a good request

<div class="grid grid-cols-2 gap-6 mt-2 text-base leading-8">
<div>

1. **Goal:** what you want to know or obtain
2. **Inputs:** which files, where they come from, what is reliable
3. **Done criterion:** what the result must satisfy
4. **Answer format:** value, files used and discarded, what was not verified
5. **Constraints:** what **not** to do (do not change data, do not invent)

</div>
<div class="p-4 rounded-xl bg-blue-50 border border-blue-200 text-sm leading-7">

A good request **does not guarantee** a correct result. It tells the agent **what matters**, and makes the checking **visible** in the report.

<div class="mt-2 opacity-70">
The instructions file (<code>AGENTS.md</code>) holds what applies to <b>every</b> request; the request holds what applies to <b>this one</b>.
</div>

</div>
</div>

---

# Before and after: case 1

<div class="grid grid-cols-2 gap-4 mt-1 text-xs leading-5">
<div class="p-3 rounded-xl bg-red-50">

**Restricted**

> Write a python script that calculates the reaction energy of H2 + F2 → 2 HF in kcal/mol using `summary.csv`

</div>
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**Rewritten**

> **Goal:** reaction energy of H2 + F2 → 2 HF, in kcal/mol.
> **Inputs:** the logs in the folder. `summary.csv` is from a colleague and may be outdated: check each row against its source log.
> **Done when:** only calculations that ended well and use the same method are included.
> **Answer:** the value, the files used and discarded (with the reason), and what you did not verify.
> **Do not:** change the files.

</div>
</div>

<div class="mt-3 text-sm leading-6">

- The rewritten request is **longer**, and that is the point: time spent writing is time not spent discovering the error later
- We did not test its effect on today's agents; it is a **hypothesis**, and today's exercise tests it with your case

</div>

---

# Context: what the agent sees

<div class="grid grid-cols-2 gap-6 mt-2 text-base leading-8">
<div>

- **The folder** it works in (files it decides to open)
- **`AGENTS.md`** / `CLAUDE.md`: read at the **start** of each session
- **Skills:** only the **name and description** are always there; the body comes in when the request matches
- **The history** of the session (what has been said and done)

</div>
<div class="p-4 rounded-xl bg-slate-100 text-sm leading-7">

What is **not** on this list, the agent **does not know**: your protocol, your colleague's email, what you saw in the lab.

<div class="mt-2">
If it matters, <b>write it down</b>: in the request, in <code>AGENTS.md</code>, or in a file in the folder (README, dictionary).
</div>

</div>
</div>

---

# Long session × fresh session

<div class="grid grid-cols-2 gap-5 mt-2 text-sm leading-7">
<div>

**Consider opening a fresh session when**
- the agent **repeats** an error you already corrected
- it starts to **forget** rules from the beginning
- the history got **huge** or full of attempts
- you are changing **task**

Before closing, ask for a **handoff summary**.

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

```markdown
# Session handoff
## Done
- (what was completed and how it was checked)
## Decisions
- (choices and the reason)
## To do
- (next steps)
## Files
- (which were read, created, and changed)
## Cautions
- (what went wrong, what not to trust)
```

</div>
</div>

---

# The independent reviewer

<div class="mt-2 text-base leading-8">

> The one who does it should not be the one who checks it.

The same model that writes the result tends to approve it. So the reviewer is **another session** (or another tool).

</div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm leading-7">
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**The reviewer receives**
- the original **request**
- the reported **result**
- the **script** and the **data**

</div>
<div class="p-3 rounded-xl bg-red-50">

**The reviewer does NOT receive**
- the **reasoning** of whoever did it
- the conversation of the original session

</div>
</div>

<div class="mt-3 text-xs opacity-70">
The idea comes from lesson 9 of the Learn Harness Engineering course (separating the one who does from the one who checks).
</div>

---

# The `review-result` skill

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

**Steps**
1. Understand the **request** and the reported result
2. **Read the data and documentation** before the author's reasoning
3. **Redo it** by an independent path, then run the author's script
4. Look for **silent failures:** files, parameters, units, missing values, leakage, scale, plausibility
5. **Do not fix** the author's work: point out and justify

</div>
<div class="p-3 rounded-xl bg-slate-100 text-sm leading-6">

**What it delivers**
- **Verdict:** trustworthy, not trustworthy, or inconclusive
- **Evidence:** files, lines, and values
- **The value you obtained**, if it differs
- **What was not verified**

</div>
</div>

---

# The test: reviewing the Lesson 1 errors

<div class="text-xs">

| Case | Author (Antigravity) | Correct | What the reviewers obtained |
|---|---|---|---|
| 1 · ORCA | −18.80 kcal/mol | −118.57 | **−118.57** (unconverged log) |
| 2 · VASP | −1.515 eV | −1.697 | **−1.697** (ENCUT 400; incomplete relaxation) |
| 3A · regression | R² 0.9982 | ≈ 0.6 | **0.638** (CV 0.565); leaked column, r = 0.9992 |
| 3B · clustering | 88/70/42 | 63/67/70 | **63/67/70** (no standardization) |

</div>

<div class="mt-3 text-base leading-7">

- **8 out of 8** reviewers (without and with the skill) caught the error and reached the correct value
- The skill changed the **form**: an explicit verdict and a list of what was not verified. Without it, the verdict on 3B was hesitant ("I do not fully trust it")
- In case 2 the reviewer even **decomposed** the error: +0.268 eV (ENCUT 400) and −0.450 eV (incomplete relaxation)

</div>

<div class="mt-1 text-xs opacity-60">
Reviewers: Claude (8 isolated runs). Authors: Antigravity. Each author's answer was reassembled from what it returned.
</div>

---

# What the test does not prove

<div class="mt-2 text-base leading-8">

- **There is no control:** we did not test reviewers on **correct** results. A reviewer told to be critical may **reject what is right**
- **Different models:** the author was Antigravity and the reviewer, Claude. Part of the gain may come from their being different
- **Cases designed by us:** known traps, with documentation in the folder
- **One run** per cell, no statistics
- The reviewer **can also be wrong**: its verdict does not replace your own check

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
The reviewer is a <b>second opinion</b>, not a guarantee. The final decision is still yours.
</div>

---

# Hands-on: in pairs

<div class="grid grid-cols-2 gap-5 mt-2 text-base leading-8">
<div>

**Person A (author)**
1. Pick a real task and write the request with the **five parts**
2. Run the agent and keep the **request, result, script, and data**

**Person B (reviewer)**

3. In a **fresh session**, give it to the agent with `review-result` (or with "review critically")
4. Read the verdict and **check one piece of evidence yourself**

</div>
<div class="p-3 rounded-xl bg-slate-100 text-sm leading-7">

**Then swap and talk**
- Did the reviewer find something the author did not see?
- Did it find something that was **not** a problem?
- Did the rewritten request change what the agent did?

</div>
</div>

---

# For the next lesson

<div class="mt-4 text-lg leading-9">

- **Use** the reviewer on one of your results and note: right, wrong, overzealous?
- **Bring** a request you rewrote and what changed
- **Share** a handoff summary or an `AGENTS.md` that worked

</div>

<div class="mt-6 text-sm opacity-70">
Possible topics: security and permissions · privacy and cost · traceability and reproducibility
</div>

---

# References

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>
