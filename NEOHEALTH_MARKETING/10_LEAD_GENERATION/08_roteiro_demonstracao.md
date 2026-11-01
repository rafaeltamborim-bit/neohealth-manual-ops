# Roteiro de demonstração executiva (30–40 min), por persona
**Regras:** usar somente a base "Operadora Modelo" (dados fictícios); dizer isso na abertura e em qualquer print ("Imagem da plataforma com dados fictícios (base de demonstração)"). Não prometer resultados. Funcionalidade fora do inventário → "[A CONFIRMAR] e retorno por escrito". Telas referenciadas pelo `id` do inventário (`01_ESTRATEGIA/inventario_telas.csv`); capas reais em `08_CRIATIVOS/assets_reais/`.

## Estrutura padrão
| Min | Bloco | Conteúdo |
|---|---|---|
| 0–3 | Abertura | Pauta, tempo, aviso de base fictícia, confirmar objetivo e desafios (da qualificação) |
| 3–8 | Visão executiva | coc-01 Cockpit Executivo, mgd-01 Painel de Gestão: "do geral ao detalhe" |
| 8–28 | Módulo da persona | ver abaixo (3 a 4 telas, 5 min cada), sempre partindo de uma pergunta de gestão |
| 28–33 | Preditivo / cenários | uma tela de previsão ou simulador adequada à persona |
| 33–37 | Governança e implantação | adm-01 (SSO), controle de acesso e auditoria, ERP Tasy/Oracle, on-premise [com status] |
| 37–40 | Fechamento | resumo das dores, próximo passo, quem mais convidar, data do retorno |

## Persona 1 — Diretoria / Superintendência (30 min)
Pergunta-guia: "Onde estão os riscos e as oportunidades da operadora?"
1. coc-01 Cockpit Executivo e mgd-01 Painel de Gestão (visão única).
2. con-15 Resultado Operacional e EBITDA.
3. sin-01 Visão Geral da Sinistralidade → sin-10 Projetado x Real.
4. ans-13 Sala de Situação ANS (visão geral regulatória).
5. Preditivo: sin-08 Previsão da Sinistralidade.
Fechamento: "Quais 2 decisões você gostaria de ver melhoradas?"

## Persona 2 — Financeiro / Controladoria (35–40 min)
Pergunta-guia: "Onde estão os riscos financeiros e as oportunidades de melhoria?"
1. con-02 DRE e con-01 Balancete; con-03 Previsão do DRE; con-04 Simulador DRE.
2. con-05 PEONA, con-17 Ativos Garantidores x Provisões, con-13 PPSC x Inadimplência.
3. fin-04 Vencimentos e Inadimplência; fin-09 Inadimplência por Safra e Canal; fin-06 Devedor Contumaz.
4. men-01 Reajustes (visão geral), men-07 Auditoria de Reajustes, men-15 Simulador de Reajuste.
Observação: normas contábeis/regulatórias de provisão citadas só com fonte oficial [VERIFICAR NA FONTE].

## Persona 3 — Atuária / Gestão de risco (35–40 min)
Pergunta-guia: "O que pressiona a sinistralidade e o que pode acontecer?"
1. sin-02 Tipo de Contratação, sin-03 Faixa Etária, sin-04 Grupos de Contratos, sin-06 Produtos.
2. ass-08 Subsídio Cruzado por Faixa Etária, ass-09 VCMH Próprio, ass-10 Dispersão de Preço.
3. sin-08 Previsão, sin-09 Simulador de Resultado, sin-10 Projetado x Real.
4. con-10 Governança de Algoritmos, con-16 Sinais de Tendência (IRIS).
5. ben-09 Sobrevivência e LTV das Coortes; ben-07 Envelhecimento da Carteira.

## Persona 4 — Assistencial / Médica (35 min)
Pergunta-guia: "Como a utilização impacta os resultados?"
1. ass-11 Estratificação de Risco; ass-12 Alto Custo e Gestão de Caso.
2. ass-05 Ofensores Assistenciais; ass-23 Utilização Hospitalar; ass-24 Reinternação em 30 dias; ass-22 ICSAP; ass-25 Saúde Mental e Terapias.
3. pre-01 Rede (visão geral), pre-07 Qualidade Hospitalar, pre-09 Verticalização.
4. aut-01 Autorizações (visão geral), aut-09 Fila de Análise, aut-10 Auditoria Médica.
5. ass-13 Simulador Assistencial.

## Persona 5 — Regulatório / Compliance (35 min)
Pergunta-guia: "Temos visibilidade contínua de indicadores, obrigações e riscos?"
1. ans-03 Gestão de IDSS, ans-04 IDSS, ans-05 Comparativo Calculado x ANS, ans-06 Plano de Ação.
2. ans-13 Sala de Situação, ans-16 Reclamações (NIP), ans-15 Ressarcimento ao SUS.
3. ans-20 SIB visão geral, ans-22 Rejeições, ans-27 Pendências de reenvio TISS, ans-28 Conciliação DIOPS.
4. ate-04 Atendimentos (RN 623) visão geral, ate-11 Ouvidoria.
Observação: não afirmar prazos/percentuais [VERIFICAR NA FONTE].

## Persona 6 — TI / BI (30–35 min)
Pergunta-guia: "Como é construído, integrado, protegido e operado?"
1. Visão geral da arquitetura: web multi-tenant, espelhamento analítico DuckDB, integração Oracle e Tasy.
2. adm-01 Login Corporativo (SSO); controle de acesso e auditoria; on-premise.
3. cha-01 Central de Chamados; glo-01 Glossário; tutoriais em vídeo por tela.
4. Perguntas técnicas: volume, latência de atualização, backup, ambiente [responder só o que consta; resto "[A CONFIRMAR]"].

## Pós-demonstração (até 1 dia útil)
E-mail com resumo (dores, telas vistas, perguntas em aberto com responsável e prazo), link dos tutoriais pertinentes, proposta de próximo passo. Atualizar CRM: etapa, stakeholders, objeções, próxima ação.
