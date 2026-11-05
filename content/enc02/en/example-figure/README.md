# Example: the same figure, without and with the skill

Real outputs from two isolated Claude runs with the same request (including "labels in English"), from `dados_eos.csv` (synthetic data; the scripts read that file, which is `eos_data.csv` in the English case folder):

- `without-skill_*`: script and PNG (1800 × 1350 px, 6 × 4.5 in, default matplotlib font, with grid).
- `with-skill_*`: script and vector PDF (8.4 × 6.3 cm, Arial embedded, no grid). The script loads the style from the `figura-publicacao/` folder (from the skill); to run it, copy the skill into the same folder and adjust the path if needed.

Files were renamed with the `without-skill_`/`with-skill_` prefix; the scripts write their outputs under the original names.
