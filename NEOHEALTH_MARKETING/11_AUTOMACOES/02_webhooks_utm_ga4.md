# Webhooks, convenção de UTMs e eventos GA4/GTM
> Especificação. Nenhum container GTM, propriedade GA4 ou webhook foi criado. IDs: `GTM-[A DEFINIR]`, `G-[A DEFINIR]`.

## 1. Webhook de captura (formulário → automação/CRM)
**POST** `https://[HOST-A-DEFINIR]/lead-capture` · `Content-Type: application/json` · Header `X-NeoHealth-Signature: HMAC-SHA256(body, segredo)` (segredo em variável de ambiente; **nunca** no front-end — preferir enviar do servidor/ferramenta de formulário, não do navegador).
```json
{
  "form_id": "demo-v1",
  "timestamp_utc": "2026-11-01T12:00:00Z",
  "nome": "Exemplo Fictício",
  "email": "pessoa@operadora-exemplo.example",
  "telefone": "+55 11 90000-0000",
  "empresa": "Operadora Exemplo",
  "tipo_operadora": "Medicina de grupo",
  "porte": "Faixa 2",
  "cargo": "Financeiro/Controladoria",
  "erp": "Philips Tasy",
  "desafios": ["Sinistralidade", "Obrigações regulatórias/ANS"],
  "mensagem": "",
  "consentimento_contato": true,
  "consentimento_marketing": false,
  "versao_texto_consentimento": "2026-11-v1",
  "utm_source": "linkedin", "utm_medium": "paid_social", "utm_campaign": "demo-q4-2026",
  "utm_content": "criativo-fin-01", "utm_term": "",
  "pagina_origem": "https://[DOMINIO-A-DEFINIR]/demonstracao", "referrer": "", "honeypot": ""
}
```
**Respostas:** `202 Accepted` (ok) · `400` (validação; corpo com campos inválidos) · `401` (assinatura) · `409` (duplicidade tratada como update, retornar 200) · `429` · `5xx` (retry com backoff). Idempotência: header `Idempotency-Key` = hash(email+form_id+timestamp arredondado ao minuto).

## 2. Outros webhooks (eventos)
| Evento | Origem | Destino | Payload mínimo |
|---|---|---|---|
| `meeting.booked` | Agenda | Automação/CRM | email, data/hora, responsável |
| `meeting.completed` | CRM (ação manual) | Automação | deal_id, resultado |
| `email.unsubscribed` | Ferramenta de e-mail | CRM | email, timestamp, canal |
| `whatsapp.optout` | Provedor WhatsApp | CRM | telefone (hash), timestamp |
| `deal.stage_changed` | CRM | Dashboard | deal_id, de, para, timestamp |

## 3. Convenção de UTMs
Regras: minúsculas, sem acentos/espaços (usar `-`), sem dados pessoais, nomes estáveis. Documentar tudo em planilha de UTMs.
| Parâmetro | Padrão | Valores permitidos / exemplos |
|---|---|---|
| utm_source | plataforma | `linkedin`, `google`, `meta`, `youtube`, `email`, `whatsapp`, `site`, `indicacao`, `evento` |
| utm_medium | tipo | `paid_social`, `cpc`, `organic_social`, `organic_search`, `email`, `video`, `referral`, `direct_msg` |
| utm_campaign | `{objetivo}-{tema}-{periodo}` | `demo-geral-q4-2026`, `ebook-do-dado-a-decisao-2026-11`, `nutricao-seq-2026q4` |
| utm_content | `{pilar}-{formato}-{versao}` | `fin-carrossel-v1`, `sin-video15-v2`, `email-03` |
| utm_term | palavra-chave (apenas busca paga) | `bi-para-operadoras` |
Exemplo: `https://[DOMINIO]/demonstracao?utm_source=linkedin&utm_medium=paid_social&utm_campaign=demo-geral-q4-2026&utm_content=sin-video15-v1`  
Persistência: gravar UTMs da **primeira** e da **última** sessão (campos `utm_*_first`/`utm_*_last`), somente após consentimento de cookies/analytics.

## 4. Eventos GA4 (via GTM)
| Evento | Disparo | Parâmetros | Conversão? |
|---|---|---|---|
| `page_view` | automático | page_location etc. | Não |
| `scroll` | 75% (recomendado/enhanced) | — | Não |
| `view_content_pillar` | visita a página de pilar | `pillar` (financeira/sinistralidade/assistencial/regulatoria/preditiva) | Não |
| `video_progress` | 25/50/75% em vídeo | `video_id`, `percent` | Não |
| `cta_click` | clique em "Solicite uma demonstração" / secundário | `cta_id`, `cta_text`, `page_section` | Não |
| `form_start` | primeiro foco no formulário | `form_id` | Não |
| `generate_lead` | envio válido do formulário (padrão recomendado GA4) | `form_id`, `lead_type` (demo/ebook/checklist), `pillar_interest` | **Sim** |
| `file_download` | download do e-book/checklist | `file_name` | Sim (micro) |
| `schedule_meeting` | agendamento concluído | `meeting_type` | Sim |
| `qualified_lead` | importação offline/MP quando CRM marcar SQL | `lead_class` | Sim (offline) |
Nunca enviar e-mail, nome ou telefone como parâmetro ao GA4/Ads/Meta (política de dados pessoais das plataformas) [VERIFICAR NA FONTE].
**GTM:** tags GA4 Config + eventos; variáveis (DLV `form_id`, `cta_id`); acionadores por data layer: `dataLayer.push({event:'generate_lead', form_id:'demo-v1', lead_type:'demo'})`. **Consent Mode**: ligar com banner de cookies; sem consentimento, sem tags de marketing.
## 5. Retorno ao CRM (offline conversions)
Quando o CRM marcar SQL/Oportunidade, exportar `gclid`/`li_fat_id`/`fbclid` + estágio para importação nas plataformas de mídia, **somente com aprovação e base legal**.
