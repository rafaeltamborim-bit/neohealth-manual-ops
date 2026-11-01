#!/usr/bin/env python3
"""Protótipo LOCAL de lead scoring NeoHealth. Lê leads.csv + lead_scoring.csv e grava leads_pontuados.csv.
NÃO envia e-mail, NÃO chama APIs, NÃO acessa rede. Uso:
  python3 score_leads.py --leads leads_exemplo.csv --regras lead_scoring.csv --saida leads_pontuados.csv
Colunas esperadas em leads: id,email,tipo_operadora,porte,cargo,erp,desafios,interesse,consentimento_contato,concorrente,estudante
(desafios e interesse: valores separados por ';'). Dados de exemplo são FICTÍCIOS."""
import argparse, csv, unicodedata

FREE = {"gmail.com","hotmail.com","outlook.com","yahoo.com","yahoo.com.br","uol.com.br","bol.com.br","icloud.com","live.com"}

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()
    return " ".join(s.split())

def carregar_regras(path):
    regras, classes = {}, []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["dimensao"] == "classe":
                classes.append((r["valor"], int(r["pontos"])))
            else:
                regras.setdefault(r["dimensao"], {})[norm(r["valor"])] = (int(r["pontos"]), r["teto_dimensao"])
    return regras, sorted(classes, key=lambda x: -x[1])

def soma(regras, dim, valores):
    tab, tot, teto = regras.get(dim, {}), 0, None
    for v in valores:
        p = tab.get(norm(v))
        if p:
            tot += p[0]; teto = int(p[1])
    return min(tot, teto) if teto is not None else tot

def pontuar(l, regras, classes):
    det = {}
    for dim in ("tipo_operadora", "porte", "cargo", "erp"):
        det[dim] = soma(regras, dim, [l.get(dim, "")])
    for dim in ("desafios", "interesse"):
        det[dim] = soma(regras, dim, [x for x in (l.get(dim) or "").split(";") if x.strip()])
    total = sum(det.values())
    dom = (l.get("email", "").split("@")[-1] or "").lower()
    motivo = []
    if dom in FREE: total += regras["penalidade"][norm("E-mail pessoal/gratuito")][0]; motivo.append("email_gratuito")
    elim = False
    if norm(l.get("concorrente")) in ("sim", "s", "1", "true"): elim = True; motivo.append("concorrente")
    if norm(l.get("estudante")) in ("sim", "s", "1", "true"): elim = True; motivo.append("estudante")
    if norm(l.get("consentimento_contato")) not in ("sim", "s", "1", "true"): elim = True; motivo.append("sem_consentimento")
    total = max(0, min(100, total))
    classe = "Descarte"
    if not elim:
        for nome, corte in classes:
            if nome != "Descarte" and total >= corte: classe = nome; break
    return total, classe, det, ";".join(motivo)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leads", required=True); ap.add_argument("--regras", required=True); ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    regras, classes = carregar_regras(a.regras)
    with open(a.leads, newline="", encoding="utf-8") as f: leads = list(csv.DictReader(f))
    campos = list(leads[0].keys()) + ["score", "classe", "pts_tipo_operadora", "pts_porte", "pts_cargo", "pts_erp", "pts_desafios", "pts_interesse", "motivos_ajuste"]
    with open(a.saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos); w.writeheader()
        for l in leads:
            t, c, d, m = pontuar(l, regras, classes)
            l.update(score=t, classe=c, motivos_ajuste=m, **{"pts_" + k: v for k, v in d.items()})
            w.writerow(l)
    print(f"{len(leads)} leads pontuados -> {a.saida} (nada foi enviado)")

if __name__ == "__main__": main()
