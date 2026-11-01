# FICHA DE FATOS — fonte única de verdade (NeoHealth BI · OPS)
> Todo material do projeto só pode afirmar o que consta aqui. Qualquer item fora desta ficha = **[A CONFIRMAR COM O PROPRIETÁRIO]**.

## A. Fatos informados pelo proprietário (resumo técnico/funcional)
- Aplicação web multi-tenant; integração com Oracle e ERP Philips Tasy; espelhamento analítico local com DuckDB.
- ~170 telas de negócio ativas (conforme módulos/permissões), ~43 grupos de menus, 261 rotas de frontend. (Uso interno/técnico: **não vender quantidade de telas**.)
- Módulos: financeiro e contábil; sinistralidade; atuarial; beneficiários; assistencial; prestadores; autorizações e auditoria; glosas; intercâmbio PTU; indicadores ANS (IDSS, RN 518, RN 623, TISS, SIB); Sala de Situação ANS; simuladores financeiros e assistenciais; modelos de machine learning, previsões e detecção de anomalias; chat inteligente; alertas e resumos por WhatsApp e e-mail; governança, auditoria e controle de acesso; instalação on-premise; aplicativo mobile.

## B. Fatos verificados no repositório (tutoriais.json, gerado em 2026-10-23)
- 223 tutoriais em vídeo (≈15 h), um por tela, gravados em **base de demonstração "Operadora Modelo" com dados fictícios**. Capas (JPG 1920×1080) e vídeos hospedados na release `manual`.
- Grupos de menu visíveis no inventário: Painel de Gestão, Cockpit Executivo, Evolução da Sinistralidade (10), Gestão Assistencial (34+), Gestão de Glosas, Gestão Financeira (9), Contabilidade (17), Gestão de Mensalidades/Reajustes (18), Contratos e Beneficiários (21), Atendimentos/RN 623 (19), Autorizações (16), Intercâmbio PTU (11), Prestadores x Profissionais (13), Obrigações ANS (33: IDSS, Sala de Situação, SIB, TISS), Painéis ANS (6), Informações de Saúde (5), Central de Chamados, Login Corporativo (SSO), Simuladores, Achados, Glossário.
- Identidade observada nas capas: logotipo "NeoHealth – BI OPS" (BI em azul-claro, OPS em cinza); tema escuro (fundo ≈ #060A15), azul "BI" ≈ #5FBEEC, azul do ícone ≈ #4190D3, destaque menta/ciano ≈ #A9EFE5.
- Inventário completo: `inventario_telas.csv`. Capas reais selecionadas: `08_CRIATIVOS/assets_reais/`.

## C. Regras de linguagem (obrigatórias)
1. Proibido inventar: clientes, depoimentos, certificações, integrações, números de resultado, prêmios, parcerias.
2. Proibido prometer/garantir redução de sinistralidade, economia ou melhora de indicador. Usar: "ajuda a identificar", "apoia", "dá visibilidade a", "oportunidades que a inteligência pode ajudar a administrar".
3. Dados em telas = **base de demonstração fictícia**. Todo criativo com tela deve trazer a nota: "Imagem da plataforma com dados fictícios (base de demonstração)".
4. Status de funcionalidade: **[DISPONÍVEL]** (confirmado no resumo/tutorial) · **[CONFIGURÁVEL]** · **[EM DESENVOLVIMENTO]** · **[PLANEJADO]** · **[A CONFIRMAR]**. Na dúvida, [A CONFIRMAR]. Cada peça lista as funcionalidades citadas e o status.
5. Sem superioridade vs. concorrentes sem evidência pública verificável.
6. Normas ANS: citar número da norma e linkar fonte oficial (gov.br/ans); não parafrasear prazos/percentuais de memória — marcar [VERIFICAR NA FONTE].
7. LGPD: consentimento/base legal explícita, opt-out em toda comunicação, sem dados de saúde pessoais em materiais.
8. Nada vai a produção, nenhum disparo, nenhuma contratação ou gasto sem aprovação (ver 15_RELATORIOS/pendencias_e_aprovacoes.md).

## D. Mensagens-âncora
- Marca: "Transforme dados em decisões. Decisões em resultados."
- CTA principal: "Solicite uma demonstração." · CTA secundário: "Conheça o potencial dos dados da sua operadora."
- Pilares: Financeira · Sinistralidade · Assistencial · Regulatória · Preditiva (mensagens no plano, seção 6).

## E. Decisões do proprietário (registro — 01/11/2026)
1. **Verba:** R$ 1.000,00/mês de mídia (abaixo do cenário inicial de R$ 3.000). Ver `01_ESTRATEGIA/05b_orcamento_1000.md`.
2. **Status de funcionalidades:** o proprietário autorizou tratar como **[DISPONÍVEL]** todas as funcionalidades listadas na seção A (resumo técnico/funcional): multi-tenant, integração Oracle/Tasy, DuckDB, módulos financeiro/contábil/sinistralidade/atuarial/beneficiários/assistencial/prestadores/autorizações/glosas/PTU, indicadores ANS (IDSS, RN 518, RN 623, TISS, SIB), Sala de Situação, simuladores, modelos de ML/previsões/anomalias, chat inteligente, alertas por WhatsApp e e-mail, governança/auditoria/controle de acesso, on-premise e app mobile. **Continuam [A CONFIRMAR]** detalhes não listados (algoritmos, métricas, SLAs, integração com outros ERPs, certificações). Alertas de [A CONFIRMAR] nas peças já escritas devem ser relidos à luz desta decisão.
3. **Domínio e logotipo:** indicado https://neohealth.com.br/ como fonte do logotipo original e domínio. **Não foi possível acessar o site** (bloqueado pela política de rede do ambiente, host neohealth.com.br). Logotipo continua provisório até o arquivo ser fornecido ou o domínio liberado.
