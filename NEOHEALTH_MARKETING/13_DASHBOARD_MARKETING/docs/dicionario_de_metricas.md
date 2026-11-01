# Dicionário de métricas — Painel de Marketing NeoHealth BI · OPS

Regra geral: toda razão com denominador 0 (ou vazio) é exibida como **"—"** (nunca 0, nunca infinito). Somas ignoram valores negativos/inválidos (tratados como 0). Linhas de vários arquivos são somadas.

| Métrica | Fórmula | Fonte do dado | Observações |
|---|---|---|---|
| Investimento | Σ investimento | plataformas de mídia / financeiro | só valores realmente gastos e aprovados |
| Impressões | Σ impressoes | Ads / YouTube | |
| Cliques | Σ cliques | Ads / YouTube | |
| CTR | cliques ÷ impressões | calculado | |
| CPC | investimento ÷ cliques | calculado | |
| Leads | Σ leads | formulários / CRM | LGPD: só leads com base legal registrada |
| CPL | investimento ÷ leads | calculado | |
| Leads qualificados | Σ leads_qualificados | CRM | critério [A CONFIRMAR com Comercial] |
| Oportunidades | Σ oportunidades | CRM | |
| Custo por oportunidade | investimento ÷ oportunidades | calculado | |
| Reuniões / Demonstrações / Propostas | Σ respectivas colunas | CRM | |
| Conversões | Σ conversoes | CRM | contratos fechados |
| CAC | investimento ÷ conversões | calculado | considera só o investimento lançado; custos de equipe/ferramentas entram apenas se lançados [A CONFIRMAR] |
| Receita | Σ receita | CRM / financeiro | regra de reconhecimento [A CONFIRMAR] |
| ROI | (receita − investimento) ÷ investimento | calculado | indefinido (—) se investimento = 0 |
| Taxa entre etapas do funil | etapa ÷ etapa anterior | calculado | — se anterior = 0 |

## Esquema dos CSV
Colunas: `data, canal, campanha, etapa_comercial, investimento, impressoes, cliques, leads, leads_qualificados, oportunidades, reunioes, demonstracoes, propostas, conversoes, receita`.
- `dados_marketing.csv`: mídia + leads (investimento, impressões, cliques, leads). `funil.csv`: etapas comerciais (leads_qualificados … receita). Pode-se também usar um único arquivo completo. **Nunca repita a mesma coluna em dois arquivos**, pois os valores são somados.
- Separador `,` ou `;`; decimal ponto ou vírgula; data `AAAA-MM-DD` ou `DD/MM/AAAA`; acentos nos cabeçalhos aceitos.
- Filtros: canal, campanha, etapa_comercial, período (de/até). Tendência agrupa por semana (segunda-feira).

## Semáforos de realocação
Sem metas: CAC ≤ 120% do CAC do conjunto E ROI ≥ 80% do ROI do conjunto = verde (candidata a ampliar); ambos fora = vermelho (rever/reduzir); misto ou sem conversões = amarelo; investimento < mínimo ou sem leads/conversões = cinza. Com metas (campos "Meta CAC", "Meta ROI" — valores **[A CONFIRMAR]** pelo proprietário), as metas substituem as referências relativas. É apoio à decisão, não garantia de resultado; realocar orçamento exige aprovação.

## Dados de exemplo
O botão "Carregar exemplo" gera dados sintéticos determinísticos, com campanhas marcadas `[EXEMPLO]` e faixa "DADOS DE EXEMPLO — NÃO SÃO RESULTADOS REAIS". Arquivos em `exemplos/` têm o mesmo conteúdo (campanhas `[EXEMPLO]`). Não representam desempenho real nem benchmarks.
