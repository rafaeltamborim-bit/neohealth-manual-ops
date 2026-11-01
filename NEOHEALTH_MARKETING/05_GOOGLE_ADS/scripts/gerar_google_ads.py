# -*- coding: utf-8 -*-
"""Gera CSVs (Google Ads Editor) e campanhas/*.md; verifica limites de caracteres. Rodar: python3 gerar_google_ads.py"""
import csv, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOM = "https://DOMINIO-A-CONFIRMAR"   # [A CONFIRMAR] domínio/landing definitivos (03_SITE_LANDING_PAGE)
COMUNS = ["Solicite uma demonstração","Transforme dados em decisões","Decisões em resultados","NeoHealth BI · OPS",
          "Veja a plataforma em ação","Conheça o potencial dos dados","Inteligência para operadoras"]
NEG_GERAIS = ["vaga","vagas","emprego","estágio","salário","curso","cursos","treinamento","certificação","faculdade","tcc","monografia",
 "grátis","gratuito","download","pdf","apostila","tutorial","youtube","hospital","clínica","consultório","prontuário","laboratório","farmácia",
 "plano de saúde individual","cotação","comparar planos","carteirinha","segunda via","boleto","telefone","reclamação","convênio médico","enfermagem","residência"]
CAMPS = [
 dict(slug="bi-operadoras", nome="GS - BI para operadoras de planos de saúde", orc=300, lp="bi-operadoras",
  grupos={"BI operadoras":["bi para operadoras de planos de saúde","business intelligence operadora de saúde","bi para operadora de saúde","bi operadoras saúde suplementar"],
          "Software plataforma operadora":["software para operadora de planos de saúde","sistema de gestão para operadoras de saúde","plataforma de inteligência para operadoras","software gestão operadora saúde"],
          "Dashboard operadora":["dashboard para operadora de saúde","painel de indicadores operadora de saúde","cockpit executivo operadora","dashboard gestão plano de saúde"]},
  h=["BI para operadoras de saúde","Plataforma para operadoras","Painel executivo da operadora","Financeiro e sinistralidade","Visão assistencial e ANS","Dados da operadora num painel","Mais visibilidade na gestão","Cockpit para gestores"],
  d=["Plataforma de inteligência estratégica para operadoras. Solicite uma demonstração.","Visão financeira, sinistralidade, assistencial e regulatória em um só lugar.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["power bi download","excel"], path=("bi-operadoras","demonstracao")),
 dict(slug="bi-tasy", nome="GS - BI para Philips Tasy", orc=200, lp="bi-philips-tasy",
  grupos={"BI Tasy":["bi para tasy","bi philips tasy","business intelligence tasy","bi tasy operadora de planos de saúde"],
          "Dados Tasy operadora":["dados do tasy operadora de saúde","integração tasy bi","análise de dados tasy","relatórios tasy operadora"],
          "Dashboard Tasy":["dashboard tasy financeiro","tasy plano de saúde indicadores","painel gerencial tasy operadora"]},
  h=["BI para operadoras com Tasy","Dados do Tasy em painéis","Integração com Philips Tasy","Do ERP à decisão","Seus dados do ERP, mais claros","Painéis financeiros e ANS","Indicadores do seu ERP","Análise além dos relatórios"],
  d=["Plataforma de BI para operadoras com integração a ERP Philips Tasy. Peça uma demonstração.","Leve os dados do seu ERP a painéis de sinistralidade, finanças e regulação.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["suporte tasy","login tasy","tasy ehr hospital","vaga tasy","curso tasy","treinamento tasy","tasy prontuário"], path=("bi-tasy","demonstracao")),
 dict(slug="indicadores-operadoras", nome="GS - Indicadores para operadoras", orc=150, lp="indicadores-operadoras",
  grupos={"Indicadores operadora":["indicadores para operadoras de saúde","indicadores de gestão operadora de saúde","indicadores de desempenho operadora","kpis operadora de planos de saúde"],
          "Indicadores setoriais":["indicadores financeiros operadora de saúde","indicadores assistenciais operadora","indicadores de sinistralidade"],
          "Painel de indicadores":["painel de indicadores ans","indicadores operadora planos de saúde dashboard"]},
  h=["Indicadores para operadoras","KPIs da sua operadora","Painel de indicadores","Indicadores financeiros","Indicadores assistenciais","Indicadores de sinistralidade","Indicadores em um só painel","Acompanhe indicadores-chave"],
  d=["Acompanhe indicadores financeiros, assistenciais e regulatórios da operadora em um painel.","Mais visibilidade sobre os indicadores que importam para a gestão. Peça demonstração.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["kpi rh","indicadores educação"], path=("indicadores","demonstracao")),
 dict(slug="gestao-sinistralidade", nome="GS - Gestão de sinistralidade", orc=200, lp="gestao-sinistralidade",
  grupos={"Gestão de sinistralidade":["gestão de sinistralidade","controle de sinistralidade operadora","como controlar sinistralidade operadora","gestão da sinistralidade plano de saúde"],
          "Análise e previsão":["análise de sinistralidade","previsão de sinistralidade","evolução da sinistralidade operadora","sinistralidade projetado x real"],
          "Software sinistralidade":["software gestão de sinistralidade","sistema controle de sinistralidade","dashboard sinistralidade"]},
  h=["Gestão de sinistralidade","Evolução da sinistralidade","Previsão de sinistralidade","Projetado x real","Fatores que pressionam custos","Não espere o fechamento do mês","Ofensores assistenciais","Sinistralidade mais clara"],
  d=["Ajuda a identificar os fatores que pressionam a sinistralidade, sem esperar o fechamento.","Evolução, previsão e projetado x real da sinistralidade em painéis. Peça uma demonstração.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["sinistralidade seguro auto","sinistro seguro","sinistralidade veículo","franquia"], path=("sinistralidade","demonstracao")),
 dict(slug="gestao-financeira", nome="GS - Gestão financeira de operadoras", orc=120, lp="gestao-financeira-operadoras",
  grupos={"Gestão financeira operadora":["gestão financeira de operadoras de saúde","gestão financeira operadora de planos de saúde","controle financeiro operadora de saúde"],
          "Temas financeiros":["inadimplência operadora de saúde","dre operadora de saúde","reajuste de mensalidades operadora"],
          "Software financeiro":["software financeiro operadora de saúde","sistema contábil operadora de planos de saúde","dashboard financeiro operadora"]},
  h=["Gestão financeira operadoras","Riscos e oportunidades","DRE e contabilidade","Inadimplência sob controle","Gestão de reajustes","Visão financeira da operadora","Finanças e sinistralidade","Painéis financeiros"],
  d=["Sua operadora sabe onde estão os riscos financeiros e as oportunidades?","Contabilidade, DRE, inadimplência e reajustes em painéis para a gestão.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["contador","contabilidade escritório","mei","nota fiscal","imposto de renda"], path=("financeiro","demonstracao")),
 dict(slug="inteligencia-regulatoria-ans", nome="GS - Inteligência regulatória ANS", orc=150, lp="inteligencia-regulatoria-ans",
  grupos={"Inteligência regulatória":["inteligência regulatória ans","monitoramento indicadores ans","gestão de obrigações ans","obrigações regulatórias operadora de saúde"],
          "IDSS e Sala de Situação":["idss gestão operadora","sistema para idss","acompanhamento idss operadora","sala de situação ans"],
          "RN 623 TISS SIB":["rn 623 atendimento operadora","monitoramento tiss operadora","sib operadora gestão"]},
  h=["Inteligência regulatória ANS","Gestão de IDSS","Sala de Situação ANS","Obrigações ANS em painéis","Mais visibilidade regulatória","Indicadores e obrigações","Monitoramento TISS e SIB","Atendimentos e RN 623"],
  d=["Mais visibilidade sobre indicadores, obrigações e riscos regulatórios da sua operadora.","IDSS, Sala de Situação, TISS, SIB e RN 623 em painéis. Peça uma demonstração.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["consulta idss","resultado idss unimed","rol de procedimentos lista","protocolo ans","reclamação ans","denúncia ans"], path=("regulatorio-ans","demonstracao")),
 dict(slug="bi-saude", nome="GS - Business Intelligence na saúde", orc=80, lp="bi-saude-suplementar",
  grupos={"BI na saúde":["business intelligence na saúde","bi na saúde","bi para saúde suplementar","bi healthcare brasil"],
          "Analytics saúde suplementar":["analytics saúde suplementar","inteligência de dados saúde suplementar","big data saúde operadoras"],
          "Gestão em saúde":["bi para gestão em saúde","dashboard gestão em saúde"]},
  h=["BI para saúde suplementar","Business Intelligence em saúde","Inteligência de dados em saúde","Analytics para operadoras","Dados de saúde suplementar","Painéis para gestores","Foco em operadoras de saúde","Da análise à decisão"],
  d=["Inteligência estratégica de dados para operadoras de planos de saúde. Demonstração.","Mais que dashboards: apoio a decisões financeiras, assistenciais e regulatórias.","Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação.","Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["hospitalar","hospital","ti saúde","tecnologia da informação curso","python","sql","power bi curso","tableau","qlik"], path=("bi-saude","demonstracao")),
]
SITELINKS=[("Solicite uma demonstração","Veja a plataforma em ação","Dados fictícios de demonstração","demonstracao"),
 ("Sinistralidade","Evolução e previsão","Fatores que pressionam custos","gestao-sinistralidade"),
 ("Gestão financeira","DRE, inadimplência, reajustes","Riscos e oportunidades","gestao-financeira-operadoras"),
 ("Obrigações ANS","IDSS, TISS, SIB, RN 623","Visibilidade regulatória","inteligencia-regulatoria-ans")]
CALLOUTS=["Feito para operadoras","Demonstração on-line","Finanças e assistencial","Painéis regulatórios ANS","Auditoria e acesso","Instalação on-premise"]
SNIPPETS=["Sinistralidade","Gestão financeira","Indicadores ANS","Gestão assistencial","Autorizações e glosas","Simuladores"]
# [A CONFIRMAR] 'Instalação on-premise' e 'Controle de acesso' constam da Ficha A (proprietário) - confirmar antes de ativar
def utm(c,g=None): return f"{DOM}/lp/{c['lp']}?utm_source=google&utm_medium=cpc&utm_campaign={c['slug']}&utm_term={{keyword}}&utm_content={{creative}}"
erros=[]
def chk(txt,lim,rot):
    if len(txt)>lim: erros.append(f"{rot}: {len(txt)}>{lim}: {txt}")
rows={k:[] for k in ["campanhas","grupos","palavras","negativas","rsa","sitelinks","callouts","snippets"]}
rep=["# Relatório de verificação de caracteres (gerado por scripts/gerar_google_ads.py)\n","| Campanha | Títulos (máx. chars) | Descrições (máx. chars) | Status |\n|---|---|---|---|"]
for c in CAMPS:
    hs=(c["h"]+COMUNS)[:15]; ds=c["d"]
    assert len(hs)==15 and len(set(hs))==15 and len(ds)==4,c["slug"]
    for t in hs: chk(t,30,c["slug"]+" H")
    for t in ds: chk(t,90,c["slug"]+" D")
    for t in c["path"]: chk(t,15,"path")
    rep.append(f"| {c['nome']} | {max(map(len,hs))} | {max(map(len,ds))} | {'OK' if all(len(x)<=30 for x in hs) and all(len(x)<=90 for x in ds) else 'FALHA'} |")
    rows["campanhas"].append({"Campaign":c["nome"],"Campaign Type":"Search","Status":"Paused","Budget":f"{c['orc']/30.4:.2f}","Budget type":"Daily","Networks":"Google search","Languages":"pt","Bid Strategy Type":"Maximize clicks","Maximum CPC limit":"","Location":"Brazil","EU political ads":"No"})
    for g,kws in c["grupos"].items():
        rows["grupos"].append({"Campaign":c["nome"],"Ad Group":g,"Ad Group Type":"Standard","Status":"Paused"})
        for k in kws:
            chk(k,80,"kw")
            for crit,txt in (("Phrase",k),("Exact",k)):
                rows["palavras"].append({"Campaign":c["nome"],"Ad Group":g,"Keyword":txt,"Criterion Type":crit,"Status":"Paused"})
        r={"Campaign":c["nome"],"Ad Group":g,"Ad type":"Responsive search ad","Final URL":utm(c),"Path 1":c["path"][0],"Path 2":c["path"][1],"Status":"Paused"}
        for i,t in enumerate(hs,1): r[f"Headline {i}"]=t
        for i,t in enumerate(ds,1): r[f"Description {i}"]=t
        rows["rsa"].append(r)
    for n in sorted(set(NEG_GERAIS+c["extra_neg"])):
        rows["negativas"].append({"Campaign":c["nome"],"Keyword":n,"Criterion Type":"Negative Phrase","Status":"Enabled"})
    for l,d1,d2,p in SITELINKS:
        chk(l,25,"sl");chk(d1,35,"sl d1");chk(d2,35,"sl d2")
        rows["sitelinks"].append({"Campaign":c["nome"],"Link Text":l,"Description Line 1":d1,"Description Line 2":d2,"Final URL":f"{DOM}/lp/{p}?utm_source=google&utm_medium=cpc&utm_campaign={c['slug']}&utm_content=sitelink","Status":"Paused"})
    for t in CALLOUTS: chk(t,25,"callout"); rows["callouts"].append({"Campaign":c["nome"],"Callout text":t,"Status":"Paused"})
    for t in SNIPPETS: chk(t,25,"snip")
    rows["snippets"].append({"Campaign":c["nome"],"Header":"Service catalog",**{f"Value {i}":t for i,t in enumerate(SNIPPETS,1)},"Status":"Paused"})
if erros: print("\n".join(erros)); sys.exit(1)
os.makedirs(BASE+"/csv_editor",exist_ok=True)
for k,v in rows.items():
    cols=[]; [cols.append(x) for r in v for x in r if x not in cols]
    with open(f"{BASE}/csv_editor/{k}.csv","w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); [w.writerow({x:r.get(x,"") for x in cols}) for r in v]
with open(BASE+"/csv_editor/lista_compartilhada_negativas.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["Lista compartilhada: Negativas_Gerais_NeoHealth","Tipo"]); [w.writerow([n,"Phrase"]) for n in NEG_GERAIS]
rep.append(f"\nTotal: {len(CAMPS)} campanhas, {len(rows['grupos'])} grupos, {len(rows['palavras'])} linhas de palavra-chave (frase+exata), {len(rows['negativas'])} linhas de negativas de campanha, {len(rows['rsa'])} RSAs. Orçamento mensal somado: R$ {sum(c['orc'] for c in CAMPS)}.")
open(BASE+"/csv_editor/VERIFICACAO_CARACTERES.md","w",encoding="utf-8").write("\n".join(rep)+"\n")
# md por campanha
for n,c in enumerate(CAMPS,1):
    hs=(c["h"]+COMUNS)[:15]
    L=[f"# Campanha {n}: {c['nome']}\n",f"- Orçamento do cenário: **R$ {c['orc']}/mês** (≈ R$ {c['orc']/30.4:.2f}/dia) · Rede: somente Pesquisa Google (sem parceiros de pesquisa/Display) · Local: Brasil · Idioma: pt · Status ao importar: **Pausada**",
       f"- Landing page de destino: `{DOM}/lp/{c['lp']}` [A CONFIRMAR domínio e criação da LP, ver 03_SITE_LANDING_PAGE]",
       f"- Final URL com UTM: `{utm(c)}`","- Lance inicial: **Maximizar cliques** com teto de CPC [HIPÓTESE: definir após Planejador de Palavras-chave] → após 15-30 conversões (principais/qualificadas offline) migrar para **Maximizar conversões**; tCPA só com ≥30 conversões/30 dias (improvável neste orçamento).",
       "- Evento de conversão principal: `generate_lead_demo` (envio do formulário de demonstração). Ver ../PLANO_MEDICAO_CONVERSOES.md\n","## Grupos de anúncios e palavras-chave (cada termo em frase e exata; sem ampla no início)\n"]
    for g,kws in c["grupos"].items():
        L.append(f"**{g}**"); [L.append(f'- "{k}" (frase) · [{k}] (exata)') for k in kws]; L.append("")
    L.append("## Negativas de campanha (frase)\n"+", ".join(sorted(set(c['extra_neg'])))+"\n\nMais a lista compartilhada `Negativas_Gerais_NeoHealth` (ver ../csv_editor/lista_compartilhada_negativas.csv): "+", ".join(NEG_GERAIS)+".\n")
    L.append("## RSA: 15 títulos (≤30 car.)\n"); [L.append(f"{i}. {t} ({len(t)})") for i,t in enumerate(hs,1)]
    L.append("\n## RSA: 4 descrições (≤90 car.)\n"); [L.append(f"{i}. {t} ({len(t)})") for i,t in enumerate(c['d'],1)]
    L.append(f"\nCaminho de exibição: /{c['path'][0]}/{c['path'][1]}\n\n## Extensões\n- Sitelinks: "+"; ".join(f"{a} → /lp/{p}" for a,_,_,p in SITELINKS)+"\n- Callouts: "+"; ".join(CALLOUTS)+" ([A CONFIRMAR] on-premise e controle de acesso)\n- Snippet estruturado (Catálogo de serviços): "+", ".join(SNIPPETS)+"\n")
    L.append("## Observações de intenção/SERP\nVer ../PESQUISA_INTENCAO_SERP.md. Termos observáveis: validar volumes e CPC no Planejador de Palavras-chave.\n")
    L.append("Funcionalidades citadas e status: painéis financeiros/sinistralidade/ANS [DISPONÍVEL, conforme Ficha A e inventário de telas]; integração Philips Tasy [A CONFIRMAR escopo comercial e uso da marca em anúncio]; previsões [DISPONÍVEL conforme Ficha A, sem promessa de resultado].")
    open(f"{BASE}/campanhas/{n:02d}_{c['slug']}.md","w",encoding="utf-8").write("\n".join(L)+"\n")
print("OK",open(BASE+"/csv_editor/VERIFICACAO_CARACTERES.md").read())
