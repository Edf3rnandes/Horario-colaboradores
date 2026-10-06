#!/usr/bin/env python3
"""Lê horario_colaborador.xlsx e gera index.html (planner) a partir de template.html."""
import json, re, sys
from pathlib import Path
import openpyxl

ROOT = Path(__file__).parent
XLSX = ROOT / "horario_colaborador.xlsx"
COURTS = {"Altiplano": 3, "Cabo Branco": 3, "Bancários": 2, "Bessa": 2}
DAYS = {"seg": "Seg", "ter": "Ter", "qua": "Qua", "qui": "Qui", "sex": "Sex", "sab": "Sab", "sáb": "Sab"}
PART = re.compile(r"^\s*([A-Za-zçáã/]+)\s+(\d{1,2}):(\d{2})\s*(?:às|as|-|–)\s*(\d{1,2}):(\d{2})\s*$", re.I)


def parse_horario(txt):
    slots = []
    for part in re.split(r"\s+e\s+", txt.strip()):
        m = PART.match(part)
        if not m:
            sys.exit(f"Horário não reconhecido: {txt!r} (trecho {part!r})")
        days, h1, m1, h2, m2 = m.groups()
        for d in days.split("/"):
            slots.append({"d": DAYS[d.lower()], "s": int(h1) * 60 + int(m1), "e": int(h2) * 60 + int(m2)})
    return slots


def clean(v):
    return re.sub(r"\s+", " ", v).strip() if isinstance(v, str) and v.strip() else None


def main():
    ws = openpyxl.load_workbook(XLSX)["Plan1"]
    classes = []
    for row in ws.iter_rows(min_row=3, min_col=2, max_col=8, values_only=True):
        unit, name, horario, cat, prof, a1, a2 = map(clean, row)
        if not name:
            continue
        classes.append({
            "id": len(classes) + 1, "q": 1, "unit": unit, "name": name, "horario": horario, "cat": cat,
            "slots": parse_horario(horario), "prof": prof, "aux": [a for a in (a1, a2) if a],
        })
    units = list(dict.fromkeys(c["unit"] for c in classes))
    ajustes = {}
    if (ROOT / "ajustes.json").exists():
        ajustes = json.loads((ROOT / "ajustes.json").read_text(encoding="utf-8"))
    for c in classes:
        a = ajustes.get("turmas", {}).get(f'{c["unit"]}|{c["name"]}')
        if a:
            c["prof"], c["aux"], c["q"] = a["prof"], a["aux"], a.get("q", 1)
    data = {"units": units, "classes": classes, "courts": COURTS,
            "funcoes": ajustes.get("funcoes", {}), "matriculas": ajustes.get("matriculas", {}), "pessoas": ajustes.get("pessoas", [])}
    html = (ROOT / "template.html").read_text(encoding="utf-8")
    html = html.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"{len(classes)} turmas em {len(units)} unidades -> index.html")


main()
