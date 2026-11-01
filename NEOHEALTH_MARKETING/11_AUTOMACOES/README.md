# 11_AUTOMACOES
Especificação de automações de captação e vendas (sem contratar/integrar nada).
- `01_especificacao_automacoes.md`: fluxos (Mermaid), etapas e regras.
- `fluxo_automacao.json`: definição genérica (desativada).
- `02_webhooks_utm_ga4.md`: payloads, convenção UTM, eventos GA4/GTM.
- `03_comparativo_ferramentas.md`: comparação (busca web) e recomendação.
- `prototipo/`: `score_leads.py` (Python 3, só biblioteca padrão) e `score_leads.gs` (Apps Script), `lead_scoring.csv` (cópia de `10_LEAD_GENERATION/12_lead_scoring.csv`), `leads_exemplo.csv` (dados fictícios), `leads_pontuados.csv` (saída).
Executar: `cd prototipo && python3 -I score_leads.py --leads leads_exemplo.csv --regras lead_scoring.csv --saida leads_pontuados.csv`. Não usa rede e não envia nada.
