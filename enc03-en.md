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
5. **A case:** when the reviewer is wrong too, and a skill that helps
6. **Hands-on:** in pairs
7. Agreements for the next lesson

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
- We did not test its effect in the Lesson 1 cases; it is a **hypothesis**. Case 4 (ahead) brings a first test, and today's exercise tests it with your case

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
3. **Redo it** with an implementation **different** from the author's, compare with a reference, then run the author's script
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

# Case 4: equation of state of Cu and Al

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

**The request (restricted)**

> Write a python script that fits a Birch-Murnaghan equation of state to the data in `resumo_eos.csv` and reports V0, B0, and a0 for Cu and Al

**The data**
- 7 volumes per element, in a `resumo_eos.csv` and one `.out` per point
- The `.out` for Al at 102% of the volume says **"SCF DID NOT CONVERGE"**; the summary **does not** carry that warning

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

**Where the numbers come from**

The parameters (V0, B0, B1) for Cu and Al are those of the **Delta test** (WIEN2k reference): Lejaeghere, Van Speybroeck, Van Oost, and Cottenier, *Crit. Rev. Solid State Mater. Sci.* (2014).

<div class="mt-2">
<b>We reconstructed the energies</b> with Birch–Murnaghan from those parameters. <b>They are not DFT output</b>, and the Al point was altered on purpose.
</div>

<div class="mt-2">
Right answer: Cu <b>141.3 GPa</b>; Al <b>78.08 GPa</b> (without the unconverged point).
</div>

</div>
</div>

---

# The same request, three authors

<div class="text-sm">

| Author (1 run per cell) | Restricted request | Rewritten request |
|---|---|---|
| Claude (isolated agent) | correct | correct |
| Claude Haiku 5.5 | correct | correct |
| OpenWork · gpt-6-luna | **wrong** | correct |

</div>

<div class="mt-2 text-sm leading-6">

**What OpenWork got wrong with the restricted request**
- Kept the **unconverged** Al point (V0 16.424 instead of 16.480 Å³)
- **Wrote the formula wrong** (`6 − 4x` where it should be `6 − 4y`): Cu B0 **47** GPa instead of 141, Al 18 instead of 78
- Fixed B1 = 4 (it said so, but nobody asked)

</div>

<div class="mt-2 text-xs opacity-70 leading-5">
The formula error does not prove the restricted request caused the failure: it may have been luck. The rewritten request changed the <b>checking of the points</b>; one run cannot separate the effects.
</div>

---

# The author, when asked, defends the error

<div class="mt-2 text-base leading-8">

1. We asked it to **explain the formula**: it repeated it, wrong, as the standard form, citing Birch (1947)
2. We asked whether the Cu B0 was **consistent with the known value** (~140 GPa): it recognized the problem ("almost a factor of 3")
3. But it blamed **the data** ("shallow curve", few points), not the formula

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
Asking whoever did it to <b>check their own work</b> reproduces the reasoning. The data were fine: with the corrected formula (and B1 = 4), Cu gives 141.6 GPa.
</div>

---

# And the reviewer? Found the point, missed the formula

<div class="text-sm">

| Reviewer (Claude, 1 run) | `Al_102` | Formula | Its own "refit" |
|---|---|---|---|
| `review-result` skill (version 1) | found | **no** | Cu 47.1 · Al 26.0 |
| no skill ("review critically") | found | **no** | Al 26.1 |

</div>

<div class="mt-2 text-base leading-7">

- Both **reused the author's model**: their values are the right ones **÷ 3**. The "independent path" was not independent
- One of them saw the 47 GPa B0 and dismissed the warning ("synthetic data")
- What found the error was a **different formula + comparison with the reference**

</div>

---

# Amending the skill and testing again

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

**Step 3, before**

Reproduce the calculation without copying the author's script logic.

**Step 3, after**

Use an implementation **different** from the author's (another formulation, a library function, or a direct numerical calculation). Do not reuse the formula or the constants. If they differ, find out which one is right.

**Plausibility:** compare with a reference; if it is far off, **do not accept it by assumption**.

</div>
<div>

| Reviewer with the new skill | Verdict | Formula |
|---|---|---|
| wrong result #1 | not trustworthy | **found** |
| wrong result #2 | not trustworthy | **found** |
| **correct** result (control) | trustworthy | n/a |

Both redid it with a polynomial, reached Cu ≈ 141 and Al ≈ 78 GPa, and the disagreement led them to the formula.

</div>
</div>

<div class="mt-2 text-xs opacity-70 leading-5">
The amendment was written <b>after</b> seeing this error, and the retest is on the same case: it is an indication, not proof. The control used a different author (Claude Haiku).
</div>

---

# Our own skill, installed: `check-inputs`

<div class="text-sm leading-6">

**Same task and data as case 4**, restricted request, in OpenWork (`gpt-6-luna`). Two folders: no skill, and with `verificar-entradas` in `.agents/skills/`. The agent said it loaded the skill.

</div>

<div class="text-sm mt-1">

| Condition | Runs | `Al_102` discarded | Al B0 reported (right: 78.08) |
|---|---|---|---|
| No skill | 3 | **0 of 3** | 18.3 · 63.1 · 55.0 GPa |
| With `verificar-entradas` | 2 | **2 of 2** | 78.08 · 78.08 GPa |

</div>

<div class="mt-3 text-sm leading-6">

- With the skill, both agents **opened the `.out` of each summary row** and discarded the unconverged point
- Without the skill, none did that check: they read only `resumo_eos.csv`

</div>

---

# What the skill changed, and what it did not

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**With the skill (in the code)**
- Opens the `.out` of each row and requires "SCF convergido"
- **Compares** the summary's volume and energy with the source file
- Prints the **discarded rows, with the reason**

</div>
<div class="p-3 rounded-xl bg-red-50">

**Without the skill**
- Summary only; no convergence filter
- One run warned that B′ "hit the limit"; another **fixed B′ = 4** to avoid the limit: the symptom treated, the cause ignored

</div>
</div>

<div class="mt-2 text-sm leading-6">

**What did not change:** the wrong formula (1 of 3 without the skill) is not covered by it. What catches it is the reviewer with the amendment.

</div>

<div class="mt-2 p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs leading-5">
<b>Limits:</b> 2 runs against 3, no randomization or blinding, a single model. The best possible p-value with this arrangement is 0.1: it is an <b>indication</b>, not proof. The skill's code depends on the format of this case's <code>.out</code> files.
</div>

---

# What the test does not prove

<div class="mt-2 text-base leading-8">

- **Minimal control:** a single reviewer approved a **correct** result (from another author). A reviewer told to be critical may **reject what is right**, and that remains to be repeated
- **Different models:** the author was Antigravity and the reviewer, Claude. Part of the gain may come from their being different
- **Cases designed by us:** known traps, with documentation in the folder
- **One run** per cell, no statistics
- **The skill amendment came after the error**: it remains to be tested on a **new** method error
- **`verificar-entradas`** was tested in 2 runs against 3, without randomization
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

**No case of your own?** Use `caso-4-eos` from the downloads.

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
- Delta test (parameters for case 4): Lejaeghere, Van Speybroeck, Van Oost, Cottenier, *Crit. Rev. Solid State Mater. Sci.* (2014), <http://arxiv.org/abs/1204.2733> · <https://github.com/molmod/DeltaCodesDFT>
