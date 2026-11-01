---
titulo_seo: "IDSS da ANS: o que é e como operadoras podem acompanhar"
meta_description: "Entenda o IDSS da ANS: as quatro dimensões (IDQS, IDGA, IDSM, IDGR), pesos, como o índice é composto e como acompanhar o desempenho da operadora."
slug: 06-idss
palavra_chave_principal: "IDSS ANS"
palavras_chave_secundarias:
  - "Índice de Desempenho da Saúde Suplementar"
  - "IDSS operadoras"
  - "Programa de Qualificação de Operadoras"
  - "IDQS IDGA IDSM IDGR"
intencao_de_busca: "Informacional (profissional de operadora que precisa entender o IDSS e como acompanhá-lo)"
data_base: 2026-11-01
status: rascunho para aprovação [A CONFIRMAR]
---

# IDSS da ANS: o que é e como operadoras podem acompanhar

O Índice de Desempenho da Saúde Suplementar (IDSS) é um dos instrumentos pelos quais a Agência Nacional de Saúde Suplementar (ANS) avalia operadoras de planos de saúde. Para quem gere uma operadora, entender como o IDSS é composto é o primeiro passo para acompanhá-lo ao longo do ano, e não apenas na divulgação dos resultados.

Este artigo explica, com base em documentos publicados pela ANS, o que é o IDSS, como se organiza, quais são as dimensões e como estruturar um acompanhamento interno. Seguindo a regra deste conteúdo, só citamos o que foi possível verificar; o restante aparece marcado como **[VERIFICAR NA FONTE]**.

> Nota de método: as informações abaixo foram identificadas em documentos do portal gov.br/ans localizados em 01/11/2026. A leitura integral dos PDFs não foi possível no ambiente de produção deste texto, de modo que pesos, bônus, indicadores e faixas devem ser conferidos nas fichas e nos métodos oficiais antes da publicação.

## O que é o IDSS

O IDSS integra o Programa de Qualificação de Operadoras (PQO) da ANS. De acordo com os documentos de método de cálculo publicados pelo órgão, ele é um índice composto, que varia de zero a um, calculado a partir de indicadores organizados em dimensões, e cada operadora é posicionada em uma faixa de avaliação [VERIFICAR NA FONTE as faixas e seus limites].

O resultado é divulgado em ciclos anuais, com um **ano-base** (o período dos dados) e um **ano de divulgação** (por exemplo, o método de cálculo "IDSS 2027" refere-se ao ano-base 2026; e o "IDSS 2025" ao ano-base 2024). Isso é importante: o que a operadora faz hoje impacta o ciclo de divulgação futuro, e o que se divulga hoje reflete o passado.

## As quatro dimensões

Segundo o método de cálculo do IDSS publicado para o ano-base 2026, o índice combina quatro dimensões:

| Dimensão | Sigla | Foco |
|---|---|---|
| Qualidade em atenção à saúde | IDQS | Qualidade do cuidado e resultados assistenciais |
| Garantia de acesso | IDGA | Acesso dos beneficiários aos serviços |
| Sustentabilidade no mercado | IDSM | Solidez econômico-financeira e aspectos de mercado |
| Gestão de processos e regulação | IDGR | Cumprimento de obrigações e processos junto ao regulador |

Os nomes e as siglas coincidem com os usados no inventário de telas da NeoHealth BI · OPS (IDQS, IDGA, IDSM e IDGR).

## Como as dimensões se combinam

O documento de método de cálculo do ano-base 2026 apresenta a fórmula de composição do índice:

**IDSS = (IDQS × 0,30) + (IDGA × 0,30) + (IDSM × 0,30) + (IDGR × 0,10)**

Ou seja, três dimensões pesam 30% cada e a dimensão de gestão de processos e regulação pesa 10%. Os pesos podem mudar entre ciclos; **confira sempre o documento do ano-base que você acompanha** [VERIFICAR NA FONTE].

Os documentos consultados indicam ainda que:

- Cada **indicador** tem um índice de desempenho, obtido pela relação entre o resultado da operadora e a pontuação máxima definida pela ANS para o indicador.
- O resultado de cada **dimensão** é uma soma ponderada dos índices dos indicadores que a compõem.
- O relatório do ano-base 2024 refere **33 indicadores** distribuídos nas quatro dimensões, além de um indicador de **bônus** associado ao programa de acreditação de operadoras [VERIFICAR NA FONTE a lista de indicadores, os pesos de cada um e os valores do bônus, que variam conforme o nível de acreditação].

## Fontes de dados do IDSS

Os indicadores são calculados pela ANS a partir de bases que as operadoras enviam ou que o regulador consulta, por exemplo informações de beneficiários, de produtos, da troca de informações em saúde suplementar (TISS) e de dados econômico-financeiros [VERIFICAR NA FONTE quais bases alimentam cada indicador]. Na prática, isso significa que **a qualidade do envio influencia o resultado**: dados incompletos ou fora do prazo podem afetar o indicador.

