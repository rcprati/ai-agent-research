#!/usr/bin/env python3
"""Monta o site: compila os slides (Slidev), gera os zips e o index.html.

Uso: python3 scripts/build_site.py
Variáveis: GITHUB_REPOSITORY (owner/repo, define o --base), GA_TRACKING_ID (opcional).
"""
import html
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
REPO = os.environ.get("GITHUB_REPOSITORY", "owner/site").split("/")[-1]
GA = os.environ.get("GA_TRACKING_ID", "").strip()
LANGS = {"pt": "🇧🇷 Português", "en": "🇺🇸 English"}


def build_slides(md: str, out: str) -> bool:
    cmd = ["npx", "slidev", "build", md, "--base", f"/{REPO}/{out}/", "--out", str(DIST / out)]
    print("→", " ".join(cmd), flush=True)
    if subprocess.run(cmd, cwd=ROOT).returncode != 0:
        print(f"⚠️  build falhou para {md}; omitido do índice", file=sys.stderr)
        return False
    return True


def make_zip(src: Path, dest: Path) -> bool:
    if not src.is_dir():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, Path(src.name) / f.relative_to(src))
    return True


def readme_html() -> str:
    readme = ROOT / "README.md"
    if not readme.exists():
        return ""
    import mistune
    return f"<div class='info-box'>{mistune.html(readme.read_text(encoding='utf-8'))}</div>"


CSS = """
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#f8fafc;color:#1e293b;max-width:800px;margin:40px auto;padding:0 20px;line-height:1.6}
h1{color:#0f172a;border-bottom:2px solid #e2e8f0;padding-bottom:10px;font-size:1.8em}
h2{color:#0f172a;font-size:1.4em;margin-top:28px;border-bottom:1px solid #e2e8f0;padding-bottom:5px}
h3{font-size:1.05em;margin:14px 0 6px;color:#334155}
.info-box{background:#eff6ff;border:1px solid #bfdbfe;padding:20px 25px;border-radius:8px;margin:20px 0 30px}
.info-box h1,.info-box h2{border:0;margin-top:0}
.meeting{background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:18px 20px;margin:14px 0;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.meeting .date{color:#64748b;font-size:.9em}
.meeting .title{font-weight:600;font-size:1.1em;color:#0f172a;margin:2px 0 8px}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:6px 0}
.lang{font-size:.9em;color:#475569;min-width:110px}
.btn{padding:5px 13px;border-radius:6px;text-decoration:none;font-size:.88em;font-weight:500;color:#fff;background:#2563eb}
.btn:hover{background:#1d4ed8}
.btn.zip{background:#475569}.btn.zip:hover{background:#334155}
.note{font-size:.85em;color:#64748b}
.footer{margin-top:50px;font-size:.85em;color:#64748b;text-align:center;border-top:1px solid #e2e8f0;padding-top:16px}
"""


def main() -> None:
    cfg = json.loads((ROOT / "meetings.json").read_text(encoding="utf-8"))
    shutil.rmtree(DIST, ignore_errors=True)
    DIST.mkdir()
    cards = []
    for m in cfg["meetings"]:
        rows = []
        for lang, lang_name in LANGS.items():
            md = m["slides"].get(lang)
            out = m["id"] if lang == "pt" else f"{m['id']}-en"
            btns = []
            if md and (ROOT / md).exists() and build_slides(md, out):
                btns.append(f"<a class='btn' href='{out}/'>Slides</a>")
            for d in m.get("downloads", []):
                name = f"{m['id']}-{lang}-{d['dir']}.zip"
                if make_zip(ROOT / "content" / m["id"] / lang / d["dir"], DIST / "downloads" / name):
                    btns.append(f"<a class='btn zip' href='downloads/{name}' download>⬇ {html.escape(d['label'][lang])}</a>")
            if btns:
                rows.append(f"<div class='row'><span class='lang'>{lang_name}</span>{' '.join(btns)}</div>")
        cards.append(
            f"<div class='meeting'>"
            f"<div class='title'>{html.escape(m['title']['pt'])}<br><span class='note'>{html.escape(m['title']['en'])}</span></div>"
            + "".join(rows) + "</div>"
        )
    ga = ""
    if GA:
        ga = (f"<script async src='https://www.googletagmanager.com/gtag/js?id={GA}'></script>"
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}"
              f"gtag('js',new Date());gtag('config','{GA}');</script>")
    page = f"""<!DOCTYPE html>
<html lang="pt-BR"><head>{ga}<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(cfg['site_title']['pt'])}</title><style>{CSS}</style></head>
<body>
<h1>{html.escape(cfg['site_title']['pt'])}<br><span class='note' style='font-size:.55em'>{html.escape(cfg['site_title']['en'])}</span></h1>
{readme_html()}
<h2>Aulas / Lessons</h2>
{''.join(cards)}
<div class="footer">Atualizado via GitHub Actions · Material adaptado em parte de
<a href="https://github.com/walkinglabs/learn-harness-engineering">Learn Harness Engineering</a> (MIT) ·
Dados dos exemplos são sintéticos / Example data are synthetic</div>
</body></html>"""
    (DIST / "index.html").write_text(page, encoding="utf-8")
    print("OK:", DIST / "index.html")


if __name__ == "__main__":
    main()
