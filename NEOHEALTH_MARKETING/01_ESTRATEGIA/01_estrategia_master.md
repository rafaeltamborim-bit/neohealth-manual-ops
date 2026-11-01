# Estratégia Master — NeoHealth BI · OPS (90 dias)
Data-base: 01/11/2026 · Idioma: pt-BR · Fonte de fatos: `00_FICHA_DE_FATOS.md` · Status: PROPOSTA, nada publicado/gasto sem aprovação.

> Convenção de status de funcionalidade: [DISPONÍVEL] · [CONFIGURÁVEL] · [EM DESENVOLVIMENTO] · [PLANEJADO] · [A CONFIRMAR]. Tudo que não está na Ficha de Fatos = [A CONFIRMAR COM O PROPRIETÁRIO].

## 1. Diagnóstico

**O que se sabe (Ficha de Fatos):** aplicação web multi-tenant; integração com Oracle e ERP Philips Tasy; espelhamento analítico com DuckDB; módulos financeiro/contábil, sinistralidade, atuarial, beneficiários, assistencial, prestadores, autorizações/auditoria, glosas, intercâmbio PTU, indicadores ANS (IDSS, RN 518, RN 623, TISS, SIB), Sala de Situação ANS, simuladores, ML/previsões/anomalias, chat inteligente, alertas WhatsApp/e-mail, governança/controle de acesso, on-premise, app mobile. 223 tutoriais em vídeo (≈15 h) na base de demonstração "Operadora Modelo" (dados fictícios).

**Forças (ancoradas em fatos):** profundidade vertical em saúde suplementar (inventário cobre financeiro, contábil, assistencial, ANS, PTU, glosas); material de demonstração abundante (223 vídeos); integração Tasy declarada; opção on-premise declarada.

**Fraquezas / lacunas de marketing:** nenhum cliente referenciável, depoimento, case, certificação ou número de resultado disponível na Ficha (e não podem ser inventados); sem marca conhecida no setor [A CONFIRMAR]; sem histórico de audiência/leads [A CONFIRMAR]; vídeos/telas só com dados fictícios; status de várias funcionalidades (ML, chat, WhatsApp, app mobile) a classificar item a item [A CONFIRMAR].

**Oportunidades:** alta carga regulatória do setor (IDSS, RN 518, RN 623, TISS, SIB, Sala de Situação) cria demanda por visibilidade integrada; operadoras que já usam Tasy [A CONFIRMAR quais]; mercado composto por BI genéricos (exigem construção do modelo de dados) e módulos gerenciais de ERPs (ver `04_matriz_concorrencia.md`).

**Ameaças:** concorrência de BI genéricos conhecidos e de fornecedores de ERP já instalados nas operadoras; ciclo de venda B2B longo e com múltiplos decisores; restrições de plataformas de anúncios para conteúdo de saúde (ver `06_riscos_compliance_lgpd.md`); desconfiança com dados de saúde (LGPD); orçamento de mídia enxuto (R$ 3–10 mil/mês).

## 2. Objetivos (90 dias) — metas de processo, não promessas de resultado
Metas numéricas de leads/contratos **não** são prometidas; abaixo, objetivos operacionais e de aprendizado. Metas quantitativas devem ser fixadas pelo proprietário após o 1º mês de dados [A CONFIRMAR].

| # | Objetivo | Indicador | Critério de sucesso |
|---|----------|-----------|--------------------|
| O1 | Colocar no ar infraestrutura mínima de captação (landing, formulário com consentimento, CRM, UTMs) | Itens publicados e testados | 100% do checklist aprovado antes de qualquer gasto |
| O2 | Validar mensagem e público por pilar | CTR, taxa de conversão LP, taxa de qualificação | Ao menos 2 pilares com dados comparáveis ao fim do dia 60 |
| O3 | Gerar conversas qualificadas com decisores de operadoras | Solicitações de demonstração; demos realizadas | Meta fixada pelo proprietário após baseline [A CONFIRMAR] |
| O4 | Construir base de conteúdo reutilizável (artigos, vídeos, one-pagers) | Peças aprovadas e publicadas | Conforme cronograma (14_CRONOGRAMA) |
| O5 | Aprender o CAC de conversa/demo por canal | Custo por solicitação de demo, por canal | Dados suficientes para decidir realocação (ver 05_orcamento) |

