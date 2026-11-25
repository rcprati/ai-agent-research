#!/usr/bin/env python3
"""Ajusta a equação de estado de Birch–Murnaghan de 3ª ordem.

Entrada esperada: resumo_eos.csv, com colunas elemento, a_A,
V_celula_A3 e E_celula_eV. Os dados deste caso são células fcc
convencionais (4 átomos/célula); energias e volumes são convertidos
para valores por átomo antes do ajuste.
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

try:
    import numpy as np
    from scipy.optimize import curve_fit
except ImportError as exc:
    raise SystemExit(
        "Dependências ausentes. Instale com: python3 -m pip install numpy scipy"
    ) from exc


EV_A3_TO_GPA = 160.2176634
ATOMS_PER_CONVENTIONAL_FCC_CELL = 4


def birch_murnaghan_3(v, e0, v0, b0_ev_a3, bp):
    """Energia por átomo em eV como função do volume por átomo em Å³."""
    x = (v0 / v) ** (2.0 / 3.0) - 1.0
    return e0 + (9.0 * v0 * b0_ev_a3 / 16.0) * (
        bp * x**3 + (6.0 - 4.0 * x) * x**2
    )


def load_data(path):
    grouped = defaultdict(lambda: {"a": [], "v": [], "e": []})
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"elemento", "a_A", "V_celula_A3", "E_celula_eV"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"CSV precisa conter as colunas: {', '.join(sorted(required))}")
        for row in reader:
            item = grouped[row["elemento"]]
            item["a"].append(float(row["a_A"]))
            item["v"].append(float(row["V_celula_A3"]) / ATOMS_PER_CONVENTIONAL_FCC_CELL)
            item["e"].append(float(row["E_celula_eV"]) / ATOMS_PER_CONVENTIONAL_FCC_CELL)
    return grouped


def fit_element(data):
    v = np.asarray(data["v"], dtype=float)
    e = np.asarray(data["e"], dtype=float)
    a = np.asarray(data["a"], dtype=float)
    i_min = int(np.argmin(e))
    p0 = (e[i_min], v[i_min], 0.8, 4.0)
    # A faixa de volumes é estreita, então fixa-se B0' no valor usual 4
    # para manter o ajuste estável e evitar parâmetros não identificáveis.
    bp_fixed = 4.0

    def model(v_fit, e0, v0, b0_ev_a3):
        return birch_murnaghan_3(v_fit, e0, v0, b0_ev_a3, bp_fixed)

    bounds = ([-np.inf, v.min() * 0.8, 0.0],
              [np.inf, v.max() * 1.2, 10.0])
    params, covariance = curve_fit(
        model, v, e, p0=p0[:3], bounds=bounds, maxfev=100000
    )
    e0, v0, b0_ev_a3 = params
    # Para estrutura fcc, V_atomo = a³/4; logo a0 = (4 V0)^(1/3).
    a0 = (ATOMS_PER_CONVENTIONAL_FCC_CELL * v0) ** (1.0 / 3.0)
    residuals = e - model(v, *params)
    rmse_mev_atom = float(np.sqrt(np.mean(residuals**2)) * 1000.0)
    return {
        "V0": v0,
        "B0": b0_ev_a3 * EV_A3_TO_GPA,
        "a0": a0,
        "B0_prime": bp_fixed,
        "E0": e0,
        "rmse_meV_atom": rmse_mev_atom,
        "covariance": covariance,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="resumo_eos.csv", type=Path)
    args = parser.parse_args()

    for element, data in load_data(args.csv).items():
        result = fit_element(data)
        print(
            f"{element}: V0 = {result['V0']:.5f} Å³/átomo, "
            f"B0 = {result['B0']:.2f} GPa, a0 = {result['a0']:.5f} Å"
        )
        print(
            f"  (B0' = {result['B0_prime']:.3f}; "
            f"RMSE = {result['rmse_meV_atom']:.3f} meV/átomo)"
        )


if __name__ == "__main__":
    main()
