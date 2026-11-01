# Personas — NeoHealth BI · OPS
Hipóteses de trabalho baseadas em funções típicas de operadoras; **não** derivadas de pesquisa com clientes (nenhuma existe na Ficha). Validar em entrevistas [A CONFIRMAR]. IDs de telas referem-se a `inventario_telas.csv`. Todos os módulos [DISPONÍVEL] conforme inventário, salvo nota.

Regras comuns: não prometer redução de sinistralidade/economia; não afirmar superioridade; telas sempre com nota de dados fictícios; CTA "Solicite uma demonstração."

---
## 1. CEO / Presidente
- **Dores:** visão consolidada tardia; dependência de relatórios de várias áreas; risco regulatório e financeiro simultâneos.
- **Interesses:** visão executiva única, tendências, cenários.
- **Objeções:** "já temos BI/ERP"; "mais um sistema"; prioridade/orçamento; confiança em dados.
- **Argumentos comerciais:** visão integrada dos pilares num cockpit; apoio à antecipação de cenários; conversa de 30 min com demo guiada.
- **Módulos:** Cockpit Executivo (coc-01), Painel de Gestão (mgd-01), Resultado Operacional e EBITDA (con-15), Previsão da Sinistralidade (sin-08), Simulador de Resultado (sin-09).
- **Canal ideal:** LinkedIn (conteúdo executivo + anúncio por cargo); contato direto/indicação.

## 2. Diretor Financeiro (CFO)
- **Dores:** acompanhar sinistralidade e resultado antes do fechamento; inadimplência; provisões e ativos garantidores; reajustes.
- **Interesses:** DRE, previsão, PEONA, caixa, inadimplência.
- **Objeções:** integração com contabilidade existente; consistência de números com o ERP; segurança.
- **Argumentos:** integração Oracle/Tasy [DISPONÍVEL conforme Ficha]; Memória de cálculo/rastreabilidade onde existir (ate-09 para RN 623; demais A CONFIRMAR); simuladores.
- **Módulos:** Balancete (con-01), DRE (con-02), Previsão do DRE (con-03), PEONA (con-05, con-12), Ativos Garantidores x Provisões (con-17), Inadimplência (fin-04, fin-06, fin-09), Gestão de Reajustes (men-01..08), Simulador DRE (con-04).
- **Canal:** LinkedIn; Google (termos de DRE/PEONA/inadimplência de operadoras).

## 3. Diretor Administrativo
- **Dores:** processos manuais, cobrança, contratos, chamados internos, controle de acessos.
- **Interesses:** eficiência de back-office, mensalidades, atendimento.
- **Objeções:** mudança de processo; esforço de implantação [A CONFIRMAR modelo].
- **Argumentos:** visão de mensalidades e inconsistências de cobrança; central de chamados; controle de acesso/SSO.
- **Módulos:** Mensalidades (men-09..16), Inconsistências de Cobrança (men-16), Central de Chamados (cha-01..05), Login Corporativo SSO (adm-01), Beneficiários (ben-*).
- **Canal:** LinkedIn; e-mail opt-in.

## 4. Diretor Assistencial / Médico
- **Dores:** entender utilização, alto custo, rede, qualidade; prazos regulatórios assistenciais.
- **Interesses:** estratificação de risco, gestão de caso, indicadores de qualidade.
- **Objeções:** "BI não entende clínica"; qualidade/codificação dos dados; sensibilidade de dados de saúde.
- **Argumentos:** análises organizadas por temas assistenciais; dados agregados; governança de acesso.
- **Módulos:** Estratificação de Risco (ass-11), Alto Custo e Gestão de Caso (ass-12), ICSAP (ass-22), Reinternação 30 dias (ass-24), Oncologia (ass-30), Diabético (ass-32), Home Care (ass-34), Prazos RN 566 (aut-14), Qualidade Hospitalar (pre-07).
- **Canal:** LinkedIn; YouTube (vídeos de tela); artigos.

## 5. Superintendente
- **Dores:** coordenar áreas, responder à ANS, equilibrar resultado e regulação.
- **Interesses:** visão transversal, risco regulatório, metas.
- **Objeções:** prioridade; tempo de implantação; "quem mantém?".
- **Argumentos:** Sala de Situação e IDSS na mesma plataforma que financeiro e assistencial.
- **Módulos:** Sala de Situação ANS (ans-13..19), Gestão de IDSS (ans-03..12), Cockpit (coc-01), Plano de Ação (ans-06).
- **Canal:** LinkedIn; indicação.

