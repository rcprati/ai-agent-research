---
name: check-inputs
description: Use before calculating a result from data files or calculation outputs (tables, CSV, DFT logs such as ORCA or VASP, machine learning results). Checks units, missing-data codes, summary tables, convergence, comparable parameters, target-derived columns, and scales, and ends by listing what was used, discarded, and not verified.
---

# Check inputs before calculating

## Steps

1. **Documentation.** Read every README and data dictionary in the folder before using the data.
2. **Summary table.** Never rely on the table alone. Open the source file of each row and check the value.
   If there is more than one candidate file for the same quantity, choose with a criterion and explain it.
3. **Calculations (DFT and similar).** Use only runs that ended well (converged, no errors).
   Compare method, functional, basis, ENCUT, and ISPIN across the files being combined; if they differ, do not combine.
   Use the **last** energy in the file, not the first. Check the units before converting.
4. **Data tables.** Check the unit of each column. Treat missing-data codes (-999, NA, 9999, empty)
   as missing, not as numbers. Count rows read and discarded.
5. **Machine learning.** Find out where each column comes from: none may be derived from the target.
   Standardize variables with different scales before distance-based methods (K-means, KNN).
   State the train/test split and seeds. A too-perfect result (R² near 1) is a reason to check.

## Before saying you are done

- **Run** the script and show the real output. Do not report a value the script did not print.
- List the files, lines, and columns **used**, and those **discarded, with the reason**.
- List every decision the request did not specify.
- Point out what was **not** verified.