## 3. Posicionamento
Plataforma especializada em **inteligência estratégica para operadoras de planos de saúde** — não "mais um BI de dashboards". Âncora de marca: **"Transforme dados em decisões. Decisões em resultados."**

Declaração de posicionamento (interna): *Para gestores de operadoras de planos de saúde que precisam enxergar riscos financeiros, assistenciais e regulatórios de forma integrada, a NeoHealth BI · OPS é a plataforma de inteligência estratégica construída para a saúde suplementar, que conecta dados da operação (Oracle/Tasy) a análises prontas por tema e a recursos preditivos [status por item a confirmar].*

Regras: não vender quantidade de telas; não alegar "melhor/líder/único"; "resultados" é horizonte da decisão, nunca promessa.

## 4. Proposta de valor
1. **Visibilidade integrada** — financeiro, sinistralidade, assistencial e regulatório em uma só plataforma [DISPONÍVEL – módulos do inventário].
2. **Conhecimento do setor embutido** — análises organizadas pelos temas que o gestor de operadora já usa (IDSS, RN 518, RN 623, TISS, SIB, PTU, glosas) [DISPONÍVEL – telas do inventário; aderência normativa de cada tela a validar com o proprietário].
3. **Da análise histórica à antecipação** — previsões, simuladores e detecção de anomalias [DISPONÍVEL/CONFIGURÁVEL – classificar por tela; ML e anomalias: A CONFIRMAR].
4. **Conexão com a base existente** — integração com Oracle e ERP Philips Tasy; instalação on-premise [DISPONÍVEL conforme Ficha].
5. **Governança** — controle de acesso, auditoria, SSO corporativo (tela adm-01) [DISPONÍVEL; detalhes A CONFIRMAR].

## 5. Mensagem central e tom
- Mensagem-mãe: "Transforme dados em decisões. Decisões em resultados."
- Tom: técnico-executivo, sóbrio, em pt-BR; verbos de apoio ("ajuda a identificar", "apoia", "dá visibilidade a"); jamais "garante", "reduz X%", "o melhor".
- CTAs: primário "Solicite uma demonstração."; secundário "Conheça o potencial dos dados da sua operadora."
- Toda imagem de tela: "Imagem da plataforma com dados fictícios (base de demonstração)".

## 6. Arquitetura de mensagens por pilar
| Pilar | Mensagem-âncora (Brief) | Promessa permitida | Provas permitidas (telas reais do inventário) | Personas-alvo | Status |
|---|---|---|---|---|---|
| 1 Financeira | "Sua operadora sabe exatamente onde estão os riscos financeiros e as oportunidades de melhoria?" | Dá visibilidade a riscos e oportunidades financeiras | Cockpit Executivo (coc-01); Balancete/DRE/Previsão do DRE (con-01..03); Resultado Operacional e EBITDA (con-15); PEONA (con-05); Ativos Garantidores x Provisões (con-17); Títulos a pagar/receber e Inadimplência (fin-01..09); Mensalidades/Reajustes (men-*) | CEO, Dir. Financeiro, Controladoria | Telas [DISPONÍVEL]; cálculos regulatórios [A CONFIRMAR] |
| 2 Sinistralidade | "Não espere o fechamento do mês para identificar os fatores que pressionam a sinistralidade." | Ajuda a identificar fatores de pressão antes do fechamento | Evolução da Sinistralidade (sin-01..10); Ofensores Assistenciais (ass-05); Frequência de Utilização (ass-02); VCMH Próprio (ass-09); Alto Custo e Gestão de Caso (ass-12); Glosas (ass-16..20, ass-35) | Dir. Financeiro, Dir. Assistencial, Atuário | [DISPONÍVEL]; "antes do fechamento" depende da periodicidade de carga [A CONFIRMAR] |
| 3 Assistencial | "Entenda como a utilização dos serviços de saúde impacta os resultados da sua operadora." | Conecta utilização a resultado | Risco de Subscrição (ass-01..10); Estratificação de Risco (ass-11); ICSAP (ass-22); Reinternação 30 dias (ass-24); Oncologia (ass-30); Diabético (ass-32); Home Care (ass-34); Prestadores (pre-*) | Dir. Assistencial, Gerente de Operações | [DISPONÍVEL] |
| 4 Regulatória | "Mais visibilidade sobre indicadores, obrigações e riscos regulatórios." | Mais visibilidade sobre indicadores e obrigações | Gestão de IDSS (ans-03..12); Sala de Situação ANS (ans-13..19); SIB (ans-20..23); Monitoramento TISS (ans-24..33); RN 623 (ate-04..12); RN 518 (con-06..11); Prazos RN 566/623 (aut-12, aut-14) | Dir. Assistencial, Superintendente, Auditoria/Regulação | Telas [DISPONÍVEL]; citação de norma só com fonte gov.br/ans [VERIFICAR NA FONTE] |
| 5 Preditiva | "Vá além da análise histórica. Utilize seus dados para antecipar cenários e apoiar decisões." | Apoia a antecipação de cenários | Previsão da Sinistralidade (sin-08); Projetado x Real (sin-10); Simuladores (sin-09, con-04, ass-13, men-15); Previsão da Produção (ass-06); Previsão do DRE (con-03); Sinais de Tendência/IRIS (con-16) | CEO, Atuário, Gestor de BI | Previsões/simuladores [DISPONÍVEL] conforme telas; ML/anomalias [A CONFIRMAR] |

