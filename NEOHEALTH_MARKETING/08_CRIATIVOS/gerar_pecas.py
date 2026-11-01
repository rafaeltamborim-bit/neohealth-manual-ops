#!/usr/bin/env python3
"""Gera as peças HTML editáveis (08_CRIATIVOS/pecas/**) e catalogo_criativos.csv.
Uso: python3 gerar_pecas.py   (depois: python3 render.py)
Cada peça é um HTML independente; edite o HTML diretamente ou os dados abaixo e regere.
"""
import os, csv, math, html
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "pecas")
NOTA = "Imagem da plataforma com dados fictícios (base de demonstração)"
CTA1 = "Solicite uma demonstração."
CTA2 = "Conheça o potencial dos dados da sua operadora."
FONT = "'Roboto Condensed','Arial Narrow','Carlito','Inter',sans-serif"
REG = (1090, 170, 830, 760)   # região da "tela" nas capas reais (x, y, w, h)
E = html.escape

P = {  # mensagens-âncora dos pilares
 "fin": "Sua operadora sabe exatamente onde estão os riscos financeiros e as oportunidades de melhoria?",
 "sin": "Não espere o fechamento do mês para identificar os fatores que pressionam a sinistralidade.",
 "ass": "Entenda como a utilização dos serviços de saúde impacta os resultados da sua operadora.",
 "reg": "Mais visibilidade sobre indicadores, obrigações e riscos regulatórios.",
 "pre": "Vá além da análise histórica. Utilize seus dados para antecipar cenários e apoiar decisões.",
 "marca": "Transforme dados em decisões. Decisões em resultados.",
}
CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#060A15}}
body{{font-family:{FONT};color:#fff;-webkit-font-smoothing:antialiased}}
.a{{position:relative;overflow:hidden;display:flex;
 background:radial-gradient(120% 90% at 85% 10%,rgba(65,144,211,.28),transparent 55%),radial-gradient(90% 70% at 0% 100%,rgba(169,239,229,.10),transparent 60%),linear-gradient(160deg,#0F172A,#060A15 70%)}}
.h{{font-weight:700;line-height:1.04;letter-spacing:-.005em}}
.h em{{font-style:normal;color:#A9EFE5}}
.s{{color:#b9c6da;line-height:1.2;font-weight:400}}
.btn{{display:inline-block;background:#5FBEEC;color:#060A15;font-weight:700;border-radius:999px;white-space:nowrap}}
.pill{{display:inline-block;border:1.5px solid rgba(169,239,229,.6);color:#A9EFE5;border-radius:999px;font-weight:700;white-space:nowrap}}
.note{{color:rgba(255,255,255,.55);line-height:1.15}}
.shot{{container-type:size;position:relative;overflow:hidden;border-radius:14px;border:1px solid rgba(95,190,236,.4);box-shadow:0 18px 50px rgba(65,144,211,.28);background:#0F172A}}
.shot img{{position:absolute;max-width:none;--iw:max(calc(100cqw*1920/var(--rw)),calc(100cqh*1920/var(--rh)));width:var(--iw);height:auto;
 left:calc(var(--iw)*var(--rx)/-1920 + (100cqw - var(--iw)*var(--rw)/1920)/2);
 top:calc(var(--iw)*9/16*var(--ry)/-1080 + (100cqh - var(--iw)*9/16*var(--rh)/1080)/2)}}
.logo{{border:0;box-shadow:none;border-radius:0;background:transparent}}
.logo img{{mix-blend-mode:screen}}
.card{{border:1.5px solid rgba(95,190,236,.35);background:rgba(15,23,42,.8);border-radius:18px}}
.num{{display:inline-flex;align-items:center;justify-content:center;border:1.5px solid rgba(169,239,229,.6);color:#A9EFE5;border-radius:12px;font-weight:700}}
"""
def page(w, h, body, title, extra=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>{E(title)}</title>
<!-- Peça editável NeoHealth BI · OPS. Fonte: Roboto Condensed (instale localmente para fidelidade; há fallbacks). Imagens: ../../assets_reais/ -->
<style>{CSS}{extra}</style></head><body>
{body}
</body></html>"""
def shot(asset, style="", reg=REG, cls=""):
    rx, ry, rw, rh = reg
    return f'<div class="shot {cls}" style="--rx:{rx};--ry:{ry};--rw:{rw};--rh:{rh};{style}"><img src="../../assets_reais/{asset}.jpg" alt="Capa real {asset} (dados fictícios)"></div>'
def logo(h):
    w = h * 400 / 70
    return shot("ini-01", f"width:{w:.0f}px;height:{h:.0f}px;flex:none", (130, 145, 400, 70), "logo")
def fs_fit(text, W, H, cap, fill=.62, k=.58):
    return max(10, min(cap, math.sqrt(fill * W * H / (max(len(text), 1) * k))))
def hl(text, fs, extra=""):
    return f'<div class="h" style="font-size:{fs:.0f}px;{extra}">{text}</div>'
def note(fs, extra=""):
    return f'<div class="note" style="font-size:{fs:.0f}px;{extra}">{NOTA}</div>'

# ---------- layouts ----------
def row(p):
    w, h = p["w"], p["h"]; pad = max(14, h * .09); colw = w * (.52 if w/h > 1.7 else .5) - pad
    big = h >= 200
    lh = max(18, h * .09)
    ht, sb = p["h1"], p.get("sub", "")
    HH = h - 2*pad - lh*1.2 - (h*.16 if big else 0) - (h*.22 if sb else 0)
    fs = fs_fit(ht, colw, max(HH, h*.25), h*.2)
    body = f'<div style="display:flex;flex-direction:column;justify-content:space-between;width:{colw:.0f}px;height:100%">'
    body += logo(lh)
    body += '<div>' + hl(ht, fs)
    if sb: body += f'<div class="s" style="font-size:{max(11, fs*.42):.0f}px;margin-top:{fs*.25:.0f}px">{sb}</div>'
    body += '</div>'
    bs = max(12, min(h * .055, 28))
    body += f'<div><span class="btn" style="font-size:{bs:.0f}px;padding:{bs*.5:.0f}px {bs*1.1:.0f}px">{p["cta"]}</span></div></div>'
    sx = w * (.52 if w/h > 1.7 else .5)
    body += f'<div style="position:absolute;left:{sx:.0f}px;top:{pad:.0f}px;width:{w-sx-pad:.0f}px;height:{h-2*pad-(h*.07):.0f}px">' + shot(p["asset"], "width:100%;height:100%") + '</div>'
    body += note(max(8, h*.028), f"position:absolute;left:{sx:.0f}px;bottom:{pad*.45:.0f}px")
    return f'<div class="a" style="width:{w}px;height:{h}px;padding:{pad:.0f}px">{body}</div>'

def col(p):
    w, h = p["w"], p["h"]; pad = w * (.07 if w > 500 else .08)
    story = p.get("story")
    top = 200 if story else 0; bot = 230 if story else 0
    share = p.get("share", .33)
    lh = max(18, w * .05 if w > 500 else 22)
    ht = p["h1"]; sb = p.get("sub", "")
    HW = w - 2*pad; HH = (h - top - bot) * share
    fs = fs_fit(ht, HW, HH, w * .1)
    bs = max(12, min(w * .04, 34)) if w > 500 else 13
    s = f'<div style="padding-top:{top}px"></div>'
    body = f'<div style="display:flex;flex-direction:column;width:100%;height:100%;padding:{pad:.0f}px {pad:.0f}px {pad*.6:.0f}px">{s}'
    body += logo(lh) + f'<div style="height:{lh*.8:.0f}px"></div>' + hl(ht, fs)
    if sb: body += f'<div class="s" style="font-size:{max(11, fs*.45):.0f}px;margin-top:{fs*.25:.0f}px">{sb}</div>'
    body += f'<div style="height:{pad*.5:.0f}px"></div>'
    if p.get("asset"): body += shot(p["asset"], "flex:1;min-height:60px;width:100%")
    body += f'<div style="margin-top:{pad*.5:.0f}px;display:flex;align-items:center;justify-content:space-between;gap:10px"><span class="btn" style="font-size:{bs:.0f}px;padding:{bs*.5:.0f}px {bs*1.1:.0f}px">{p["cta"]}</span></div>'
    body += note(max(8, w*.017 if w > 500 else 8), f"margin-top:{pad*.3:.0f}px;padding-bottom:{bot}px") if p.get("asset") else f'<div style="padding-bottom:{bot}px"></div>'
    body += '</div>'
    return f'<div class="a" style="width:{w}px;height:{h}px">{body}</div>'

def leader(p):
    w, h = p["w"], p["h"]; pad = 10
    fs = fs_fit(p["h1"], w*.5, h-12, h*.32, .8)
    body = f'<div style="display:flex;align-items:center;gap:16px;width:100%;padding:0 {pad+6}px">' + logo(h*.3)
    body += f'<div style="flex:1">{hl(p["h1"], fs)}</div><span class="btn" style="font-size:{h*.17:.0f}px;padding:{h*.1:.0f}px {h*.2:.0f}px">{p["cta"]}</span></div>'
    return f'<div class="a" style="width:{w}px;height:{h}px;align-items:center">{body}</div>'

def thumb(p):
    w, h = p["w"], p["h"]; pad = 56
    fs = fs_fit(p["h1"], 620, 330, 130, .7)
    body = f'<div style="display:flex;flex-direction:column;justify-content:space-between;width:640px;height:100%">'
    body += f'<div>{logo(34)}</div><div>{hl(p["h1"], fs)}</div>'
    body += f'<div><span class="pill" style="font-size:30px;padding:8px 24px">{p["tag"]}</span></div></div>'
    body += f'<div style="position:absolute;left:660px;top:{pad}px;width:{w-660-pad+20}px;height:{h-2*pad-26}px">' + shot(p["asset"], "width:100%;height:100%;border-width:2px") + '</div>'
    body += note(12, f"position:absolute;left:660px;bottom:{pad*.5:.0f}px")
    return f'<div class="a" style="width:{w}px;height:{h}px;padding:{pad}px">{body}</div>'

def cover(p):
    w, h = p["w"], p["h"]; pad = 110
    fs = fs_fit(p["h1"], 760, 380, 150, .7)
    body = f'<div style="display:flex;flex-direction:column;justify-content:space-between;width:800px;height:100%">'
    body += f'<div>{logo(64)}<div style="margin-top:34px"><span class="pill" style="font-size:30px;padding:8px 26px">{p["tag"]}</span></div></div>'
    body += f'<div>{hl(p["h1"], fs)}<div class="s" style="font-size:{fs*.4:.0f}px;margin-top:20px">{p["sub"]}</div></div>'
    body += f'<div><span class="btn" style="font-size:32px;padding:16px 36px">{p["cta"]}</span></div></div>'
    body += f'<div style="position:absolute;left:960px;top:150px;width:{w-960-80}px;height:{h-300}px">' + shot(p["asset"], "width:100%;height:100%;border-width:2px") + '</div>'
    body += note(18, "position:absolute;left:960px;bottom:70px")
    return f'<div class="a" style="width:{w}px;height:{h}px;padding:{pad}px 0 {pad}px {pad}px">{body}</div>'

def slide(sl, i, n, w=1080, h=1350):
    pad = 80; kind = sl.get("kind", "content")
    body = f'<div class="a slide" style="width:{w}px;height:{h}px"><div style="display:flex;flex-direction:column;width:100%;height:100%;padding:{pad}px">'
    body += f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(46)}<span class="s" style="font-size:28px">{i}/{n}</span></div><div style="height:50px"></div>'
    if sl.get("tag"): body += f'<div><span class="pill" style="font-size:28px;padding:6px 22px">{sl["tag"]}</span></div><div style="height:26px"></div>'
    fs = fs_fit(sl["h1"], w-2*pad, 330 if sl.get("asset") else 560, 120 if kind == "cover" else 92, .7)
    body += hl(sl["h1"], fs)
    if sl.get("txt"): body += f'<div class="s" style="font-size:{max(32, fs*.45):.0f}px;margin-top:26px">{sl["txt"]}</div>'
    if sl.get("items"):
        body += '<div style="margin-top:34px;display:flex;flex-direction:column;gap:18px">'
        for k, it in enumerate(sl["items"], 1):
            body += f'<div style="display:flex;align-items:center;gap:20px;font-size:40px"><span class="num" style="width:56px;height:56px;font-size:32px;flex:none">{k}</span><span>{it}</span></div>'
        body += '</div>'
    body += '<div style="flex:1"></div>'
    if sl.get("asset"): body += shot(sl["asset"], "width:100%;height:430px;flex:none") + note(18, "margin-top:10px")
    if sl.get("cta"): body += f'<div style="margin-top:30px"><span class="btn" style="font-size:40px;padding:20px 44px">{sl["cta"]}</span></div>'
    if sl.get("foot"): body += f'<div class="note" style="font-size:20px;margin-top:20px">{sl["foot"]}</div>'
    body += '</div></div>'
    return body

def build(p):
    L = p["layout"]
    if L == "row": return row(p)
    if L == "col": return col(p)
    if L == "leader": return leader(p)
    if L == "thumb": return thumb(p)
    if L == "cover": return cover(p)
    raise ValueError(L)

# ---------- peças ----------
pieces = []   # dicts: id, cat, fmt, w, h, h1, sub, cta, asset, canal, st, layout
def add(**k):
    k.setdefault("sub", ""); k.setdefault("cta", CTA1); k.setdefault("st", "Rascunho: aguardando aprovação")
    pieces.append(k)
FN = "[DISPONÍVEL] módulos citados (ficha de fatos)."
# Banners institucionais
B = "banners_institucionais"
add(id="BAN-01", cat=B, fmt="Banner institucional", w=1200, h=628, layout="row", h1="Transforme dados em <em>decisões</em>. Decisões em resultados.", asset="coc-01", canal="LinkedIn / Meta (link)", fn=FN)
add(id="BAN-02", cat=B, fmt="Banner de capa LinkedIn", w=1584, h=396, layout="row", h1="Inteligência estratégica para operadoras de planos de saúde", cta=CTA2, asset="mgd-01", canal="LinkedIn (página)", fn=FN)
add(id="BAN-03", cat=B, fmt="Billboard", w=970, h=250, layout="row", h1="Não espere o fechamento do mês", sub="para identificar os fatores que pressionam a sinistralidade.", asset="sin-01", canal="Google Display", fn="[DISPONÍVEL] Evolução da Sinistralidade.")
add(id="BAN-04", cat=B, fmt="Leaderboard", w=728, h=90, layout="leader", h1="Transforme dados em decisões.", cta="Solicite uma demonstração", asset="", canal="Google Display", fn=FN)
add(id="BAN-05", cat=B, fmt="Retângulo médio", w=300, h=250, layout="col", share=.34, h1="Onde estão os riscos e as oportunidades financeiras?", cta="Solicite uma demonstração", asset="con-02", canal="Google Display", fn="[DISPONÍVEL] Demonstrativo (DRE).")
add(id="BAN-06", cat=B, fmt="Half page", w=300, h=600, layout="col", share=.3, h1="Utilização que impacta o resultado", sub="Entenda como a utilização dos serviços de saúde impacta os resultados da sua operadora.", asset="ass-11", canal="Google Display", fn="[DISPONÍVEL] Estratificação de Risco.")
add(id="BAN-07", cat=B, fmt="Arranha-céu largo", w=160, h=600, layout="col", share=.34, h1="Visibilidade regulatória", cta="Demonstração", asset="ans-13", canal="Google Display", fn="[DISPONÍVEL] Sala de Situação ANS.")
add(id="BAN-08", cat=B, fmt="Hero do site", w=1920, h=600, layout="row", h1="Vá além da análise histórica", sub="Utilize seus dados para antecipar cenários e apoiar decisões.", asset="sin-08", canal="Site / landing page", fn="[DISPONÍVEL] Previsão da Sinistralidade (escopo dos modelos [A CONFIRMAR]).")
add(id="BAN-09", cat=B, fmt="Banner quadrado social", w=1080, h=1080, layout="col", share=.3, h1="Não é mais um BI de dashboards. É inteligência estratégica.", asset="mgd-01", canal="LinkedIn / Instagram", fn=FN)
add(id="BAN-10", cat=B, fmt="Retângulo grande", w=336, h=280, layout="col", share=.34, h1="Simule cenários antes de decidir", cta="Solicite uma demonstração", asset="sin-09", canal="Google Display", fn="[DISPONÍVEL] Simulador de Resultado.")
# Anúncios comerciais
A = "anuncios_comerciais"
add(id="ADS-01", cat=A, fmt="Anúncio feed quadrado", w=1080, h=1080, layout="col", share=.36, h1=P["fin"], asset="con-15", canal="LinkedIn Ads / Meta Ads", fn="[DISPONÍVEL] Resultado Operacional e EBITDA.")
add(id="ADS-02", cat=A, fmt="Anúncio feed quadrado", w=1080, h=1080, layout="col", share=.36, h1=P["sin"], asset="sin-10", canal="LinkedIn Ads / Meta Ads", fn="[DISPONÍVEL] Projetado x Real.")
add(id="ADS-03", cat=A, fmt="Anúncio feed quadrado", w=1080, h=1080, layout="col", share=.36, h1=P["ass"], asset="ass-12", canal="LinkedIn Ads / Meta Ads", fn="[DISPONÍVEL] Alto Custo e Gestão de Caso.")
add(id="ADS-04", cat=A, fmt="Anúncio feed quadrado", w=1080, h=1080, layout="col", share=.36, h1=P["reg"], asset="ans-03", canal="LinkedIn Ads / Meta Ads", fn="[DISPONÍVEL] Gestão de IDSS.")
add(id="ADS-05", cat=A, fmt="Anúncio link 1.91:1", w=1200, h=628, layout="row", h1=P["pre"], asset="sin-08", canal="LinkedIn Ads / Google Display", fn="[DISPONÍVEL] Previsão da Sinistralidade.")
add(id="ADS-06", cat=A, fmt="Anúncio link 1.91:1", w=1200, h=628, layout="row", h1="Do dado à decisão em uma única plataforma", sub="Financeira, sinistralidade, assistencial, regulatória e preditiva.", asset="coc-01", canal="LinkedIn Ads / Google Display", fn=FN)
add(id="ADS-07", cat=A, fmt="Anúncio link 1.91:1", w=1200, h=628, layout="row", h1="Ressarcimento ao SUS com mais visibilidade", asset="ans-15", canal="LinkedIn Ads", fn="[DISPONÍVEL] Ressarcimento ao SUS.")
add(id="ADS-08", cat=A, fmt="Anúncio feed vertical 4:5", w=1080, h=1350, layout="col", share=.3, h1="Glosas, auditoria e autorizações sob uma mesma leitura", sub="Apoio à análise de contas médicas e ao fluxo de autorizações.", asset="ass-35", canal="Meta Ads / LinkedIn Ads", fn="[DISPONÍVEL] Sugestão de Glosas na Rede.")
add(id="ADS-09", cat=A, fmt="Anúncio feed vertical 4:5", w=1080, h=1350, layout="col", share=.3, h1="Conheça o potencial dos dados da sua operadora", asset="mgd-01", cta=CTA2, canal="Meta Ads / LinkedIn Ads", fn="[DISPONÍVEL] Painel de Gestão.")
add(id="ADS-10", cat=A, fmt="Anúncio feed vertical 4:5", w=1080, h=1350, layout="col", share=.3, h1="Gestão de mensalidades e reajustes com mais clareza", asset="men-01", canal="Meta Ads / LinkedIn Ads", fn="[DISPONÍVEL] Gestão de Reajustes (Visão Geral).")
# Capas de vídeo e thumbnails
V = "capas_video"
for i, (t, sub, a, tag, r) in enumerate([
  ("Conheça a plataforma", "Painel de Gestão e Cockpit Executivo", "mgd-01", "Apresentação", 2),
  ("Inteligência financeira", "DRE, EBITDA, PEONA e inadimplência", "con-02", "Financeira", 4),
  ("Gestão assistencial", "Utilização e resultado da operadora", "ass-11", "Assistencial", 5),
  ("Análise preditiva", "Previsões e simuladores", "sin-08", "Preditiva", 7),
  ("Demonstração executiva", "Um percurso guiado pela plataforma", "coc-01", "Demo", 9)], 1):
    add(id=f"CAP-{i:02d}", cat=V, fmt="Capa de vídeo 16:9", w=1920, h=1080, layout="cover", h1=t, sub=sub, tag=tag, asset=a, canal=f"YouTube (roteiro {r:02d})", fn=FN)
T = "thumbnails_youtube"
for i, (t, tag, a, r) in enumerate([
  ("Dados em decisões", "Institucional", "coc-01", 1),
  ("Sinistralidade sem esperar o mês", "Sinistralidade", "sin-01", 3),
  ("Visibilidade regulatória", "ANS", "ans-13", 6),
  ("Integra com Tasy e Oracle", "Integração", "mgd-01", 8),
  ("Solicite uma demonstração", "Convite", "coc-01", 10)], 1):
    add(id=f"THB-{i:02d}", cat=T, fmt="Thumbnail YouTube", w=1280, h=720, layout="thumb", h1=t, tag=tag, asset=a, cta="", canal=f"YouTube (roteiro {r:02d})", fn="Integração Oracle/Tasy: informado pelo proprietário [A CONFIRMAR detalhes]." if r == 8 else FN)
# Stories
S = "stories"
st = [("Sua operadora sabe onde estão os riscos?", P["fin"], "con-02"), ("Não espere o fechamento do mês", P["sin"], "sin-01"),
 ("Utilização que impacta o resultado", P["ass"], "ass-11"), ("Visibilidade regulatória", P["reg"], "ans-13"),
 ("Vá além do histórico", P["pre"], "sin-08"), ("Transforme dados em decisões.", "Decisões em resultados.", "coc-01"),
 ("Cockpit Executivo", "A visão da diretoria em uma tela.", "coc-01"), ("Sala de Situação ANS", "Indicadores, obrigações e riscos reunidos.", "ans-13"),
 ("Simule cenários", "Teste hipóteses antes de decidir.", "sin-09"), ("Conheça o potencial dos dados da sua operadora", "", "mgd-01")]
for i, (h1, sub, a) in enumerate(st, 1):
    add(id=f"STO-{i:02d}", cat=S, fmt="Story 9:16", w=1080, h=1920, layout="col", story=True, share=.3, h1=h1, sub=sub, asset=a, cta=CTA2 if i == 10 else CTA1, canal="Instagram / Facebook Stories", fn=FN)
# Remarketing
R = "remarketing"
add(id="RMK-01", cat=R, fmt="Remarketing feed quadrado", w=1080, h=1080, layout="col", share=.34, h1="Ainda avaliando? Veja a plataforma com os dados da sua operadora.", asset="coc-01", canal="LinkedIn / Meta / Google Display (remarketing)", fn=FN)
add(id="RMK-02", cat=R, fmt="Remarketing feed 4:5", w=1080, h=1350, layout="col", share=.28, h1="Você conheceu a plataforma. Agora veja na prática.", sub="Uma demonstração conduzida para a realidade da sua operadora.", asset="sin-01", canal="LinkedIn / Meta (remarketing)", fn="[DISPONÍVEL] Evolução da Sinistralidade.")
add(id="RMK-03", cat=R, fmt="Remarketing link 1.91:1", w=1200, h=628, layout="row", h1="Conheça o potencial dos dados da sua operadora", asset="mgd-01", cta=CTA1, canal="Google Display (remarketing)", fn=FN)
add(id="RMK-04", cat=R, fmt="Remarketing retângulo médio", w=300, h=250, layout="col", share=.34, h1="Dados em decisões. Veja na prática.", cta="Solicite uma demonstração", asset="coc-01", canal="Google Display (remarketing)", fn=FN)
add(id="RMK-05", cat=R, fmt="Remarketing story", w=1080, h=1920, layout="col", story=True, share=.3, h1="Ainda tem dúvidas? Converse com a nossa equipe.", sub="Solicite uma demonstração e tire suas dúvidas.", asset="ans-13", canal="Instagram / Facebook Stories (remarketing)", fn=FN)

# ---------- carrosséis ----------
CAR = "carrosseis"
carousels = []
def car(i, titulo, canal, fn, slides): carousels.append((f"CAR-{i:02d}", titulo, canal, fn, slides))
car(1, "Os cinco pilares da inteligência para operadoras", "LinkedIn (documento/carrossel)", "[DISPONÍVEL] módulos da ficha de fatos", [
 dict(kind="cover", h1="Cinco pilares para decidir com <em>dados</em>", txt="Inteligência estratégica para operadoras de planos de saúde.", asset="coc-01"),
 dict(tag="1 · Financeira", h1="Riscos e oportunidades financeiras", txt=P["fin"], asset="con-02"),
 dict(tag="2 · Sinistralidade", h1="Sem esperar o fechamento", txt=P["sin"], asset="sin-01"),
 dict(tag="3 · Assistencial", h1="Utilização e resultado", txt=P["ass"], asset="ass-11"),
 dict(tag="4 · Regulatória", h1="Indicadores, obrigações e riscos", txt=P["reg"], asset="ans-13"),
 dict(tag="5 · Preditiva", h1="Antecipar cenários", txt=P["pre"], asset="sin-08"),
 dict(kind="cta", h1="Transforme dados em decisões. Decisões em resultados.", cta=CTA1, foot="Conheça o potencial dos dados da sua operadora.")])
car(2, "Cockpit Executivo: o que a diretoria vê", "LinkedIn / Instagram", "[DISPONÍVEL] Cockpit Executivo (tutorial coc-01)", [
 dict(kind="cover", h1="Cockpit Executivo: a visão da diretoria em uma tela", asset="coc-01"),
 dict(h1="Barra de ações e o que a tela mede", txt="Cada tela explica o que mede e como o número é calculado.", asset="coc-01"),
 dict(h1="Competência e recortes", txt="Ano, competência, grupo de contratos e produto como filtros.", asset="coc-01"),
 dict(h1="Cartões da carteira e cadastro de meta", txt="Cartões de carteira e resultado, com cadastro de meta.", asset="coc-01"),
 dict(h1="Gráficos que recortam a tela", txt="Ao interagir com o gráfico, a leitura se ajusta ao recorte.", asset="coc-01"),
 dict(kind="cta", h1="Veja o Cockpit com os dados da sua operadora", cta=CTA1)])
car(3, "Sinistralidade em cinco leituras", "LinkedIn / Instagram", "[DISPONÍVEL] Evolução da Sinistralidade (tutorial sin-01)", [
 dict(kind="cover", h1="Sinistralidade: cinco leituras da Visão Geral", asset="sin-01"),
 dict(h1="Onde fica e barra de ações", txt="Navegação do módulo e ações da tela.", asset="sin-01"),
 dict(h1="Regra do cálculo e filtros", txt="O número vem com a regra à vista e filtros analíticos.", asset="sin-01"),
 dict(h1="Cartões do período", txt="Beneficiários, receitas, resultado e ticket médio da competência.", asset="sin-01"),
 dict(h1="Operadora × mercado", txt="Comparativo com o mercado [A CONFIRMAR fonte].", asset="sin-01"),
 dict(kind="cta", h1="Não espere o fechamento do mês", txt="Identifique os fatores que pressionam a sinistralidade.", cta=CTA1)])
car(4, "Visibilidade regulatória", "LinkedIn", "[DISPONÍVEL] Sala de Situação ANS, IDSS, Ressarcimento ao SUS, RN 623 (normas: [VERIFICAR NA FONTE gov.br/ans])", [
 dict(kind="cover", h1="Mais visibilidade sobre indicadores, obrigações e riscos", asset="ans-13"),
 dict(tag="Sala de Situação ANS", h1="Indicadores reunidos em uma visão geral", asset="ans-13"),
 dict(tag="IDSS", h1="Gestão de IDSS", txt="Acompanhamento do índice e de seus componentes.", asset="ans-03"),
 dict(tag="SUS", h1="Ressarcimento ao SUS", txt="Visão dedicada ao tema.", asset="ans-15"),
 dict(tag="RN 623", h1="Gestão de atendimentos", txt="Acompanhamento da RN 623. Verifique a norma em gov.br/ans.", asset="ate-04"),
 dict(kind="cta", h1="Veja a visão regulatória na prática", cta=CTA1)])
car(5, "Da análise histórica ao cenário", "LinkedIn / Instagram", "[DISPONÍVEL] Projetado x Real, Previsão da Sinistralidade, Previsão da Produção, Simulador (escopo dos modelos [A CONFIRMAR])", [
 dict(kind="cover", h1="Vá além da análise histórica", txt="Antecipe cenários e apoie decisões.", asset="sin-08"),
 dict(tag="1", h1="Projetado × Real", txt="Compare o planejado com o realizado.", asset="sin-10"),
 dict(tag="2", h1="Previsão da Sinistralidade", txt="Veja cenários projetados. Previsões são estimativas.", asset="sin-08"),
 dict(tag="3", h1="Previsão da Produção", txt="Apoio ao planejamento assistencial.", asset="ass-06"),
 dict(tag="4", h1="Simulador de Resultado", txt="Teste hipóteses; o resultado depende dos parâmetros informados.", asset="sin-09"),
 dict(kind="cta", h1="Conheça o potencial dos dados da sua operadora", cta=CTA1)])

# ---------- infográficos (só conceitos) ----------
INF = "infograficos"
def inf_shell(title, inner, sub=""):
    return (f'<div class="a" style="width:1080px;height:1350px"><div style="display:flex;flex-direction:column;width:100%;height:100%;padding:80px">'
            f'{logo(46)}<div style="height:44px"></div>{hl(title, fs_fit(title,920,200,84,.7))}'
            + (f'<div class="s" style="font-size:34px;margin-top:18px">{sub}</div>' if sub else '') + f'<div style="height:40px"></div>{inner}<div style="flex:1"></div>'
            f'<div class="note" style="font-size:22px">Infográfico conceitual: descreve a estrutura do produto, sem números de desempenho. Resultados dependem da gestão de cada operadora.</div></div></div>')
def box(t, s="", extra=""): return f'<div class="card" style="padding:26px 30px;{extra}"><div class="h" style="font-size:42px">{t}</div>' + (f'<div class="s" style="font-size:28px;margin-top:8px">{s}</div>' if s else '') + '</div>'
arrow = '<div style="text-align:center;color:#5FBEEC;font-size:44px;line-height:1">&#9660;</div>'
inf = []
inf.append(("INF-01", "Dados, decisões, resultados", "[DISPONÍVEL] conceito de marca", inf_shell("Transforme dados em decisões. Decisões em resultados.",
  '<div style="display:flex;flex-direction:column;gap:14px">' + box("1 · Dados", "Financeiro, sinistralidade, assistencial, beneficiários, prestadores, autorizações e intercâmbio.") + arrow + box("2 · Decisões", "Leitura organizada, regra do cálculo à vista, alertas e simulações para apoiar a análise.") + arrow + box("3 · Resultados", "Dependem das ações e da gestão da operadora; a plataforma apoia a visibilidade.", "border-color:#A9EFE5") + '</div>')))
inf.append(("INF-02", "Os cinco pilares", "[DISPONÍVEL] pilares da marca", inf_shell("Cinco pilares de inteligência para operadoras",
  '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(f'<div class="card" style="padding:20px 26px;display:flex;gap:22px;align-items:center"><span class="num" style="width:64px;height:64px;font-size:38px;flex:none">{k}</span><div><div class="h" style="font-size:40px;color:#A9EFE5">{n}</div><div class="s" style="font-size:25px;margin-top:4px">{q}</div></div></div>' for k, (n, q) in enumerate([("Financeira", "Onde estão os riscos financeiros e as oportunidades de melhoria?"), ("Sinistralidade", "Quais fatores pressionam a sinistralidade, antes do fechamento do mês?"), ("Assistencial", "Como a utilização dos serviços impacta o resultado?"), ("Regulatória", "Indicadores, obrigações e riscos com mais visibilidade."), ("Preditiva", "Cenários antecipados para apoiar decisões.")], 1)) + '</div>')))
inf.append(("INF-03", "Da fonte à decisão", "[DISPONÍVEL] integração Oracle/Tasy e DuckDB conforme ficha; alertas WhatsApp/e-mail [A CONFIRMAR escopo]", inf_shell("Da fonte de dados à decisão",
  '<div style="display:flex;flex-direction:column;gap:14px">' + box("Fontes da operadora", "Oracle · ERP Philips Tasy") + arrow + box("Espelhamento analítico local", "DuckDB, para consultas analíticas") + arrow + box("Módulos de inteligência", "Financeiro · Sinistralidade · Assistencial · Regulatório · Preditivo") + arrow + box("Alertas e resumos", "WhatsApp e e-mail [A CONFIRMAR escopo]", "border-color:#A9EFE5") + '</div>')))
mods = ["Financeiro e contábil", "Sinistralidade", "Atuarial", "Beneficiários", "Assistencial", "Prestadores", "Autorizações e auditoria", "Glosas", "Intercâmbio PTU", "Indicadores ANS", "Simuladores", "Machine learning e previsões"]
inf.append(("INF-04", "Mapa de módulos", "[DISPONÍVEL] módulos da ficha (seção A)", inf_shell("Mapa de módulos da plataforma",
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">' + "".join(f'<div class="card" style="padding:24px 26px;font-size:36px;font-weight:700;{"border-color:#A9EFE5" if k%5==0 else ""}">{m}</div>' for k, m in enumerate(mods)) + '</div>', "Uma plataforma, vários módulos que conversam entre si.")))
inf.append(("INF-05", "Ciclo de gestão", "[DISPONÍVEL] conceito", inf_shell("O ciclo da decisão orientada por dados",
  '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(f'<div class="card" style="padding:20px 26px;display:flex;gap:22px;align-items:center"><span class="num" style="width:64px;height:64px;font-size:38px;flex:none">{k}</span><div><div class="h" style="font-size:40px">{n}</div><div class="s" style="font-size:26px;margin-top:4px">{d}</div></div></div>' for k, (n, d) in enumerate([("Observar", "Painéis e indicadores com a regra do cálculo à vista."), ("Entender", "Filtros e recortes para chegar aos fatores."), ("Simular", "Teste hipóteses e cenários antes de decidir."), ("Decidir", "A decisão permanece com a equipe da operadora."), ("Acompanhar", "Projetado x real, alertas e resumos.")], 1)) + '</div>')))

# ---------- escrita ----------
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)
catalog = []
def cat_row(i, fmt, size, text, cta, asset, canal, st, fn, arq):
    catalog.append([i, fmt, size, text, cta, asset, canal, st, fn, arq])
def strip(t): return html.unescape(t.replace("<em>", "").replace("</em>", ""))
for p in pieces:
    body = build(p)
    rel = f"pecas/{p['cat']}/{p['id']}.html"
    write(os.path.join(BASE, rel), page(p["w"], p["h"], body, p["id"]))
    txt = strip(p["h1"]) + ((" | " + p["sub"]) if p["sub"] else "")
    cat_row(p["id"], p["fmt"], f"{p['w']}x{p['h']}", txt, p["cta"], (p["asset"] + ".jpg") if p["asset"] else "(somente logotipo recortado de ini-01.jpg)", p["canal"], p["st"], p["fn"], rel)
for cid, titulo, canal, fn, slides in carousels:
    n = len(slides); sb = ""
    for k, sl in enumerate(slides, 1): sb += slide(sl, k, n) + "\n"
    rel = f"pecas/{CAR}/{cid}.html"
    write(os.path.join(BASE, rel), page(1080, 1350, f'<div style="display:flex;flex-direction:column;gap:0">{sb}</div>', cid))
    assets = ",".join(sorted({s["asset"] + ".jpg" for s in slides if s.get("asset")}))
    cat_row(cid, f"Carrossel ({n} slides)", "1080x1350 por slide", titulo + " | " + " / ".join(strip(s["h1"]) for s in slides), CTA1, assets, canal, "Rascunho: aguardando aprovação", fn, rel)
for iid, titulo, fn, content in inf:
    rel = f"pecas/{INF}/{iid}.html"
    write(os.path.join(BASE, rel), page(1080, 1350, content, iid))
    cat_row(iid, "Infográfico conceitual", "1080x1350", titulo, "(sem CTA; assinatura de marca)", "(somente logotipo recortado de ini-01.jpg)", "LinkedIn / Instagram", "Rascunho: aguardando aprovação", fn, rel)
catalog.sort(key=lambda r: r[0])
with open(os.path.join(BASE, "catalogo_criativos.csv"), "w", newline="", encoding="utf-8") as f:
    wr = csv.writer(f); wr.writerow(["ID", "formato", "tamanho", "texto", "CTA", "asset_usado", "canal", "status", "funcionalidades_e_status", "arquivo"]); wr.writerows(catalog)
print(len(catalog), "peças")
