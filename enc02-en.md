---
theme: seriph
title: Skills in practice — Lesson 2
info: |
  AI coding tools in research.
  Lesson 2: read, build, and test a skill.
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

# Skills in practice

### Lesson 2 · Read, build, and test a skill

<div class="pt-10 opacity-70 text-sm">
AI coding tools in research
</div>

<!--
Welcome. Ask: who did the homework (analyze a skill from the list)? What did they see?
-->

---

# Today's plan

<div class="mt-6 text-lg leading-10">

1. **Recap** of Lesson 1
2. A **skill from the inside**
3. **Reading** real skills
4. **Building** ours: `check-inputs`
5. **Testing:** the same figure, without and with skill
6. **Hands-on:** your own skill
7. Agreements for the next lesson

</div>

---

# Recap of Lesson 1

<div class="mt-2 text-base leading-8">

- **Restricted** request ("…using `summary.csv`") → the agent read **only what was pointed to** → clean output, **no warning**
  <br><span class="text-sm opacity-70">ORCA, VASP, regression, and clustering: the same pattern in all four cases</span>
- With an **`AGENTS.md`**, the agent started opening the source files and reading the dictionary
- But the file **guarantees nothing**: in case 2 it reported the value **without running** the script
- An `AGENTS.md` with too many rules becomes a long text that the agent reads **every time**

</div>

<div class="mt-6 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center text-lg">
What if the check were <b>a reusable recipe</b>, loaded only when the task appears?
</div>

---

# A skill from the inside

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div>

```text
publication-figure/
├── SKILL.md        ← name, description, steps
├── scripts/
│   └── pubstyle.mplstyle  ← style (optional)
└── references/     ← details (optional)
```

</div>
<div class="leading-7">

**Three loading layers**
1. **Always:** `name` and `description` (a few lines)
2. **When the request matches:** the body of `SKILL.md`
3. **Only if needed:** `scripts/` and `references/`

The folder name must equal the `name`.

</div>
</div>

<div class="mt-2 text-xs leading-5">

**Where to install** (project · global; each skill in a `<name>/` subfolder)
- **Claude Code:** `.claude/skills/` · `~/.claude/skills/`
- **Antigravity:** `.agents/skills/` · `~/.gemini/config/skills/` (app and IDE) or `~/.gemini/antigravity-cli/skills/` (CLI)
- **OpenCode:** `.opencode/skills/` · `~/.config/opencode/skills/` (native); also reads `.claude/skills/` and `.agents/skills/`, in the project and globally

<span class="opacity-70">Tip: a skill in `.agents/skills/` works in Antigravity **and** OpenCode.</span>

</div>

<!--
Show the real folder from the materials (zip "Skill publication-figure"). Antigravity and OpenCode paths were supplied by the presenter (OpenCode: six locations, native + Claude Code-compatible + Agent Skills standard). Check them against the installed versions before the lesson.
-->

---

# Reading real skills (K-Dense)

<div class="text-sm">

| Skill | `SKILL.md` | Scripts | References |
|---|---|---|---|
| exploratory-data-analysis | 311 lines | 13 Python files (~130 KB) | 6 + 1 template |
| statistical-analysis | 453 lines | 1 | 5 |
| uncertainty-and-units | 415 lines | 7 Python files (~150 KB) | 7 |

</div>

<div class="mt-3 text-base leading-7">

- Long descriptions, in the **"use when…"** format
- Many **"do not"** rules: do not delete outliers, do not impute on your own, do not overwrite raw data
- They require Python 3.12+ and pinned libraries: a **barrier** for non-programmers
- A skill can instruct the agent **beyond the task** (the EDA one tells it to cite the K-Dense paper and query arXiv)

</div>

<div class="mt-2 text-xs opacity-60">
Read without installing: the EDA <code>SKILL.md</code>, part of <i>uncertainty-and-units</i>, and the headings of <i>statistical-analysis</i>. None was executed.
</div>

---

# What would they catch in our cases?

<div class="text-sm">

| Case | What the reading suggests |
|---|---|
| 1 · ORCA · 2 · VASP | Outside the scope of all three |
| 3A · leaked column | The "leakage audit" looks at **train/test overlap**, not a column derived from the target. But EDA requires a **data dictionary** with derivations |
| 3B · scale in K-means | Mentions recording transformations; does not say to standardize before distance |
| Missing (-999) | Covered by EDA: explicit code, no automatic imputation |
| Units in a table | *uncertainty-and-units* audits **Python code**, not columns of a CSV |

</div>

<div class="mt-3 text-center text-lg">
Reading, not testing. What was missing is a <b>small, specific skill</b> for our failures.
</div>

---

# What makes a good description

<div class="grid grid-cols-2 gap-5 mt-2 text-sm">
<div class="p-3 rounded-xl bg-red-50">

**Vague**
```yaml
description: Helps analyze data.
```
The agent does not know **when** to load it, or what to expect.

</div>
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**Specific, with triggers**
```yaml
description: Use before calculating a
  result from data files or calculation
  outputs (CSV, DFT logs, ML results).
  Checks units, missing codes,
  convergence...
```

</div>
</div>

<div class="mt-4 text-base leading-8">

