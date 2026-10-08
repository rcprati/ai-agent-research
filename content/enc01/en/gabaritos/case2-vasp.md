# Answer key: case 2 (VASP, fictional data)

## Traps
- `summary.csv` uses `CO_gas_ecut400.OUTCAR` (**ENCUT = 400 eV**) for gas-phase CO; the other calculations use 520 eV.
  The correct file is `CO_gas.OUTCAR`.
- For CO/slab it uses `COslab_run1.OUTCAR`, a relaxation that **ended at the step limit** (NSW = 5),
  without the `reached required accuracy` line. The correct one is `COslab_run2.OUTCAR`.
- Each OUTCAR has **several energies** (one per ionic step); the **last** one counts.

## Correct result
E_ads = −361.600 − (−345.123) − (−14.780) = **−1.697 eV**.

## Typical error
Trusting `summary.csv`: E_ads = −361.15 + 345.123 + 14.512 = **−1.515 eV**. Negative and the right order of magnitude,
but off by 0.18 eV.

## Real test (Antigravity, restricted prompt, 1 run)
Read only `summary.csv` (opened no OUTCAR) and answered **−1.515 eV** with no warning.
