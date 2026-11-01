# Matriz de Concorrência e Alternativas
Data da consulta: **01/11/2026**. Dados estruturados em `matriz_concorrencia.csv` (16 linhas).

## Limites desta pesquisa (leia primeiro)
- A pesquisa foi feita via WebSearch; o acesso direto (WebFetch) a sites externos estava **bloqueado** no ambiente (hosts benner.com.br, support.google.com, linkedin.com não resolveram). Portanto o conteúdo das URLs foi lido **apenas por resumos de busca**, não pelas páginas inteiras.
- Cada linha traz o nível de verificação. Preços são **valores de lista informados em resumos**, em USD, que variam por região e data: **não usar externamente sem validar na página oficial**.
- Não foram verificados: tabelas de preço em R$, funcionalidades atuais de BI dos ERPs, nem consultorias específicas. Não há afirmações de superioridade.
- A integração com o Philips Tasy consta na Ficha de Fatos; qualquer relação de parceria/homologação é [A CONFIRMAR].

## 1. Categorias e itens (resumo)
| Categoria | Itens (ver CSV para URL e data) | Verificação |
|---|---|---|
| BI genérico | Power BI, Qlik Cloud Analytics, Tableau, Looker / Looker Studio Pro | Parcial (Tableau: só secundárias) |
| Módulo gerencial de sistemas de operadoras | Philips Tasy Operadoras, TOTVS Saúde, Benner Saúde/BI, MV SOUL Operadora | Parcial |
| Analytics de saúde (nacional/regional) | Dedalus BI4H, painel UNIDAS (associativo) | Baixa/Parcial |
| Analytics de saúde (internacional) | Health Catalyst, Arcadia, Innovaccer (foco em mercado dos EUA, conforme agregadores) | Baixa |
| Fonte pública | Dados abertos/painéis ANS | Oficial |
| Consultorias | Categoria genérica, sem nomes | Não verificado |
| Desenvolvimento interno | Categoria genérica | N/A |

## 2. Como comparar a proposta de valor por categoria
Princípio: comparar **critérios de decisão** do cliente, não declarar vencedor.

**a) BI genérico (Power BI, Qlik, Tableau, Looker)**
- São ferramentas de uso geral: a operadora constrói modelo de dados, métricas e dashboards. A NeoHealth é uma plataforma setorial com análises organizadas por temas da saúde suplementar (inventário de telas).
- Perguntas para o cliente: quanto tempo e que equipe levaria para modelar IDSS/RN 518/RN 623/TISS/PTU nas ferramentas atuais? Quem mantém? Há necessidade de complementar em vez de substituir? [exportação/API: A CONFIRMAR]
- Mensagem permitida: "Uma plataforma construída para a saúde suplementar, que pode coexistir com o BI que você já usa [A CONFIRMAR possibilidade de coexistência técnica]."

**b) Módulos gerenciais de sistemas de gestão de operadoras (Tasy, TOTVS, Benner, MV)**
- Esses fornecedores descrevem soluções de gestão operacional com algum componente gerencial/BI. A NeoHealth declara integração com o Tasy e foco em inteligência estratégica sobre os dados.
- Perguntas: o módulo gerencial atual cobre as análises dos cinco pilares? Qual a profundidade em sinistralidade, assistencial e regulatória? Quanto depende de customização?
- Mensagem permitida: "Camada de inteligência estratégica sobre a operação que você já tem [integração Tasy conforme Ficha; demais ERPs A CONFIRMAR]."

**c) Analytics de saúde internacionais**
- Foco informado em mercado norte-americano (provedores/pagadores, value-based care). Comparar apenas em: aderência regulatória brasileira (ANS/TISS/PTU), idioma, suporte local, residência de dados.
- Não alegar ausência de funcionalidades deles.

**d) Consultorias de indicadores**
- Serviço sob demanda × plataforma contínua. Pode ser complementar (a consultoria interpreta; a plataforma dá visibilidade contínua). Sem citar nomes.

**e) Desenvolvimento interno**
- Custo total (pessoas, manutenção, atualização normativa) × plataforma pronta. Comparar com perguntas, não com números inventados. Dados de custo do cliente devem vir do próprio cliente.

## 3. O que NÃO afirmar
- "Melhor", "único", "líder", "mais completo", "mais barato", "mais rápido" ou qualquer comparativo de superioridade.
- Preços de concorrentes em material público (variáveis e não validados).
- Que concorrentes "não têm" determinado recurso.
- Quantidade de telas como diferencial (regra da Ficha).
- Parceria, homologação ou certificação com Philips/Tasy, Oracle ou qualquer fornecedor sem confirmação.
- Clientes, cases, depoimentos, prêmios, participação de mercado.
- Resultados/economia/redução de sinistralidade.
- Aderência plena a normas ANS sem fonte oficial e validação do proprietário.
- Nomes de operadoras (ex.: Unimed SC, HBC Saúde) como evidência de mercado: são clientes de terceiros.

## Pendências
- Reabrir as URLs com WebFetch liberado e promover os níveis "Parcial/Baixa" a "Verificado".
- Obter URL oficial de preços Tableau.
- Pesquisar consultorias e outros fornecedores nacionais (ex.: soluções específicas de BI para operadoras) com URLs.
- Proprietário: lista de concorrentes que aparecem em propostas reais [A CONFIRMAR].
