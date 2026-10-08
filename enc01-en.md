---
theme: seriph
title: AI Agents for Code in Research — Lesson 1
info: |
  AI coding tools (Claude Code, Antigravity, OpenCode).
  Lesson 1: what they are, where they fail silently, and how to check them.
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

# AI that writes code<br>for your research

### Lesson 1 · What works, where it fails silently, and how to check it

<div class="pt-10 opacity-70 text-sm">
No programming knowledge needed
</div>

<!--
[~0:00] Welcome. Ask who has used Claude Code, Antigravity or OpenCode, and who has never used any of them.
-->

---

# Today's plan

<div class="mt-6 text-lg leading-10">

1. What a **coding agent** is (and what it is not)
2. **Real cases:** the agent says "done"
3. **Silent failures** in research code
4. The main rule: **don't trust, verify**
5. The project's **instructions file** and **skills**
6. **Checklist** and agreements for the next lesson

</div>

---

# Chat × coding agent

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="p-5 rounded-xl bg-slate-100">

### Chat (ChatGPT, Claude.ai)
- You paste a snippet and get text back
- You copy it, run it, and come back with the error
- **You** run everything
</div>
<div class="p-5 rounded-xl bg-blue-50 border border-blue-200">

### Coding agent
- Reads the files in your folder
- **Runs commands**, creates and edits files
- Tries again on its own when something fails
- **Tells you when it thinks it is finished**
</div>
</div>

<div class="mt-8 text-center text-lg">
More autonomy = more productivity <b>and</b> more places for an error to slip by unnoticed.
</div>

<!--
[~0:10] Key point: the agent acts on your folder. That is useful, but it changes your role: from the person who writes to the person who reviews.
-->

---

# Claude Code, Antigravity and OpenCode: the same idea

| | Claude Code | Google Antigravity | OpenCode |
|---|---|---|---|
| Where it runs | Terminal, desktop app, IDE extensions | Its own editor (IDE) and CLI | Terminal, desktop app, IDE extension |
| What it does | Reads, edits, runs commands | Same, with an agent panel | Same |
| Cost | Subscription or API key | Limited free quota | **Free, open-source** tool; the cost comes from the model |
| Instructions file | `CLAUDE.md` | `AGENTS.md` / `GEMINI.md` | `AGENTS.md` (the `/init` command creates it) |
| Reusable skills | Yes | Yes | Yes |

<div class="mt-4 text-sm opacity-70 leading-6">
Everything we cover today applies to all three. What changes is where to click, the cost, and the name of the instructions file.<br>
OpenCode works with many model providers (with an API key, and free or local models when available: check). Another free option, from a different category:
<a href="https://anythingllm.com/">AnythingLLM</a>, a private local assistant for chatting with your documents (we did not check whether it edits project files).
</div>

<!--
Check before the lesson: Antigravity names and paths change between versions (IDE × CLI). Third-party sources indicate the IDE started reading AGENTS.md from v1.20.x (March 2026); confirm in the official documentation.
-->

---

# Case 1: the request (DFT, ORCA)

<div class="mt-2 text-sm opacity-70">Antigravity · Gemini 3.1 Pro (low) · a folder with 5 DFT logs and a <code>summary.csv</code> (synthetic data)</div>

<div class="mt-6 p-5 rounded-xl bg-slate-100 text-lg leading-8">

> Create a python script that calculates the reaction energy of **H2 + F2 → 2 HF** in kcal/mol using `summary.csv`

</div>

<div class="mt-6 text-lg text-center">
A common request: someone hands over a summary spreadsheet and asks for the analysis.<br>
<b>What could go wrong?</b>
</div>

<!--
[~0:20] Ask the audience for 2 or 3 guesses before showing the answer. Data and answer key: materials/demo and materials/answer-keys/00-demo.md. Script and variations: materials/demo-script.md.
Note: the original run, including the prompt and the agent's output, was in Portuguese; it is translated into English on these slides.
Note: the model was Gemini 3.1 Pro (low) in Antigravity; confirm before the lesson.
-->

---

# The agent's answer

```text
=== Reaction Energy Calculation ===
Reaction: H2 + F2 -> 2 HF
E(H2):    -1.173525 Hartree
E(F2):  -199.343845 Hartree
E(HF):  -100.273666 Hartree
------------------------------------
ΔE (Hartree):     -0.029962
ΔE (kcal/mol):   -18.801425
```

<div class="mt-4 p-4 rounded-xl bg-green-50 border border-green-200">
"The final reaction energy calculated is <b>-18.80 kcal/mol</b>. The script is ready in your directory."
</div>

