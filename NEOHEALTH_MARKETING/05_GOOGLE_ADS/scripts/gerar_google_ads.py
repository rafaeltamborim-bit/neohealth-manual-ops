# -*- coding: utf-8 -*-
"""Gera CSVs (Google Ads Editor) e campanhas/*.md; verifica limites de caracteres. Rodar: python3 gerar_google_ads.py"""
import csv, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOM = "https://neohealth.com.br"   # domínio informado pelo proprietário; páginas /lp/* ainda a publicar (03_SITE_LANDING_PAGE)
COMUNS = ["Solicite uma demonstração","Transforme dados em decisões","Decisões em resultados","NeoHealth BI · OPS",
          "Veja a plataforma em ação","Conheça o potencial dos dados","Inteligência para operadoras"]
NEG_GERAIS = ["vaga","vagas","emprego","estágio","salário","curso","cursos","treinamento","certificação","faculdade","tcc","monografia",
 "grátis","gratuito","download","pdf","apostila","tutorial","youtube","hospital","clínica","consultório","prontuário","laboratório","farmácia",
 "plano de saúde individual","cotação","comparar planos","carteirinha","segunda via","boleto","telefone","reclamação","convênio médico","enfermagem","residência"]
COMUNS_H = ["Solicite uma demonstração","Transforme dados em decisões","Decisões em resultados","NeoHealth BI · OPS",
          "Veja a plataforma em ação","Conheça o potencial dos dados","Inteligência para hospitais"]
