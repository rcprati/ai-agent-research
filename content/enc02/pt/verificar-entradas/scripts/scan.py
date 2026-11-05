#!/usr/bin/env python3
"""Varredura mecânica de uma pasta de dados/resultados, antes de calcular.

Uso: python3 scripts/scan.py [pasta] [--lang pt|en]
Só lê arquivos de texto (biblioteca padrão), não altera nada e não usa a rede.
Sinaliza o que merece conferência; não prova que algo está errado nem certo.
"""
import csv, math, re, statistics, sys
from collections import defaultdict
from pathlib import Path

T = {
 "pt": {"docs": "Documentação (leia antes de usar os dados)", "nodocs": "Nenhum README ou dicionário de dados encontrado.",
  "noconv": "{f}: sinais de cálculo NÃO convergido ou terminado com erro ({m})",
  "noacc": "{f}: relaxação sem a linha 'reached required accuracy' (incompleta?)",
  "multi": "{f}: {n} energias no arquivo ({k}); vale a última (estrutura final), não a primeira",
  "diff": "Parâmetro '{p}' difere entre arquivos: {v}. Energias com parâmetros diferentes não se combinam",
  "missing": "{f}, coluna '{c}': {n} valor(es) com código de faltante ({t})",
  "scale": "{f}: escalas muito diferentes entre colunas ({a} ~{x:.3g} × {b} ~{y:.3g}). Padronize antes de métodos baseados em distância",
  "corr": "{f}: colunas '{a}' e '{b}' quase idênticas (|r|={r:.3f}). Possível vazamento do alvo ou duplicata; confira a origem",
  "neg": "{f}, coluna '{c}': {n} valor(es) negativo(s), mas o nome sugere grandeza positiva",
  "unit": "{f}, coluna '{c}': unidades misturadas ({u})", "none": "Nada a sinalizar (isso não prova que está tudo certo).",
  "ref": "{f}: a linha '{r}' aponta para {t}, que tem problema (veja acima). Não confie na tabela-resumo",
  "pm": "método", "head": "Varredura de", "flags": "Pontos de atenção"},
 "en": {"docs": "Documentation (read before using the data)", "nodocs": "No README or data dictionary found.",
  "noconv": "{f}: signs of an UNCONVERGED or errored calculation ({m})",
  "noacc": "{f}: relaxation without the 'reached required accuracy' line (incomplete?)",
  "multi": "{f}: {n} energies in the file ({k}); the last one counts (final structure), not the first",
  "diff": "Parameter '{p}' differs between files: {v}. Energies with different parameters should not be combined",
  "missing": "{f}, column '{c}': {n} value(s) with a missing-data code ({t})",
  "scale": "{f}: very different scales between columns ({a} ~{x:.3g} × {b} ~{y:.3g}). Standardize before distance-based methods",
  "corr": "{f}: columns '{a}' and '{b}' almost identical (|r|={r:.3f}). Possible target leakage or duplicate; check the origin",
  "neg": "{f}, column '{c}': {n} negative value(s), but the name suggests a positive quantity",
  "unit": "{f}, column '{c}': mixed units ({u})", "none": "Nothing to flag (this does not prove everything is fine).",
  "ref": "{f}: row '{r}' points to {t}, which has a problem (see above). Do not trust the summary table",
  "pm": "method", "head": "Scan of", "flags": "Points to check"}}
BAD = re.compile(r"NOT CONVERGED|error termination|SCF.*FAIL|did not converge", re.I)
MISSING = {"-999", "-9999", "9999", "na", "nan", "null", "n/a", "none", ""}
POSITIVE = re.compile(r"raio|radius|conc|massa|mass|volume|pressao|pressure", re.I)
DOC = re.compile(r"readme|dicion|dictionary|codebook|notas|notes", re.I)

def num(x):
    try: return float(x)
    except ValueError: return None