<div class="mt-4 text-center text-lg">
It ran without errors. Sign and order of magnitude look reasonable. <b>Would you trust it?</b>
</div>

---

# What was behind it

<div class="grid grid-cols-2 gap-6 mt-2 text-sm">
<div>

### `summary.csv`
```text
molecule,file,energy
H2,H2.log,-1.173525
F2,F2.log,-199.343845
HF,HF_run1.log,-100.273666
```

### `HF_run1.log`
```text
*   ERROR: SCF NOT CONVERGED AFTER 2 CYCLES  *
Total Energy (last cycle)  -100.273665650111 Eh
****ORCA finished by error termination****
```

</div>
<div class="text-base leading-8">

- The HF line came from a calculation that **did not converge**
- There was a **converged** `HF_run2.log` that the table did not mention
- The agent read **only the table**, as asked, and **warned about nothing**

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Correct result: <b>−118.6 kcal/mol</b><br>
<span class="text-sm opacity-70">the agent gave −18.8: wrong by a factor of 6, and still exothermic</span>
</div>

</div>
</div>

---

# Same request, different results

| Run | Request | Result |
|---|---|---|
| Antigravity · Gemini 3.1 Pro (low) | "…using `summary.csv`" | **−18.80** (wrong) |
| Antigravity | "…using the files in this folder; say which ones you used and why" | −118.57 (right) |
| Claude (6 isolated agents) | both requests, 3 runs each | **−118.57** (6 out of 6 right) |

<div class="mt-4 text-base leading-8">

- The agents that got it right **opened the logs on their own**; the one that got it wrong did not
- **Few runs:** this is not a ranking of tools. It shows that the result **varies**
- With the right answer known, the error is easy to see. **What if you did not know it?**

</div>

<!--
Methodological honesty: the "isolated Claude agents" were subagents, not interactive Claude Code; 6 runs, on this problem only. The same agents do not always get other problems right. The point is variability and the need to verify, not which tool is better.
Note: three subagents described the error that "would result" from the CSV with made-up numbers (-55, -56, -80); the real value is -18.80.
-->

---

# Case 2: adsorption energy (VASP, fictional data)

<div class="mt-1 text-sm opacity-70">Antigravity · same kind of request · five <code>OUTCAR</code> files and a <code>summary.csv</code></div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm">
<div>

> Write a python script that calculates the adsorption energy of CO on Pt(111) in eV, E_ads = E(CO/slab) − E(slab) − E(CO gas), using `summary.csv`

```text
Adsorption Energy Calculation
E(CO/slab) :   -361.150 eV
E(slab)    :   -345.123 eV
E(CO gas)  :    -14.512 eV
E_ads      :     -1.515 eV
```

</div>
<div class="leading-7">

**What was behind it**
- CO gas: the summary uses a calculation with **ENCUT = 400 eV**; the others use **520**
- CO/slab: a relaxation that **stopped at the step limit** (no `reached required accuracy`)
- The agent **did not open a single OUTCAR**

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Correct: <b>−1.697 eV</b> · agent: <b>−1.515 eV</b><br>
<span class="text-xs opacity-70">right sign and order of magnitude, off by 0.18 eV</span>
</div>

</div>
</div>

<!--
Fictional data (simplified VASP-style files, not real output). The original run was in Portuguese; the prompt and output are translated here. Answer key: materials/answer-keys/case2-vasp.md. Confirm the model used in this run.
-->

---

# Case 3: machine learning (synthetic data)

<div class="mt-1 text-sm opacity-70">Antigravity · two CSVs and a <code>data_dictionary.txt</code> that it <b>did not read</b></div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm">
<div>

**A) Linear regression**
> …predict `energy` using `regression_data.csv` and report R² on test data

R² = **0.9982** (80/20 split chosen by the agent)

**B) K-means with 3 clusters**
> …cluster `clustering_data.csv` into 3 clusters and show the size of each

Cluster 0: **88** · Cluster 1: **70** · Cluster 2: **42**

</div>
<div class="leading-7">

**What the dictionary said** (translated)
```text
previous_calc_energy  ... derived from the
  target itself; NOT a descriptor
radius_A     ... values around 1
energy_meV   ... values around 1000
```

- **A)** with the leaked column: R² ≈ 1.00. Without it: **0.5–0.65**
- **B)** without standardizing: 88 / 70 / 42. Standardized: **63 / 67 / 70**

</div>
</div>

