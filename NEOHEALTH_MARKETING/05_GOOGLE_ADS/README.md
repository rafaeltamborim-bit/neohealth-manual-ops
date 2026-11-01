# 05_GOOGLE_ADS — Campanhas de Pesquisa (cenário R$ 1.200/mês)
Nada aqui foi publicado nem gasto. Tudo importa **pausado**. Siga a Ficha de Fatos (`01_ESTRATEGIA/00_FICHA_DE_FATOS.md`).

| Arquivo/pasta | Conteúdo |
|---|---|
| `PESQUISA_INTENCAO_SERP.md` | Intenção de busca, concorrência observável, o que NÃO foi possível verificar |
| `ESTRATEGIA_LANCES_ORCAMENTO.md` | Lance por fase, divisão do orçamento, hipóteses rotuladas |
| `PLANO_MEDICAO_CONVERSOES.md` | Eventos, UTM, GCLID, conversões offline, LGPD |
| `campanhas/01..07_*.md` | 7 campanhas: grupos, palavras (frase/exata), negativas, 15 títulos, 4 descrições, extensões, LP |
| `csv_editor/*.csv` | Importáveis no Google Ads Editor (campanhas, grupos, palavras, negativas, RSA, sitelinks, callouts, snippets) + lista compartilhada de negativas |
| `csv_editor/VERIFICACAO_CARACTERES.md` | Resultado da contagem automática (títulos ≤30, descrições ≤90, sitelinks, callouts) |
| `scripts/gerar_google_ads.py` | Fonte única: edite e rode `python3 -I scripts/gerar_google_ads.py` para regenerar CSVs e .md (aborta se algum limite for excedido) |
| `PENDENCIAS.md` | Pendências e [A CONFIRMAR] |

Contagem: 7 campanhas · 21 grupos · 144 linhas de palavra-chave · 21 RSAs (15 títulos + 4 descrições cada) · 28 sitelinks · 42 callouts · 7 snippets.
Notas de importação: cabeçalhos em inglês (use o Editor em inglês ou mapeie colunas); importe uma tabela por vez na ordem campanhas → grupos → palavras → negativas → RSA → extensões; o domínio `DOMINIO-A-CONFIRMAR` deve ser substituído antes. A lista compartilhada de negativas é criada manualmente (Biblioteca compartilhada) a partir do CSV e anexada às 7 campanhas.
