"""Caso EOS v2: arquivos de saída por ponto (com status do SCF) + resumo_eos.csv SEM o status.
Parâmetros de referência: Delta test (WIEN2k), Lejaeghere et al., Crit. Rev. Solid State Mater. Sci. (2014),
https://github.com/molmod/DeltaCodesDFT . Energias reconstruídas por Birch-Murnaghan: NÃO são saída de DFT."""
import csv, os
EV_A3_GPA = 160.21766208
REF = {"Cu": (11.9511, 141.335, 4.86, -3.72), "Al": (16.4796, 78.077, 4.57, -3.74)}
def bm(V, V0, B0, B1, E0):
    x = (V0 / V) ** (2 / 3) - 1
    return E0 + 9 * V0 * B0 / 16 * (x**3 * B1 + x**2 * (6 - 4 * (x + 1)))
os.makedirs("pt/calculos", exist_ok=True)
rows = []
for el, (V0, B0g, B1, E0) in REF.items():
    B0 = B0g / EV_A3_GPA
    for f in [0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06]:
        V = V0 * f; a = (4 * V) ** (1 / 3); E = 4 * bm(V, V0, B0, B1, E0)
        bad = el == "Al" and f == 1.02
        if bad: E += 0.060
        nome = f"{el}_{int(round(f*100)):03d}.out"
        with open(f"pt/calculos/{nome}", "w") as fh:
            fh.write(f"EOS run  elemento={el}  escala_volume={f:.2f}\n")
            fh.write(f"celula fcc convencional, 4 atomos, a = {a:.5f} Ang, V = {4*V:.4f} Ang^3\n")
            fh.write("funcional PBE, celula fixa (sem relaxacao)\n")
            if bad:
                fh.write("SCF: 60 iteracoes (maximo atingido)\n")
                fh.write("AVISO: SCF NAO CONVERGIU; energia da ultima iteracao\n")
            else:
                fh.write(f"SCF: {11 + int(f*10) % 5} iteracoes\nSCF convergido (dE < 1e-6 eV)\n")
            fh.write(f"ENERGIA TOTAL (eV por celula): {E:.6f}\n")
        rows.append([el, f"{a:.5f}", f"{4*V:.4f}", f"{E:.6f}", f"calculos/{nome}"])
with open("pt/resumo_eos.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["elemento", "a_A", "V_celula_A3", "E_celula_eV", "arquivo"]); w.writerows(rows)