<!--
In both runs the agent saw only the first 10 lines of the CSV and did not open the dictionary. The runs used the Portuguese originals (file and column names); the English files in the downloads are translations. Answer key: materials/answer-keys/case3-ml.md. Confirm the model used.
-->

---

# The same pattern, four times

| Case | What the agent read | Answered | Correct |
|---|---|---|---|
| 1 · DFT (ORCA) | only `summary.csv` | −18.80 kcal/mol | −118.6 |
| 2 · DFT (VASP) | only `summary.csv` | −1.515 eV | −1.697 |
| 3A · regression | 10 lines of the CSV | R² = 0.9982 | 0.5–0.65 |
| 3B · clustering | 10 lines of the CSV | 88 / 70 / 42 | 63 / 67 / 70 |

<div class="mt-4 text-base leading-8">

- Restricted request → read **only what was pointed to** → clean output, **no warning at all**
- The error was not in the calculation, but in what the agent **did not look at**
- In none of the cases did the output give the problem away

</div>

<div class="mt-2 text-xs opacity-60">Antigravity, one run per case. When the request let the agent open the logs (case 1), it got it right.</div>

---

# The problem: it sounds confident, even when wrong

<div class="mt-4 text-lg leading-8">

The agent writes the code, runs it, sees "no errors" and answers:

<div class="my-4 p-4 rounded-xl bg-green-50 border border-green-200 italic">
"The final reaction energy is -18.80 kcal/mol. The script is ready."
</div>

- Running **without errors** ≠ calculating **correctly**
- The agent rates its own work optimistically, even when a human observer would judge it poor
- The longer the task, the bigger the gap between "looks done" and "is correct"

</div>

<div class="absolute bottom-6 text-xs opacity-60">
Idea from lesson 9 of the Learn Harness Engineering course (walkinglabs, MIT)
</div>

---

# Silent failures in research code

<div class="grid grid-cols-2 gap-x-8 gap-y-3 mt-4 text-base">

<div class="p-3 rounded-lg bg-red-50">📏 <b>Swapped units</b><br><span class="text-sm opacity-70">mM treated as µM, degrees as radians</span></div>
<div class="p-3 rounded-lg bg-red-50">🕳️ <b>Missing data turned into a number</b><br><span class="text-sm opacity-70">-999, NA, blanks going into the average</span></div>
<div class="p-3 rounded-lg bg-red-50">📂 <b>File not read</b><br><span class="text-sm opacity-70">analyzed 3 of the 10 files and did not say so</span></div>
<div class="p-3 rounded-lg bg-red-50">🎭 <b>Invented data or references</b><br><span class="text-sm opacity-70">cites a paper or a value that does not exist</span></div>
<div class="p-3 rounded-lg bg-red-50">🔧 <b>Method swapped without notice</b><br><span class="text-sm opacity-70">a different statistical test, filter or tolerance</span></div>
<div class="p-3 rounded-lg bg-red-50">✂️ <b>Changed what you did not ask for</b><br><span class="text-sm opacity-70">"improved" the script and changed the result</span></div>

</div>

<div class="mt-6 text-center">
In every case the code <b>runs</b> and delivers a number that looks like an answer.
</div>

<!--
[~0:35] Ask the class for their own examples. Write them down for the next lesson.
-->

---

# The main rule: don't trust, verify

<div class="mt-4 text-lg leading-9">

1. **Reproduce what you already know.** Run the method on a case with a known answer
2. **Check plausibility.** Order of magnitude, sign, units
3. **Ask for a data accounting.** How many rows did it use? Which did it drop? Why?
4. **Demand evidence of execution.** The command and the real output, not "it should work"
5. **Redo one calculation by hand.** One or two points, independently

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
"The agent said it's done" is <b>not</b> a verification.
</div>

---

# The one who does it should not be the one who checks it

<div class="grid grid-cols-2 gap-8 mt-6">
<div>

### The problem
The same model that wrote the code tends to approve its own work.

</div>
<div>

### What to do
- Open **another session** and ask for a critical review of the result
- Or use **another tool** (Claude reviews Antigravity, and vice versa)
- Give the reviewer the result and the data, **not** the first session's reasoning
- Ask explicitly: "look for errors, be demanding"

</div>
</div>

<div class="mt-8 text-center opacity-80">
And in the end, the final reviewer is <b>you</b>: responsibility for the result lies with whoever signs it.
</div>

---

# The project's instructions file

<div class="mt-4 text-lg leading-8">

A text file in the project folder that the agent reads **at the start of every session**.

- Context: what the project is, where the data and results live
- Rules: what it may and may not do
- **Definition of "done":** what it must prove before saying it has finished

