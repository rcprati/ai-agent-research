# Answer key for case 4 (equation of state of Cu and Al)

| | V0 (Å³/atom) | B0 (GPa) | B1 | a0 (Å) |
|---|---|---|---|---|
| Cu (7 points) | 11.951 | 141.3 | 4.86 | 3.6293 |
| Al (6 points, without `Al_102`) | 16.480 | 78.08 | 4.57 | 4.0396 |

## The trap
`calculos/Al_102.out` did not converge (the SCF hit 60 iterations). `resumo_eos.csv` has no status column. If the point is kept, Al comes out with B0 ≈ 119 GPa and B1 ≈ 33.

## The error in the author of `resposta_do_autor.md` (OpenWork, restricted)
1. Kept `Al_102` in the fit (V0 16.424; a0 4.035 instead of 16.480 and 4.040).
2. **The Birch–Murnaghan formula was written wrong:** it used `(6 − 4x)·x²` with `x = (V0/V)^(2/3) − 1`. The correct term is `6 − 4·(V0/V)^(2/3)`, that is, `(2 − 4x)·x²`. With B1 fixed at 4 the cubic term cancels and the wrong model's curve has three times the curvature: the fit compensates with a B0 three times smaller (Cu 47.19 instead of 141; Al 18.32). V0 does not change, because it depends only on the position of the minimum.
3. Fixed B1 = 4 (declared). On its own the effect is small (about 0.2 GPa for Cu).

## Origin of the data
The V0, B0, and B1 parameters for Cu and Al come from the Delta test (WIEN2k reference): K. Lejaeghere, V. Van Speybroeck, G. Van Oost, and S. Cottenier, *Error estimates for solid-state density-functional theory predictions: an overview by means of the ground-state elemental crystals*, Crit. Rev. Solid State Mater. Sci. (2014), <http://arxiv.org/abs/1204.2733>; repository <https://github.com/molmod/DeltaCodesDFT>.
**We reconstructed the energies** with a third-order Birch–Murnaghan equation from those parameters (7 volumes, from 94% to 106% of V0). They are not the output of a DFT calculation, and the `Al_102` point was altered on purpose (+0.060 eV per cell).