Mensagens de apoio transversais: Governança e acesso (adm-01 SSO); Intercâmbio PTU (int-01..11); Prestadores e rede (pre-*); Beneficiários e carteira (ben-*).

## 7. Funil (B2B, ciclo longo)
| Etapa | Objetivo | Conteúdo/ativo | Canal principal | Métrica |
|---|---|---|---|---|
| Descoberta | Ser visto por decisores | Posts por pilar; vídeos curtos de tela real (com nota); artigos SEO | LinkedIn, Google (pesquisa), YouTube | Impressões, CTR, alcance qualificado |
| Interesse | Educar sobre o problema | Artigos, one-pager por pilar, vídeo-tutorial real | Site/blog, YouTube, LinkedIn | Sessões, tempo, inscritos |
| Consideração | Mostrar profundidade | Página por pilar, glossário de telas, comparativo "como avaliar" (sem superioridade) | Site, e-mail (com opt-in) | Conversão para lead de conteúdo |
| Decisão | Gerar conversa | LP de demonstração, formulário curto | Google (marca/categoria), LinkedIn Lead Gen, remarketing permitido | Solicitações de demo |
| Qualificação | Filtrar encaixe | Roteiro BANT/MEDDIC adaptado; CRM | CRM (12_CRM) | MQL→SQL, demos realizadas |
| Retenção/relacionamento | Manter conversa | Newsletter opt-in | E-mail | Descadastros, respostas |

## 8. Canais e papéis
- **LinkedIn (Ads + orgânico):** principal para decisores (cargo/segmento da empresa). Lead Gen Forms só com consentimento e sem dados de saúde.
- **Google Ads (pesquisa):** captura demanda explícita ("BI para operadora de saúde", "indicadores IDSS"); sem remarketing por categoria sensível (ver 06).
- **Meta Ads:** papel reduzido, topo de funil/remarketing de visitantes do site sujeito a políticas; menor verba.
- **YouTube:** reuso dos tutoriais reais; autoridade e demonstração.
- **SEO/Artigos:** base de longo prazo (09_SEO_ARTIGOS).
- **E-mail/WhatsApp:** somente base com consentimento e opt-out (11_AUTOMACOES).
- **Eventos/relacionamento direto:** fora do escopo pago; sugerir [A CONFIRMAR].

## 9. KPIs
| Camada | KPI | Observação |
|---|---|---|
| Mídia | Impressões, CTR, CPC, CPM, frequência | Benchmarks só após dados próprios |
| Site | Sessões, conversão LP, scroll, origem UTM | |
| Lead | Leads, custo por lead, % qualificados | Não há meta prometida |
| Vendas | Demos solicitadas/realizadas, SQL, ciclo | Dependente do comercial [A CONFIRMAR] |
| Conteúdo | Views de vídeo, retenção, downloads | |
| Saúde da base | Opt-out, descadastro, reclamações de spam | LGPD |
| Eficiência | Custo por demo realizada, por canal | Base para realocação |

## 10. Premissas e limites
Sem garantias de leads ou contratos; custos são estimativas a validar; qualquer norma ANS é [VERIFICAR NA FONTE]; nenhuma afirmação sobre concorrentes sem URL (ver 04).

## Pendências
Ver `PENDENCIAS.md`.
