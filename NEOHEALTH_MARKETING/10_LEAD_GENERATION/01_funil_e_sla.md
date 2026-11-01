# Funil de geração de demanda — 7 etapas, critérios e SLAs
> SLAs são **propostas** a validar com o time comercial [A CONFIRMAR]. Etapas espelham o pipeline do CRM (`12_CRM`).

## Visão geral
ATRAÇÃO → INTERESSE → CONVERSÃO → QUALIFICAÇÃO → DEMONSTRAÇÃO → PROPOSTA → CONTRATAÇÃO

| # | Etapa | Definição | Estado do contato no CRM | Critério de passagem para a próxima | SLA proposto | Responsável |
|---|---|---|---|---|---|---|
| 1 | ATRAÇÃO | Público-alvo (operadoras) é exposto à marca via LinkedIn, Google, Meta, YouTube, SEO, indicação. Ainda anônimo. | Sem registro (apenas analytics) | Visita com intenção: leu conteúdo, assistiu vídeo ≥50% ou clicou em anúncio com UTM válida | — | Marketing |
| 2 | INTERESSE | Visitante consome conteúdo (artigo, vídeo, landing) mas não se identificou. | Anônimo (cookie, com consentimento) | Retorna ≥2 vezes ou visita página de módulo/“Solicite uma demonstração” e inicia formulário | — | Marketing |
| 3 | CONVERSÃO | Visitante preenche formulário (demo, e-book, checklist) com consentimento registrado. | Lead (status NOVO) | Formulário válido: e-mail corporativo, empresa, cargo, consentimento marcado, UTMs gravadas | Registro no CRM em até 5 min (automático) | Marketing / automação |
| 4 | QUALIFICAÇÃO | Time avalia aderência (BANT/MEDDIC adaptado) e score. | Lead → MQL → SQL | Score ≥ corte da classe A ou B **e** conversa de qualificação confirma dor + papel decisório + janela de tempo | 1º contato: até 1 dia útil (classe A: 4 h úteis). Qualificação concluída: 5 dias úteis | SDR / Comercial |
| 5 | DEMONSTRAÇÃO | Demo executiva (30–40 min) agendada e realizada, por persona. | Oportunidade criada | Demo realizada com decisor ou influenciador + próximo passo acordado por escrito | Agendar em até 5 dias úteis após SQL; resumo pós-demo em 1 dia útil | Comercial |
| 6 | PROPOSTA | Proposta formal enviada após escopo validado. | Negócio em PROPOSTA | Escopo e stakeholders validados; proposta enviada; reunião de revisão agendada | Proposta em até 5 dias úteis após validação de escopo | Comercial |
| 7 | CONTRATAÇÃO | Negociação, análise jurídica/compras, assinatura. | Negócio GANHO ou PERDIDO | Contrato assinado (GANHO) ou decisão formal de não seguir (PERDIDO, com motivo) | Revisão semanal de negócios parados; sem SLA fixo (depende do cliente) | Comercial / Diretoria |

## Regras transversais
- **Descarte**: lead fora do ICP (não é operadora, estudante, concorrente direto, e-mail pessoal sem empresa) vai para "Descartado" com motivo; não entra em nutrição comercial.
- **Retorno ao nutrimento**: lead sem timing vai para nutrição (e-mails 5–8 do arquivo 05) e é reavaliado em 90 dias.
- **Mudança de etapa** sempre registra data, responsável e motivo (ver `12_CRM`).
- **Conversão entre etapas**: métricas medidas pelo dashboard (`13_DASHBOARD_MARKETING`). Nenhuma meta numérica foi inventada; metas são [A DEFINIR] com base nos primeiros 30 dias de dados reais.
- **Definições de qualidade**: MQL = formulário + score ≥ corte B; SQL = MQL + conversa de qualificação positiva.

## ICP (perfil de cliente ideal) — hipótese de trabalho [A CONFIRMAR]
Operadoras de planos de saúde (medicina de grupo, cooperativas, autogestões, seguradoras de saúde, odontológicas). Papéis: Diretoria (CEO/Superintendente), CFO/Financeiro, Controladoria/Contabilidade, Atuária, Gestão assistencial/Médico, Regulatório/Compliance, TI/BI.