</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-center text-sm">
<div class="p-3 rounded-lg bg-slate-100"><code>CLAUDE.md</code><br>Claude Code</div>
<div class="p-3 rounded-lg bg-slate-100"><code>AGENTS.md</code><br>open standard; Antigravity and others</div>
<div class="p-3 rounded-lg bg-slate-100"><code>GEMINI.md</code><br>specific to Antigravity</div>
</div>

<div class="mt-4 text-sm opacity-70">
Tip: write one <code>AGENTS.md</code> and create a <code>CLAUDE.md</code> containing only the line <code>@AGENTS.md</code>. That way both tools read the same content.
</div>

<!--
[~0:55] Show materials/AGENTS.md and materials/CLAUDE.md. Keep it short: long files are partly ignored; a few clear rules work better.
-->

---

# Example: the part that matters most

```markdown
## Working rules
- Do only what was asked. Do not "improve" what was not requested.
- Never invent data, references or values.
- Log every exclusion or transformation of data (what, how many rows, why).
- Check units and missing-data codes (-999, NA, blank) before calculating.

## Definition of "done"
You may only say you are finished when:
- [ ] the code was run and the real output was shown;
- [ ] the method reproduces the reference result (expected value: [VALUE ± TOLERANCE]);
- [ ] you listed what was discarded, converted or assumed;
- [ ] you pointed out what was NOT verified.
```

<div class="mt-4 text-sm opacity-70">
Full template: <code>materials/AGENTS.md</code> (adapted from the Learn Harness Engineering course template, MIT)
</div>

---

# Does the instructions file change the result?

<div class="mt-1 text-sm opacity-70">Antigravity · same restricted requests · <code>AGENTS.md</code> <b>without mentioning any of the traps</b> (generic) or mentioning them (specific)</div>

| Case | No file | Generic | Specific |
|---|---|---|---|
| 1 · ORCA | −18.80 ✗ | −118.57 ✓ | −118.57 ✓ |
| 2 · VASP | −1.515 ✗ | −1.697 ✓* | −1.697 ✓* |
| 3A · regression | R² 0.9982 ✗ | R² 0.638 ✓ | – |
| 3B · clustering | 88/70/42 ✗ | 67/70/63 ✓† | – |

<div class="mt-3 text-base leading-7">

- With **general** rules, the agent started opening the source files, comparing ENCUT and convergence, and **reading the data dictionary** on its own
- It listed what it used, what it discarded, and **what it did not verify**
- But the file **guarantees nothing**: in case 2 it reported the value **without running** the script

</div>

<div class="mt-2 text-xs opacity-60 leading-5">
✗ wrong · ✓ right · – not tested yet · * did not run the script · † repeated in a fresh session; result reproduced from the agent's script (its answer was not recorded)<br>
One run per cell. Claude subagents (9 runs in case 3, told to read the file) got everything right; without the file, in case 1, they also did (6 of 6): the gain for them is unclear.
</div>

<!--
Full results and per-run notes: testes-agents/RESULTADOS.md. The "Instruções lidas." canary confirms the file was loaded. Fill in the "–" cells when the Antigravity quota returns; The original runs were in Portuguese; numbers are the same.
-->

---

# Do I have to write everything from scratch?

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div class="p-4 rounded-xl bg-slate-100">

### The problem
- Each project has its own `AGENTS.md`, but **many tasks repeat** across projects and labs
  - checking units and missing data
  - validating against a reference result
  - checking citations, standardizing figures
- Writing and **improving** this alone, every time, is repeated work
- An `AGENTS.md` full of rules becomes a long text that the agent **reads in full, every time**

</div>
<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

### The way out
- **Package** each task once, in a separate file
- **Reuse** what other people have already written
- **Share** what works in your lab
- Load the recipe **only when the task comes up**

</div>
</div>

<div class="mt-6 text-center text-xl">
Can I use other people's instructions? <b>Yes, and it has a name: skill.</b>
</div>

<div class="mt-3 text-center text-sm opacity-70">
But be careful: third-party skills run code on your machine and quality varies. Read before using.
</div>

<!--
Transition between "instructions file" and "skill". Stress: AGENTS.md = rules for YOUR project (always apply); skill = a recipe for ONE task, reusable. Mention up front that public collections exist (list in skills-candidates.md) and that we will build our own.
-->

---

# So what is a "skill"?

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div>

A **reusable recipe** for a specific task, kept in a folder:

```text
check-units/
├── SKILL.md      ← name, description, steps
└── scripts/      ← (optional) supporting code
```

