# Roteiro de qualificação — BANT/MEDDIC adaptado a operadoras
Duração: 15–25 min (ligação ou vídeo). Objetivo: decidir se há aderência e agendar a demonstração. Tom consultivo; não pressionar; não prometer resultados. Registrar tudo no CRM (campos entre colchetes).

## Abertura (1 min)
"Olá, {{nome}}, aqui é {{SDR}}, da NeoHealth. Você pediu [material/demonstração]. Posso fazer algumas perguntas rápidas para direcionar a conversa ao que importa para a {{empresa}}? Leva uns 15 minutos."

## Matriz BANT + MEDDIC adaptada
| Dimensão | Origem | Perguntas | Sinais positivos | Sinais de alerta | Campo CRM |
|---|---|---|---|---|---|
| **Need / Dor (Identify Pain)** | BANT-N, MEDDIC-I | "Qual decisão hoje chega tarde ou sem dados suficientes?" "Quais áreas (financeiro, sinistralidade, assistencial, regulatório, preditivo) mais pesam?" "Como vocês acompanham isso hoje?" | Dor concreta, citada com exemplo; consolidação manual | "Estamos só olhando" sem tema | dor_principal, pilar_interesse |
| **Metrics** | MEDDIC-M | "Que indicadores a diretoria acompanha? Qual melhoraria a conversa de gestão se fosse mais rápido/confiável?" | Indicadores nomeados | Sem indicadores definidos | indicadores_chave |
| **Authority / Economic Buyer** | BANT-A, MEDDIC-E | "Quem decide ou aprova uma ferramenta assim? Quem mais deveria ver a demonstração?" | Decisor identificado ou acessível | Ninguém sabe quem decide | decisor, stakeholders |
| **Champion** | MEDDIC-C | "Você usaria? Defenderia internamente?" | Interesse pessoal e acesso à diretoria | Sem influência | campeao |
| **Decision criteria / process** | MEDDIC-D,D | "Como a operadora avalia fornecedores? TI, jurídico, compras participam? Há comitê?" | Processo conhecido | Processo opaco | processo_decisao |
| **Timing** | BANT-T | "Existe uma janela (orçamento, ciclo regulatório, troca de sistema) para decidir?" | Janela ≤ 6 meses | Sem previsão | janela_decisao |
| **Budget** | BANT-B | "Esse tema tem orçamento previsto ou precisaria ser criado? Como costumam aprovar?" (não perguntar valor de cara) | Orçamento existe/pode ser criado | "Sem verba este ano" | orcamento_status |
| **Contexto técnico** | adaptação | "Qual ERP/sistema de gestão? Há equipe de BI/TI? Preferência por implantação em ambiente próprio (on-premise)?" | Tasy/Oracle (aderência confirmada), TI disponível | Sistemas sem conector [A CONFIRMAR] | erp_utilizado, implantacao |
| **Concorrência / alternativa** | MEDDIC-C | "O que usam hoje (planilhas, BI genérico, outro fornecedor)?" Não criticar concorrentes. | Ferramentas atuais insatisfatórias | Contrato recente | alternativa_atual |

## Pontuação de qualificação (0–2 por dimensão)
0 = desconhecido/negativo · 1 = parcial · 2 = claro. Dimensões: Dor, Autoridade, Timing, Budget, Contexto técnico, Champion. 
- **SQL** (avança para demonstração): Dor = 2 **e** soma ≥ 7 de 12. 
- **Nutrição**: Dor ≥ 1 mas soma < 7. 
- **Descarte**: fora do ICP ou Dor = 0 sem perspectiva.
(Cortes são hipótese de trabalho [A CONFIRMAR] e devem ser calibrados após as primeiras 20 qualificações.)

## Fechamento
"Pelo que entendi, o ponto principal é {{dor}}. Sugiro uma demonstração de 30–40 minutos focada em {{pilar}}, com {{stakeholders}}. Terça ou quinta funciona?" Confirmar por e-mail com convite.

## Regras
- Não coletar dados pessoais de saúde ou de beneficiários.
- Se pedirem preço: explicar que a proposta depende de escopo.
- Registrar a origem da informação e atualizar consentimento se o contato permitir novo canal.