NEG_H = [n for n in NEG_GERAIS if n not in ("hospital","clínica")] + ["plano de saúde","operadora de saúde"]
D_COM = "Transforme dados em decisões. Decisões em resultados. Veja a plataforma em ação."
CAMPS = [
 dict(slug="op-decisao", nome="GS - Operadoras: inteligência de dados e decisão", orc=200, lp="operadoras",
  grupos={"Inteligência operadoras":["inteligência de dados para operadoras de saúde","plataforma de inteligência para operadoras","inteligência estratégica operadora de saúde","bi para operadoras de planos de saúde"],
          "Gestão operadora":["software para operadora de planos de saúde","sistema de gestão para operadoras de saúde","gestão estratégica operadora de saúde","indicadores para operadoras de saúde"],
          "Decisão e previsão":["previsão de sinistralidade","gestão de sinistralidade operadora","análise preditiva operadora de saúde"]},
  h=["Inteligência estratégica","Decida com dados","Antecipe cenários","Visão integrada da operadora","Financeiro e sinistralidade","Assistencial e regulatório","Apoio a decisões na gestão","Previsões e simuladores"],
  d=["Plataforma de inteligência estratégica para operadoras. Solicite uma demonstração.","Visão financeira, sinistralidade, assistencial e regulatória para decidir e antecipar.",D_COM,"Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["power bi download","excel"], path=("operadoras","demonstracao")),
 dict(slug="op-erp", nome="GS - Operadoras: qualquer ERP", orc=200, lp="operadoras-erp",
  grupos={"Integração ERP":["bi integrado ao erp operadora de saúde","integração erp operadora de saúde bi","inteligência de dados erp operadora","dados do erp da operadora em um só lugar"],
          "ERPs específicos":["bi tasy operadora de planos de saúde","dados do tasy operadora de saúde","análise de dados tasy operadora"],
          "Qualquer ERP":["bi para qualquer erp operadora","plataforma independente de erp operadora"]},
  h=["Funciona com seu ERP","Dados do ERP em decisões","Inteligência de dados","Do ERP à decisão","Visão integrada de dados","Financeiro e sinistralidade","Assistencial e regulatório","Antecipe cenários"],
  d=["Integra-se ao ERP da sua operadora. Transforme dados em decisões. Peça uma demonstração.","Dados do ERP em visão integrada: financeiro, sinistralidade, assistencial e ANS.",D_COM,"Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["suporte tasy","login tasy","tasy ehr hospital","vaga tasy","curso tasy","treinamento tasy","tasy prontuário"], path=("operadoras","erp")),
 dict(slug="op-sinistralidade", nome="GS - Operadoras: sinistralidade (fase 2)", orc=0, lp="gestao-sinistralidade",
  grupos={"Gestão de sinistralidade":["gestão de sinistralidade","controle de sinistralidade operadora","como controlar sinistralidade operadora","gestão da sinistralidade plano de saúde"],
          "Análise e previsão":["análise de sinistralidade","previsão de sinistralidade","evolução da sinistralidade operadora","sinistralidade projetado x real"]},
  h=["Gestão de sinistralidade","Evolução da sinistralidade","Previsão de sinistralidade","Projetado x real","Fatores que pressionam custos","Não espere o fechamento do mês","Ofensores assistenciais","Sinistralidade mais clara"],
  d=["Ajuda a identificar os fatores que pressionam a sinistralidade, sem esperar o fechamento.","Evolução, previsão e projetado x real da sinistralidade. Peça uma demonstração.",D_COM,"Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["sinistralidade seguro auto","sinistro seguro","sinistralidade veículo","franquia"], path=("sinistralidade","demonstracao")),
 dict(slug="op-ans", nome="GS - Operadoras: inteligência regulatória ANS (fase 2)", orc=0, lp="inteligencia-regulatoria-ans",
  grupos={"Inteligência regulatória":["inteligência regulatória ans","monitoramento indicadores ans","gestão de obrigações ans","obrigações regulatórias operadora de saúde"],
          "IDSS e Sala de Situação":["idss gestão operadora","sistema para idss","acompanhamento idss operadora","sala de situação ans"]},
  h=["Inteligência regulatória ANS","Gestão de IDSS","Sala de Situação ANS","Obrigações ANS em visão única","Mais visibilidade regulatória","Indicadores e obrigações","Monitoramento TISS e SIB","Atendimentos e RN 623"],
  d=["Mais visibilidade sobre indicadores, obrigações e riscos regulatórios da sua operadora.","IDSS, Sala de Situação, TISS, SIB e RN 623 em uma visão integrada. Peça demonstração.",D_COM,"Conheça o potencial dos dados da sua operadora. Demonstração com base fictícia."],
  extra_neg=["consulta idss","resultado idss unimed","rol de procedimentos lista","protocolo ans","reclamação ans","denúncia ans"], path=("regulatorio-ans","demonstracao")),
 dict(slug="hosp-decisao", nome="GS - Hospitais: inteligência de dados e decisão", orc=200, lp="hospitais", comuns=COMUNS_H, neg=NEG_H,
  grupos={"Inteligência hospitais":["inteligência de dados para hospitais","plataforma de inteligência hospitalar","inteligência estratégica gestão hospitalar","bi para hospitais"],
          "Gestão hospitalar":["indicadores de gestão hospitalar","software de gestão hospitalar indicadores","analytics hospitalar","gestão hospitalar baseada em dados"]},
  h=["Inteligência estratégica","Decida com dados","Visão integrada da gestão","Antecipe cenários","Dados que viram decisão","Gestão hospitalar com dados","Apoio a decisões na gestão","Mais visibilidade na gestão"],
  d=["Plataforma de inteligência de dados e decisão para hospitais. Solicite uma demonstração.","Transforme os dados do seu hospital em visão integrada para decidir e antecipar.",D_COM,"Conheça o potencial dos dados do seu hospital. Demonstração com base fictícia."],
  extra_neg=["prontuário eletrônico","vaga hospital","concurso hospital"], path=("hospitais","demonstracao")),
 dict(slug="hosp-erp", nome="GS - Hospitais: qualquer ERP", orc=200, lp="hospitais-erp", comuns=COMUNS_H, neg=NEG_H,
  grupos={"Integração ERP hospital":["bi integrado ao erp hospitalar","inteligência de dados erp hospitalar","dados do erp do hospital em um só lugar","integração erp hospital bi"],
          "ERPs específicos":["bi tasy hospital","dados do tasy hospital","análise de dados tasy hospital"]},
  h=["Funciona com seu ERP","Dados do ERP em decisões","Inteligência de dados","Do ERP à decisão","Visão integrada de dados","Gestão hospitalar com dados","Antecipe cenários","Dados que viram decisão"],
  d=["Integra-se ao ERP do seu hospital. Transforme dados em decisões. Peça uma demonstração.","Dados do ERP hospitalar em uma visão integrada para a gestão decidir e antecipar.",D_COM,"Conheça o potencial dos dados do seu hospital. Demonstração com base fictícia."],
  extra_neg=["suporte tasy","login tasy","vaga tasy","curso tasy","treinamento tasy","tasy prontuário"], path=("hospitais","erp")),
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
    hs=(c["h"]+c.get("comuns",COMUNS))[:15]; ds=c["d"]
    assert len(hs)==15 and len(set(hs))==15 and len(ds)==4,c["slug"]
    for t in hs: chk(t,30,c["slug"]+" H")
    for t in ds: chk(t,90,c["slug"]+" D")
    for t in c["path"]: chk(t,15,"path")
    rep.append(f"| {c['nome']} | {max(map(len,hs))} | {max(map(len,ds))} | {'OK' if all(len(x)<=30 for x in hs) and all(len(x)<=90 for x in ds) else 'FALHA'} |")
    rows["campanhas"].append({"Campaign":c["nome"],"Campaign Type":"Search","Status":"Paused","Budget":(f"{c['orc']/30.4:.2f}" if c["orc"] else "A DEFINIR (fase 2)"),"Budget type":"Daily","Networks":"Google search","Languages":"pt","Bid Strategy Type":"Maximize clicks","Maximum CPC limit":"","Location":"Brazil","EU political ads":"No"})
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
    for n in sorted(set(c.get("neg",NEG_GERAIS)+c["extra_neg"])):
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
    hs=(c["h"]+c.get("comuns",COMUNS))[:15]
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
    L.append("Funcionalidades citadas e status: painéis financeiros/sinistralidade/ANS [DISPONÍVEL, conforme Ficha A e inventário de telas]; integração com ERPs (qualquer ERP, conforme proprietário; lista e forma [A CONFIRMAR]); Tasy citado só como palavra-chave, sem parceria; hospitais: funcionalidades específicas [A CONFIRMAR]; previsões [DISPONÍVEL conforme Ficha A, sem promessa de resultado].")
    open(f"{BASE}/campanhas/{n:02d}_{c['slug']}.md","w",encoding="utf-8").write("\n".join(L)+"\n")
print("OK",open(BASE+"/csv_editor/VERIFICACAO_CARACTERES.md").read())