- Say **when to use it** (file types, words in the request)
- Say **what it does** and what it delivers at the end
- Too-short descriptions do not trigger; too-long ones spend context

</div>

---

# Building ours: `check-inputs`

<div class="text-sm leading-6">

One page, text only, with six blocks:

1. **Documentation:** read every README and data dictionary before using the data
2. **Summary table:** open the source file of each row; never rely on the table alone
3. **Calculations (DFT):** only converged runs; same method, ENCUT, and ISPIN; the **last** energy
4. **Tables:** the unit of each column; missing codes (-999, NA) treated as absent
5. **Machine learning:** where each column comes from (nothing derived from the target); standardize before distance
6. **Before saying "done":** **run** the script, show the real output, list what was used, discarded, and **not verified**

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-sm">
Each step comes from a failure we <b>saw</b> in Lesson 1. Full file in the materials zip.
</div>

<!--
Show the real SKILL.md (materials/check-inputs/SKILL.md) and the Portuguese version verificar-entradas.
-->

---

# Another skill: figure for publication

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

The **same request** in both cases:

> Write a python script that makes a figure of energy versus lattice parameter, with both functionals, from `dados_eos.csv`, with the labels in English

**The skill says:**
- **vector** format (PDF), PNG only as a preview
- **no title** inside the plot (it goes in the paper's caption)
- fonts **≥ 8–9 pt at the final size**
- labels with **symbol and unit**
- **color and marker** (colorblind-safe)
- **reproducible** script, reading the data from the file

</div>
<div>

```text
publication-figure/
├── SKILL.md
└── scripts/
    └── pubstyle.mplstyle
```

<div class="text-xs opacity-70 leading-5">
The <code>pubstyle.mplstyle</code> file sets a single-column size (8.6 cm), fonts, palette, and PDF with embedded fonts. The agent only has to load it.
</div>

</div>
</div>

---

# The same figure, without and with the skill

<div class="grid grid-cols-2 gap-6 mt-1">
<div class="text-center">

<img src="/fig-sem-skill.png" style="height:230px;margin:0 auto" />

<div class="text-xs leading-5 mt-1"><b>Without skill</b> · PNG 1800 × 1350 px · default 10 pt font (≈ 5.7 pt in a column) · grid and framed legend</div>

</div>
<div class="text-center">

<img src="/fig-com-skill.png" style="height:230px;margin:0 auto" />

<div class="text-xs leading-5 mt-1"><b>With skill</b> · vector PDF · Arial embedded · 9–10 pt · 8.4 × 6.3 cm · no grid or frame</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70 leading-5">
Both at the same scale (one-column width). Two Claude runs with the same request; the one without the skill did not open the image to check it. Here the agent without the skill did not add a title, but the other rules did not come on their own.
</div>

<!--
Real figures generated by two isolated Claude runs (subagents) from dados_eos.csv (synthetic data), asking for English labels in both. The script and figures are in the "Figure example" zip. In Antigravity/OpenCode, repeat the test live: same request, without and with the skill installed.
-->

---

# Hands-on: your skill

<div class="grid grid-cols-2 gap-5 mt-2 text-sm">
<div class="leading-7">

Pick a task that **repeats** in your lab and draft:

1. The folder **name** (lowercase, hyphens)
2. **When to use it** (the description)
3. **4 to 6 steps**
4. **What to report** at the end
5. **A case with a known answer** to test it

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

```markdown
---
name: my-skill
description: Use when ... Does ... and delivers ...
---

# Title

## Steps
1. ...
2. ...

## Before saying you are done
- Run it and show the real output
- List used, discarded, not verified
```

</div>
</div>

---

# Checklist for a good skill

<div class="mt-2 text-lg leading-9">

☐ Does the description say **when** to use it?<br>
☐ Are the steps **short and verifiable**, not generic?<br>
☐ Does it say to **run and show the real output**?<br>
☐ Does it say what **not** to do (do not delete, do not invent)?<br>
☐ Was it **tested** on at least one case with a known answer?<br>
☐ Can someone who does not program **read and understand** the `SKILL.md`?

</div>

---

# Care with third-party skills

<div class="mt-2 text-base leading-8">

- Skills **run code** on your machine: read the `SKILL.md` **and the scripts** before installing
- Each skill's **license** (the repository may be MIT and the skill not)
- They may carry **embedded instructions** (cite papers, access the network): what does it ask the agent to do?
- Test in an **isolated folder**, with non-sensitive data
- Pin the **version** you tested: skills change

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
When you will not install it, <b>reading the SKILL.md</b> already teaches a lot about what the agent will do.
</div>

---

# For the next lesson

<div class="mt-4 text-lg leading-9">

- **Test** your skill on a real case and note what changed
- **Share** a skill (or the draft) in the shared repository
- **Bring** a case where the skill did **not** help

</div>

<div class="mt-6 p-3 rounded-xl bg-blue-50 border border-blue-200 text-base">
<b>Next lesson: asking well and reviewing.</b> How to write the request, what the agent sees (context), and the <b>independent reviewer</b>.
</div>

---

# References

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>
- Scientific Agent Skills (K-Dense-AI, MIT, license per skill): <https://github.com/K-Dense-AI/scientific-agent-skills>