## 6. CIO / TI
- **Dores:** segurança, integração, carga em Oracle/Tasy, suporte a vários BIs.
- **Interesses:** arquitetura, on-premise, SSO, governança, LGPD.
- **Objeções:** mais um fornecedor; risco de segurança; custo de integração; lock-in.
- **Argumentos (fatos da Ficha):** integração Oracle e Tasy; espelhamento analítico DuckDB; multi-tenant; on-premise; controle de acesso e auditoria. Detalhes (certificações, SLA, pentest): [A CONFIRMAR] — não afirmar.
- **Módulos:** SSO (adm-01), Glossário das Telas (glo-01), governança (Ficha).
- **Canal:** Google (pesquisa técnica); LinkedIn por cargo; documentação técnica [A CONFIRMAR].

## 7. Gerente de Operações
- **Dores:** autorizações, filas, prazos, glosas, ocorrências, agendas.
- **Interesses:** produtividade, gargalos, SLAs.
- **Objeções:** adoção pela equipe; mudança de rotina.
- **Argumentos:** visões operacionais prontas; tutoriais por tela (223 vídeos de apoio).
- **Módulos:** Autorizações (aut-01..16), Fila de Análise (aut-09), Atendimentos (ate-*), Tratamento de Ocorrências (ate-19), Gestão de Agendas (ate-13..18), Glosas (ass-16..20).
- **Canal:** LinkedIn; YouTube.

## 8. Gestor de BI / Dados
- **Dores:** fila de pedidos de relatórios; modelagem de dados de saúde; regras ANS; reconciliação.
- **Interesses:** modelo de dados pronto, extensibilidade, performance.
- **Objeções:** "temos Power BI/Qlik/Tableau"; perda de controle; duplicidade.
- **Argumentos:** não precisa competir com a ferramenta atual: análises específicas do setor podem complementar [A CONFIRMAR possibilidade de exportação/API]; Glossário das Telas. Sem afirmar superioridade.
- **Módulos:** Explorador da Produção (ass-03), Glossário (glo-01), Achados (ach-01), Conferência ANS x Sistema (ans-23).
- **Canal:** Google; YouTube; artigos técnicos.

## 9. Atuário
- **Dores:** projeções, VCMH, precificação, reajustes, provisões.
- **Interesses:** séries históricas, projetado x real, simuladores, benchmarks.
- **Objeções:** transparência de metodologia; auditabilidade dos modelos; ML como "caixa-preta".
- **Argumentos:** Governança de Algoritmos (con-10) como tela existente [detalhes A CONFIRMAR]; memória de cálculo onde existir.
- **Módulos:** VCMH Próprio (ass-09), Projetado x Real (sin-10), Previsão da Sinistralidade (sin-08), Subsídio Cruzado (ass-08), Dispersão de Preço (ass-10), Benchmark de Reajuste (men-08), Sobrevivência e LTV (ben-09), PEONA (con-05).
- **Canal:** artigos e vídeos; LinkedIn orgânico; Google.

## 10. Controladoria
- **Dores:** consistência contábil, RN 518, conciliações, riscos corporativos.
- **Interesses:** anexos, matriz de risco, conciliação DIOPS.
- **Objeções:** aderência normativa (exigir fonte); validação com contabilidade.
- **Argumentos:** telas organizadas por tema normativo [citar norma só com fonte gov.br/ans — VERIFICAR NA FONTE].
- **Módulos:** RN 518 Anexos (con-06..08), Matriz de Risco (con-09), Conciliação com DIOPS (ans-28), Balancete (con-01), Ativos Garantidores (con-17).
- **Canal:** LinkedIn; Google.

## 11. Auditoria / Regulação (auditoria médica, regulação ANS)
- **Dores:** acompanhar NIP, prazos, SIB/TISS, uso fora de padrão, glosas.
- **Interesses:** trilhas de auditoria, rastreabilidade, pendências.
- **Objeções:** evidência/auditabilidade; falsos positivos; carga de trabalho.
- **Argumentos:** visão de pendências e rejeições; auditoria de reajustes; "Uso fora Padrão".
- **Módulos:** Auditoria Médica (aut-10), Uso fora Padrão (aut-11), Auditoria de Reajustes (men-07), NIP (ans-16, ate-10), SIB (ans-20..23), TISS (ans-24..33), Ouvidoria (ate-11).
- **Canal:** LinkedIn; Google; YouTube.
