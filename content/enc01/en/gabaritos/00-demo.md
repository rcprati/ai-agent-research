# Demo answer key (do not show beforehand)

## Traps
- `summary.csv` (from a colleague) points to `HF_run1.log`, which **did not converge** (`SCF NOT CONVERGED`)
  but still contains an energy. The good run is `HF_run2.log`, which the table does not cite.
- `HF_pbe.log` uses a different method (PBE), not comparable with the others (B3LYP).
- The unit (Eh) and the convergence only appear inside the logs, not in the table.
- Stoichiometry: 2 HF.

## Correct result
Use `H2.log`, `F2.log`, and `HF_run2.log`:
ΔE = 2·E(HF) − E(H2) − E(F2) = −0.1889 Eh ≈ **−118.6 kcal/mol** (B3LYP/def2-SVP, electronic only).
Reference: the experimental ΔH is about −128 kcal/mol.

## Typical errors
| What the agent did | Result |
|---|---|
| Trusted `summary.csv` (HF_run1, unconverged) | ≈ **−18.8** kcal/mol (looks plausible) |
| Used `HF_pbe.log` | ≈ **+6.1** kcal/mol (sign flipped) |

The most dangerous error is the first: the table looks trustworthy and the result is still exothermic.
Real tests (Antigravity): in the version with `converged`/`method`/`unit` columns, it got it right. In this version,
with the prompt "using summary.csv", it got it wrong (−18.80); with "using the files in this folder", it got it right.
The result depends on the prompt and the model; there is no guarantee.
