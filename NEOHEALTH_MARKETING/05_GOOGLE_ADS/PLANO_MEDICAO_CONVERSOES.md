# Plano de medição e conversões (inclui offline)
## Eventos (GTM/GA4 → importar para Google Ads)
| Evento | Gatilho | Tipo no Google Ads | Valor |
|---|---|---|---|
| `generate_lead_demo` | envio do formulário "Solicite uma demonstração" | **Principal** | [A CONFIRMAR valor] |
| `click_whatsapp` | clique no botão WhatsApp (se existir) | Secundária | – |
| `view_video_demo` | ≥50% de vídeo demonstrativo (7 min máx.) | Secundária (observação) | – |
| `scroll_75` / `cta_click` | 75% da página / clique em CTA | Observação (não otimizar) | – |
| `lead_mql`, `lead_sql`, `opportunity`, `won` | importação offline do CRM (12_CRM) | MQL/SQL como principais futuras; ganho com valor | valor real do contrato [A CONFIRMAR] |
## Captura e UTM
- Parâmetros: `utm_source=google`, `utm_medium=cpc`, `utm_campaign=<slug>`, `utm_term={keyword}`, `utm_content={creative}`; ativar **marcação automática (gclid)** e manter UTM manuais para GA4/CRM.
- Formulário guarda em campos ocultos: gclid, gbraid/wbraid, UTM, URL de origem, timestamp, **consentimento (checkbox não pré-marcado + versão da política)**.
## Conversão offline (fluxo)
1. Lead chega com gclid → gravado no CRM. 2. Equipe comercial qualifica (cargo de decisão em operadora? porte? demo realizada?). 3. A cada estágio, exportar CSV (GCLID, nome da conversão, data/hora com fuso, valor) ou integrar via API/Zapier; **importar em até 90 dias do clique**. 4. Optar por "Conversões otimizadas" = lead qualificado quando houver ≥10-15 por mês [HIPÓTESE].
## Conversões avançadas para leads
Pode enviar e-mail com hash SHA-256 **somente com consentimento** e conforme a política de dados do Google. [A CONFIRMAR com jurídico/DPO.]
## LGPD e Consent Mode
Banner de cookies com Consent Mode v2 (necessário para medir no EEE; no Brasil, recomendado como boa prática) [A CONFIRMAR]. Sem dados de saúde pessoais em eventos. Política de privacidade na LP.
## Validação antes de ativar
Tag Assistant, teste de formulário real (marcar como teste), conferir 1 conversão no Google Ads, conferir recebimento no CRM com UTM e gclid.
