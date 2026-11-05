import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(here, "dados_eos.csv"))

fig, ax = plt.subplots(figsize=(6, 4.5))
for (name, g), marker in zip(df.groupby("funcional", sort=False), ["o", "s", "^", "d"]):
    g = g.sort_values("a_A")
    ax.plot(g["a_A"], g["E_eV_atomo"], marker=marker, ms=5, lw=1.5, label=name)

ax.set_xlabel("Lattice parameter (Å)")
ax.set_ylabel("Energy (eV/atom)")
ax.legend(title="Functional")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(here, "energia_vs_parametro_de_rede.png"), dpi=300)