def pearson(a, b):
    if len(a) < 3: return 0.0
    ma, mb = statistics.fmean(a), statistics.fmean(b)
    sa = math.sqrt(sum((x-ma)**2 for x in a)); sb = math.sqrt(sum((y-mb)**2 for y in b))
    return 0.0 if sa == 0 or sb == 0 else sum((x-ma)*(y-mb) for x, y in zip(a, b))/(sa*sb)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lang = "en" if "--lang" in sys.argv and sys.argv[sys.argv.index("--lang")+1] == "en" else "pt"
    t = T[lang]; root = Path(args[0] if args and args[0] not in ("pt", "en") else ".")
    files = sorted(p for p in root.rglob("*") if p.is_file() and p.stat().st_size < 2_000_000 and not any(s.startswith(".") for s in p.parts))
    flags = []; badfiles = set(); refs = []; params = defaultdict(dict); docs = [p for p in files if DOC.search(p.name)]
    for p in files:
        try: text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError): continue
        name = str(p.relative_to(root))
        if DOC.search(p.name): continue
        m = BAD.search(text)
        if m: flags.append(t["noconv"].format(f=name, m=m.group(0))); badfiles.add(p.name)
        if "ionic step" in text and "reached required accuracy" not in text: flags.append(t["noacc"].format(f=name)); badfiles.add(p.name)
        for key, pat in (("ENCUT", r"ENCUT\s*=\s*([\d.]+)"), ("ISPIN", r"ISPIN\s*=\s*(\d)")):
            mm = re.search(pat, text)
            if mm: params[key][name] = mm.group(1)
        mm = re.search(r"^!\s*(.+)$", text, re.M)
        if mm: params[t["pm"]][name] = mm.group(1).strip()
        en = re.findall(r"(?:FINAL SINGLE POINT ENERGY|free\s+energy\s+TOTEN)\s*=?\s*(-?\d+\.\d+)", text)
        if len(en) > 1: flags.append(t["multi"].format(f=name, n=len(en), k=en[0] + " … " + en[-1]))
        if p.suffix.lower() in (".csv", ".tsv"):
            rows = list(csv.reader(text.splitlines(), delimiter="\t" if p.suffix.lower() == ".tsv" else ","))
            if len(rows) < 3: continue
            head, body = rows[0], rows[1:]; cols = list(zip(*[r + [""]*(len(head)-len(r)) for r in body]))
            numeric = {}
            for h, col in zip(head, cols):
                if re.fullmatch(r"arquivo|file|arquivo_origem", h.strip(), re.I):
                    for r_, v in zip(body, col): refs.append((name, r_[0], v.strip()))
                bad = [v for v in col if v.strip().lower() in MISSING]
                if bad: flags.append(t["missing"].format(f=name, c=h, n=len(bad), t=", ".join(sorted(set(b or "vazio/empty" for b in bad)))))
                vals = [num(v) for v in col]
                if all(v is not None for v in vals): numeric[h] = vals
                if POSITIVE.search(h) and any(v is not None and v < 0 for v in vals):
                    flags.append(t["neg"].format(f=name, c=h, n=sum(1 for v in vals if v is not None and v < 0)))
                if re.search(r"unidade|unit", h, re.I) and len(set(col)) > 1: flags.append(t["unit"].format(f=name, c=h, u=", ".join(sorted(set(col)))))
            mags = {h: statistics.median(abs(v) for v in vs) for h, vs in numeric.items() if any(vs)}
            hs = sorted(mags, key=mags.get)
            for a_, b_ in zip(hs, hs[1:]):
                if mags[a_] > 0 and mags[b_]/mags[a_] > 100:
                    flags.append(t["scale"].format(f=name, a=a_, x=mags[a_], b=b_, y=mags[b_])); break
            hs = list(numeric)
            for i in range(len(hs)):
                for j in range(i+1, len(hs)):
                    r = pearson(numeric[hs[i]], numeric[hs[j]])
                    if abs(r) >= 0.98: flags.append(t["corr"].format(f=name, a=hs[i], b=hs[j], r=abs(r)))
    for f_, r_, tgt in refs:
        if Path(tgt).name in badfiles: flags.append(t["ref"].format(f=f_, r=r_, t=tgt))
    for k, d in params.items():
        if len(set(d.values())) > 1:
            flags.append(t["diff"].format(p=k, v="; ".join(f"{f}={v}" for f, v in sorted(d.items()))))
    print(f"{t['head']} {root.resolve().name}/ ({len(files)} {'arquivos' if lang == 'pt' else 'files'})\n")
    print(t["docs"] + ":", ", ".join(str(d.relative_to(root)) for d in docs) if docs else t["nodocs"], "\n")
    print(t["flags"] + ":")
    for f in flags or [t["none"]]: print(" ⚠", f) if flags else print(" ", f)

if __name__ == "__main__":
    main()