Por isso, o acompanhamento do IDSS passa pelo acompanhamento das obrigações de envio. Veja o panorama em [Indicadores fundamentais para operadoras](/blog/02-indicadores-fundamentais-operadoras).

## Por que acompanhar o IDSS durante o ano

Esperar a divulgação oficial para conhecer o desempenho tem limitações:

1. **Defasagem:** o resultado oficial refere-se a um período já encerrado.
2. **Sem tempo de resposta:** se o problema está na qualidade do dado enviado, a correção deveria ter ocorrido antes.
3. **Diagnóstico tardio:** é difícil saber qual dimensão ou indicador mais contribuiu para o resultado.

Uma abordagem proativa consiste em **reproduzir internamente o cálculo** dos indicadores com os dados da própria operadora, conforme as fichas técnicas oficiais, e comparar com o resultado divulgado. Diferenças (por exemplo, no tratamento de registros, na janela de dados ou na versão da base) ajudam a descobrir problemas de qualidade de dados e de processo.

A NeoHealth BI · OPS possui um grupo de telas "Gestão de IDSS", com visão do IDSS, comparativo entre o resultado calculado e o resultado da ANS, plano de ação e telas dedicadas às dimensões IDQS, IDGA, IDSM e IDGR, além de visão de capital regulatório [DISPONÍVEL, conforme inventário de tutoriais; telas gravadas em base de demonstração com dados fictícios].

## Passo a passo para estruturar o acompanhamento

### 1. Obtenha os documentos oficiais do ano-base

Para cada ciclo, a ANS publica o método de cálculo, fichas técnicas dos indicadores e perguntas e respostas (FAQ). Reúna esses documentos e registre a versão utilizada.

### 2. Monte o dicionário dos indicadores

Para cada indicador: nome, dimensão, fórmula, fonte de dados, periodicidade, responsável interno e área impactada. Veja o roteiro em [Como estruturar BI para operadoras](/blog/01-como-estruturar-bi-operadoras).

### 3. Replique o cálculo e compare com o oficial

Calcule os indicadores internamente e compare com o resultado divulgado. Documente as diferenças e investigue as causas. É um excelente teste de qualidade de dados.

### 4. Acompanhe a evolução por dimensão

Em vez de olhar só a nota final, acompanhe cada dimensão. Como as dimensões IDQS, IDGA e IDSM pesam, cada uma, três vezes o peso da IDGR no cálculo do ano-base 2026, uma variação em uma delas pode ter maior efeito sobre o índice final. Mas lembre-se de que o peso de cada **indicador** dentro da dimensão também importa [VERIFICAR NA FONTE].

### 5. Crie um plano de ação por indicador

Priorize indicadores com maior potencial de melhora e menor custo de intervenção. Para cada ação: responsável, prazo, evidência de conclusão. Revise em ciclos mensais ou trimestrais.

### 6. Conecte o IDSS à gestão assistencial e financeira

Indicadores de qualidade e acesso dependem de ações assistenciais; os de sustentabilidade, da gestão financeira; os de processos, do cumprimento de obrigações. Por isso o IDSS não pertence a uma única área. Leia também [Indicadores assistenciais](/blog/05-indicadores-assistenciais) e [Gestão financeira na saúde suplementar](/blog/04-gestao-financeira-saude-suplementar).

## Dimensão por dimensão: o que costuma exigir atenção

### IDQS: qualidade em atenção à saúde

Reúne indicadores de natureza assistencial. A operadora costuma precisar de dados clínicos e administrativos bem estruturados e de processos de cuidado, prevenção e acompanhamento. Quais indicadores compõem a dimensão no ciclo que você acompanha: [VERIFICAR NA FONTE].

### IDGA: garantia de acesso

Relaciona-se com a capacidade de a rede atender beneficiários nas condições previstas. Pode envolver aspectos como cobertura de rede e prazos de atendimento [VERIFICAR NA FONTE os indicadores e as normas de garantia de atendimento, como a RN 623].

### IDSM: sustentabilidade no mercado

Aborda a situação econômico-financeira e a trajetória de mercado da operadora. É a dimensão mais ligada à gestão financeira, à contabilidade e ao acompanhamento prudencial [VERIFICAR NA FONTE os indicadores].

### IDGR: gestão de processos e regulação

Tem peso menor no cálculo (0,10 no ano-base 2026), mas costuma estar ligada a processos que a operadora controla diretamente, como cumprimento de envios e rotinas regulatórias [VERIFICAR NA FONTE os indicadores].

## Boas práticas de governança do IDSS

- **Um dono** para o tema, com interlocução entre assistencial, financeiro, TI e regulatório.
- **Calendário regulatório** de envios, com verificação de qualidade antes do prazo.
- **Trilha de auditoria** das alterações em dados enviados.
- **Reunião periódica** de acompanhamento do IDSS, com plano de ação.
- **Documentação das diferenças** entre o cálculo interno e o oficial.
- **Cultura de dados:** treinar equipes que registram informações, porque a qualidade nasce na origem.

