---
name: review-result
description: Use to independently review a result produced by another person or agent (a value, a table, a figure, or a conclusion), from the original request, the data, and the script. Reproduces the calculation on its own, looks for silent failures (wrong files, incompatible parameters, units, missing values, leakage, scale), and delivers a verdict with evidence.
---

# Independently review a result

You are the **reviewer**, not the author. Do not trust what the author says they did: check it.

## Steps

1. **Understand the request.** Read the original request and the reported result (value, table, conclusion).
2. **Do not start from the author's reasoning.** Read the data and all documentation in the folder yourself
   (README, data dictionary, protocols) before looking at how the author got the value.
3. **Redo it by an independent path.** Reproduce the calculation without copying the author's script logic.
   Then run the author's script and compare.
4. **Look for silent failures:**
   - did the author use **all** relevant files? does a summary table point to a file with a problem?
   - are the combined calculations **comparable** (same method, parameters) and did they **end well** (convergence)?
   - are **units** and **missing-data codes** (-999, NA) handled? did they use the right energy in the file (the last one)?
   - is any column **derived from the target** (leakage)? are variables on different **scales** before distance-based methods?
   - is the result **plausible** (order of magnitude, sign)? "Too good" or "too clean" is also a warning sign.
5. **Do not fix the author's work.** Point out and justify; do not change their data or scripts.

## What to deliver

- **Verdict:** trustworthy, not trustworthy, or inconclusive.
- **Evidence:** files, lines, and values that support the verdict.
- **The value or conclusion you obtained** independently, if it differs from the author's.
- **What you did not verify.**
