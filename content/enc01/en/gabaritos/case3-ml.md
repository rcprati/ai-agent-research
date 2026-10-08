# Answer key: case 3 (ML)

## Regression (prompt A)
- `previous_calc_energy` is practically the target (leakage); the dictionary says it is **not a descriptor**.
- Without it: test R² ≈ 0.5–0.65 (varies with the split). With it: ≈ 1.00.

## Clustering (prompt B)
- Very different scales (Å ~ 1; meV ~ 1000). K-means without standardizing: ARI ≈ 0.53; standardized: ≈ 0.96.
- Cluster sizes (measured): unstandardized ≈ 42 / 70 / 88; standardized ≈ 63 / 67 / 70. True groups: 70 / 70 / 60.
- Note: `radius_A` has 10 negative values (artifact of the synthetic data).

## Real tests (Antigravity, restricted prompts, 1 run each)
- A: read only 10 lines of the CSV, did not open the dictionary, used all columns: **R² = 0.9982**.
- B: did not standardize: **88 / 70 / 42**.