## Erros comuns

- **Olhar apenas a nota final,** sem decompor por dimensão e indicador.
- **Não registrar a versão** do método de cálculo usada.
- **Confundir ano-base com ano de divulgação.**
- **Tratar o IDSS como "projeto de TI"** em vez de tema de gestão multidisciplinar.
- **Prometer metas** de nota sem conhecer a metodologia detalhada. Ações apoiadas por dados ajudam a identificar oportunidades, mas o resultado depende de muitos fatores.

## Como a NeoHealth BI · OPS apoia o pilar Regulatório

O pilar Regulatório oferece mais visibilidade sobre indicadores, obrigações e riscos regulatórios. No contexto do IDSS, a plataforma organiza as dimensões, o comparativo entre o resultado calculado e o resultado da ANS e o plano de ação [DISPONÍVEL, conforme inventário], além de módulos relacionados a RN 518, RN 623, TISS, SIB e Sala de Situação ANS [DISPONÍVEL, conforme ficha de fatos]. A plataforma não garante nota ou classificação; apoia a organização da informação e das decisões. Saiba mais: [/#pilar](/#pilar).

Imagens de tela em materiais da NeoHealth correspondem a dados fictícios (base de demonstração "Operadora Modelo").

## Perguntas frequentes

**O IDSS é obrigatório?** O IDSS é calculado pela ANS para as operadoras no âmbito do programa de qualificação; regras de participação, exceções e consequências: [VERIFICAR NA FONTE].

**Qual a faixa de pontuação?** Os documentos consultados indicam escala de zero a um, com faixas de avaliação definidas pela ANS [VERIFICAR NA FONTE os limites].

**Quando sai o resultado?** A ANS divulga em ciclo anual; a data exata de cada ciclo deve ser consultada no portal [VERIFICAR NA FONTE].

**Os pesos são sempre os mesmos?** Não necessariamente. Consulte o método do ano-base que está acompanhando.

## Referências oficiais (consulta em 01/11/2026)

- ANS, Método de Cálculo IDSS 2027 (ano-base 2026): https://www.gov.br/ans/pt-br/arquivos/acesso-a-informacao/perfil-do-setor/dados-e-indicadores-do-setor/dados-do-programa-de-qualificacao-de-operadoras/2027/Mtodo_de_Clculo_IDSS_anobase_2026.pdf — consulta em 01/11/2026 (fórmula e pesos conforme resumo de busca; PDF não aberto diretamente).
- ANS, Método de Cálculo IDSS 2025 (ano-base 2024): https://www.gov.br/ans/pt-br/acesso-a-informacao/perfil-do-setor/dados-e-indicadores-do-setor/METODO_DE_CALCULO_IDSS_ab_2024.pdf — consulta em 01/11/2026.
- ANS, Relatório do Programa de Qualificação de Operadoras, IDSS ano-base 2024: https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/Relatrio_IDSS_AB_2024_r03.pdf — consulta em 01/11/2026 (33 indicadores e bônus de acreditação conforme resumo de busca; [VERIFICAR NA FONTE]).
- ANS, Ficha Técnica IDSS ano-base 2026: https://www.gov.br/ans/pt-br/arquivos/acesso-a-informacao/perfil-do-setor/dados-e-indicadores-do-setor/dados-do-programa-de-qualificacao-de-operadoras/2027/Ficha_IDSS_ab2026_site.pdf — consulta em 01/11/2026 (valores de bônus: [VERIFICAR NA FONTE]).
- ANS, Perguntas e Respostas IDSS ano-base 2024: https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/FAQ_IDSS_anobase_2024_vf_site_CORRIGIDO.pdf — consulta em 01/11/2026.

## Leia também

- [Indicadores fundamentais para operadoras](/blog/02-indicadores-fundamentais-operadoras)
- [Indicadores assistenciais](/blog/05-indicadores-assistenciais)
- [Gestão financeira na saúde suplementar](/blog/04-gestao-financeira-saude-suplementar)
- [Como estruturar BI para operadoras](/blog/01-como-estruturar-bi-operadoras)

**Solicite uma demonstração.** Veja como a plataforma organiza o acompanhamento do IDSS e das obrigações regulatórias da sua operadora: [/#pilar](/#pilar).

*Conheça o potencial dos dados da sua operadora.*

---
**Funcionalidades citadas e status:** Gestão de IDSS (IDSS, Comparativo Calculado x ANS, Plano de Ação, IDQS, IDGA, IDSM, IDGR, Capital Regulatório, Configurações) [DISPONÍVEL, conforme inventário]; RN 518, RN 623, TISS, SIB, Sala de Situação ANS [DISPONÍVEL, conforme ficha de fatos].
