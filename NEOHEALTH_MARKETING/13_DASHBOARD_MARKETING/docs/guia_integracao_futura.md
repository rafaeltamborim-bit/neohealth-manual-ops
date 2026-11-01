# Guia de integração futura (somente instruções — nada foi conectado)

Nenhuma integração existe hoje; todas dependem de aprovação e de credenciais do proprietário [A CONFIRMAR]. O painel segue lendo CSV.

## Caminho recomendado
1. Consolidar exportações em uma planilha (estrutura em `templates/planilha_estrutura.csv`), uma linha por dia × campanha.
2. Conectar a planilha ao **Looker Studio** (conector Google Sheets) e mapear os campos com os mesmos nomes do dicionário; criar campos calculados com as fórmulas de `dicionario_de_metricas.md` (usar `SAFE_DIVIDE`/`CASE WHEN denominador=0 THEN NULL`).
3. Opcional: baixar CSV do Looker/planilha e abrir no painel HTML.

## Fontes
- **GA4**: no Looker Studio, conector Google Analytics (GA4); trazer sessões e eventos-chave (envio de formulário, clique em CTA) por origem/mídia/campanha (UTM). Marcar eventos-chave no GA4 e no Tag Manager antes. Documentação: support.google.com/analytics.
- **Google Ads**: conector Google Ads do Looker Studio (campanha, custo, impressões, cliques, conversões). API: Google Ads API (exige developer token e conta aprovada).
- **Meta Ads**: Marketing API / exportação agendada para CSV; conectores de terceiros exigem avaliação de LGPD e custo [A CONFIRMAR].
- **LinkedIn Ads**: exportação CSV do Campaign Manager ou Marketing API (acesso sujeito à aprovação da LinkedIn).
- **YouTube**: via Google Ads (campanhas de vídeo) e YouTube Analytics.
- **CRM** (ver 12_CRM): exportar leads, qualificados, oportunidades, reuniões, demonstrações, propostas, conversões e receita por campanha (campo de origem/UTM obrigatório no lead).

## Chave de junção
`data + canal + campanha` com nomes padronizados (convenção UTM: utm_source=canal, utm_campaign=campanha). Sem UTM consistente não há atribuição.

## Governança
Sem dados pessoais de saúde ou de leads individuais no painel (apenas agregados); acesso restrito; registrar base legal (LGPD); revisar permissões de cada API antes de conectar.
