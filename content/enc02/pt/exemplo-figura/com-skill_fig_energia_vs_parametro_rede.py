"""Energy vs. lattice parameter for PBE and PBE+D3 (data: dados_eos.csv)."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parent
plt.style.use(base / "figura-publicacao" / "scripts" / "pubstyle.mplstyle")

df = pd.read_csv(base / "dados_eos.csv")
markers = {"PBE": "o", "PBE+D3": "s"}

fig, ax = plt.subplots(figsize=(3.4, 2.6))  # one column, final size
for name, g in df.groupby("funcional", sort=False):
    ax.plot(g["a_A"], g["E_eV_atomo"], linestyle="none",
            marker=markers.get(name, "^"), label=name)

ax.set_xlabel(r"Lattice parameter, $a$ (Å)")
ax.set_ylabel(r"Energy, $E$ (eV/atom)")
ax.legend(loc="upper center")

fig.savefig(base / "eos_energia_vs_parametro_rede.pdf")
fig.savefig(base / "eos_energia_vs_parametro_rede_preview.png", dpi=200)