- The agent reads only each skill's **name and description**
- When your request matches, it **loads** the whole skill and follows the steps (and the folder is easy to **share**)

</div>
<div class="p-4 rounded-xl bg-slate-100">

### Project instructions × skill
| | `AGENTS.md` | Skill |
|---|---|---|
| When it applies | **Always**, in the project | **On demand** |
| Used for | General rules | One specific task |
| Lives in | Project folder | Your machine or the project |

</div>
</div>

```markdown
---
name: check-units
description: Use when reading numeric data: looks for mixed units and missing-data codes (-999, NA).
---
List the units of each column, look for -999/NA/9999 and report them before calculating.
```

<!--
Point: a skill is just a text file (plus, sometimes, a script). It is not an installed program or a magic plugin.
Claude Code reads skills from .claude/skills/<name>/SKILL.md (project) or ~/.claude/skills/ (personal). The SKILL.md format is an open standard, and the K-Dense repository claims compatibility with Antigravity; confirm the installation path in Antigravity before the lesson. OpenCode: `.opencode/skills/<name>/SKILL.md` or `~/.config/opencode/skills/` (third-party source; confirm at opencode.ai/docs/skills).
Warning: third-party skills run code on your machine; read before installing.
-->

---

# Skills that might be useful

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm">
⚠ <b>A list of candidates. None of these skills has been tested or verified by us.</b> Skills run code on your machine:
read the <code>SKILL.md</code> and the scripts before installing, and check the license.
</div>

<div class="grid grid-cols-2 gap-x-6 gap-y-2 mt-3 text-xs leading-5">
<div>

**Verification and rigor**
Uncertainty & Units · Statistical Analysis · Experimental Design · Statistical Power · `review-paper-code`

**Writing and LaTeX**
Scientific Writing · Venue Templates · Citation Management · Peer Review

**Literature**
Paper Lookup · Literature Review · pyzotero · MarkItDown (PDF → text)

</div>
<div>

**Data and figures**
Scientific Visualization · Matplotlib · Seaborn · `scientific-figure-making`

**Chemistry and materials**
RDKit · pymatgen · Cantera · OpenMM · and 35 computational chemistry skills (VASP, CP2K, Quantum ESPRESSO, xTB, LAMMPS, DeePMD)

**Reproducibility**
DataLad · Nextflow · LaminDB

</div>
</div>

<div class="mt-3 text-xs opacity-70 leading-5">
Sources: <a href="https://github.com/K-Dense-AI/scientific-agent-skills"><code>K-Dense-AI/scientific-agent-skills</code></a> (177 skills, MIT, license per skill) · <a href="https://github.com/jinzhezenggroup/computational-chemistry-agent-skills"><code>jinzhezenggroup/computational-chemistry-agent-skills</code></a> (LGPLv3) · <a href="https://github.com/ChenLiu-1996/figures4papers"><code>ChenLiu-1996/figures4papers</code></a> (license to be confirmed) · <a href="https://github.com/claesbackman/AI-research-feedback"><code>claesbackman/AI-research-feedback</code></a> (MIT)<br>
Full annotated list: <code>skills-candidates.md</code>
</div>

<!--
The names come from the repositories' READMEs; nothing was installed or run. Idea: pick 2 or 3 to test with the lesson's cases. The K-Dense skill list may be incomplete (the page was long). Check the licenses before redistributing anything.
-->

---

# Checklist: before accepting the result

<div class="mt-2 text-lg leading-9">

☐ Does it reproduce something I already know?<br>
☐ Is the number plausible (order of magnitude, sign, units)?<br>
☐ Did it use all the data? Did it drop anything? Why?<br>
☐ Did it really run? Did it show the real output?<br>
☐ Did it touch anything I did not ask for?<br>
☐ Did I redo one calculation by hand?<br>
☐ Did I ask for a second opinion (another session or tool)?

</div>

<div class="mt-4 text-sm opacity-60">materials/checklist.md</div>

---

# For the next lesson

<div class="mt-4 text-lg leading-9">

- **Task:** use the agent on **one** real task of your own and note what it got wrong or let slip
- **Bring:** a case of silent failure (or a surprising success)
- **Analyze one skill** from the list: **no need to install it**; just open the `SKILL.md` and look at the content and structure (what it asks for, what it does, what is missing)
- **Share:** a prompt, an `AGENTS.md` or a skill that worked
- **Shared repository:** to keep prompts, configurations and skills

</div>

<div class="mt-6 text-sm opacity-70">
Possible topics: reusable skills · how to ask well · agents on long tasks · use with sensitive data
</div>

---

# References

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>
