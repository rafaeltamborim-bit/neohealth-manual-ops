---
titulo_seo: "Gestão de glosas em operadoras: dados e indicadores"
meta_description: "Como acompanhar glosas por prestador, procedimento e beneficiário, tratar contestações e usar dados para apoiar a relação com a rede. Guia prático."
slug: 10-gestao-glosas-operadoras
palavra_chave_principal: "gestão de glosas"
palavras_chave_secundarias:
  - "glosas operadoras de planos de saúde"
  - "análise de contas médicas"
  - "recurso de glosa TISS"
  - "indicadores de glosa ANS"
  - "outliers contas médicas"
intencao_de_busca: "Informacional/investigação de solução: equipes de contas médicas, auditoria e rede buscam método e indicadores para gerir glosas."
pilar: "Assistencial / Sinistralidade"
status_publicacao: "RASCUNHO — depende de aprovação do proprietário"
data_base: "01/11/2026"
---

# Gestão de glosas: como transformar divergências de cobrança em informação de gestão

Não espere o fechamento do mês para identificar os fatores que pressionam a sinistralidade. A análise de contas médicas e a gestão de glosas estão entre as áreas em que dados bem organizados fazem mais diferença: cada divergência de cobrança carrega informação sobre cadastro, contrato, processo de autorização e comportamento da rede. Este guia apresenta um modelo para acompanhar glosas de forma sistemática, sem prometer resultado e sem simplificar a complexidade da relação com os prestadores.

## O que é glosa e por que ela merece gestão

Glosa é, em linhas gerais, a recusa total ou parcial de um valor cobrado por um prestador à operadora, por inconformidade com regras contratuais, cobertura, autorização ou documentação. Em contas médicas, ela é uma ferramenta de controle; ao mesmo tempo, quando mal gerida, vira fonte de atrito, retrabalho e disputa.

Do ponto de vista de gestão, três perguntas orientam o tema:

1. **Qual é o volume e o valor glosado, e como evolui?**
2. **Onde estão concentradas as glosas (prestador, procedimento, motivo, beneficiário)?**
3. **O que acontece depois da glosa (contestação, recurso, acordo, reversão)?**

Responder a essas perguntas com dados conciliados evita decisões baseadas em casos isolados.

### Padrão TISS e transparência

A ANS mantém o Padrão TISS (Troca de Informações na Saúde Suplementar), que padroniza a troca eletrônica entre operadoras e prestadores. Os componentes organizacionais publicados pela ANS descrevem, entre outros, processos de cobrança de serviços e de recurso de glosa. A agência também disponibilizou um **Painel de Indicadores de Glosa**, com indicadores construídos a partir de dados recebidos via TISS, com a finalidade de promover transparência nas relações entre prestadores e operadoras. A descrição detalhada de cada indicador e da periodicidade deve ser conferida na fonte: **[VERIFICAR NA FONTE]**.

Regras específicas sobre glosa, prazos de resposta e de pagamento e eventuais obrigações de justificativa: **[VERIFICAR NA FONTE]**. Este artigo não reproduz prazos nem percentuais de memória.

## Cinco visões para entender as glosas

### 1. Visão por prestador

Mostra quem concentra mais glosas, em valor e em frequência, e se existe padrão recorrente. É a visão que mais conecta a gestão de glosas à [gestão de prestadores](/blog/09-gestao-prestadores-operadoras). Cuidado: um prestador pode ter mais glosas simplesmente por ter mais volume; comparações devem considerar a proporção.

### 2. Visão por procedimento

Revela procedimentos com maior incidência de divergência. Pode indicar regra contratual pouco clara, tabela desatualizada, cobrança inadequada ou problema de cadastro. É a visão mais útil para ajustar regras e comunicação com a rede.

### 3. Visão por beneficiário

Ajuda a identificar padrões de utilização e eventuais inconsistências cadastrais. Atenção à LGPD: dados de saúde são dados pessoais sensíveis; o acesso deve ser restrito por perfil e finalidade, e **nenhum dado individual deve aparecer em materiais de comunicação**.

### 4. Visão por motivo

Classificar glosas por motivo (cobertura, documentação, autorização, duplicidade, valor etc.) mostra se o problema é de processo ou de comportamento. A taxonomia de motivos utilizada pelo mercado e pela ANS deve ser conferida: **[VERIFICAR NA FONTE]**.

### 5. Visão de contestação e desfecho

Quanto foi contestado, quanto foi revertido, quanto tempo levou? Essa visão mostra se a glosa é bem fundamentada e se o processo de recurso funciona. No intercâmbio, a contestação ganha uma dimensão adicional entre operadoras.

## Outliers: o olhar estatístico para o que foge do padrão

Além do acompanhamento por visão, a análise de **outliers** procura eventos ou entidades que se afastam do comportamento típico: um prestador com taxa de glosa muito acima de pares comparáveis, um procedimento cobrado com frequência incomum, um valor fora da faixa. Outlier não significa irregularidade; significa que vale investigar. Essa abordagem se relaciona com a detecção de anomalias discutida em [Machine learning na saúde suplementar](/blog/12-machine-learning-saude-suplementar).

## Como a plataforma apoia a gestão de glosas

A NeoHealth BI · OPS inclui um grupo "Gestão de Glosas" e telas relacionadas em outros módulos. Segundo o inventário dos tutoriais (gravados em base de demonstração com dados fictícios, "Operadora Modelo"):

| Tela | Para que serve | Status |
|---|---|---|
| Gestão Assistencial › Gestão de Glosas › Por Prestador | Glosas por prestador | [DISPONÍVEL] |
| … › Por Procedimento | Glosas por procedimento | [DISPONÍVEL] |
| … › Por Beneficiário | Glosas por beneficiário | [DISPONÍVEL] |
| … › Dashboards | Painéis de acompanhamento | [DISPONÍVEL] |
| … › Outliers | Identificação de pontos fora do padrão | [DISPONÍVEL] |
| Gestão de Glosas › Glosas de Contas Médicas › Sugestão de Glosas na Rede | Sugestões de glosa para análise | [DISPONÍVEL] (método e critérios da sugestão: [A CONFIRMAR]) |
| Gestão de Autorizações › Glosas e Ocorrências | Glosas e ocorrências ligadas a requisições | [DISPONÍVEL] |
| Gestão de Autorizações › Glosa do Autorizado | Glosa sobre o que foi autorizado | [DISPONÍVEL] |
| Intercâmbio › Glosas e Contestação (A550) | Glosas e contestação em intercâmbio PTU | [DISPONÍVEL] |
| Sala de Situação ANS › Glosa × Painel ANS | Comparativo com o painel da ANS | [DISPONÍVEL] (escopo da comparação: [A CONFIRMAR]) |

A "Sugestão de Glosas na Rede" é apresentada como apoio à análise. **A decisão de glosar permanece com a operadora**, seguindo seu contrato, suas regras e a regulamentação aplicável. Não afirmamos que a sugestão seja automática, precisa ou que reduza custos.

## Um fluxo de gestão de glosas orientado por dados

### Etapa 1 — Padronize os dados

Garanta consistência entre tabelas, códigos e cadastros. Sem isso, as taxas de glosa não são comparáveis. A base de dados integrada ao ERP (a plataforma descreve integração com Oracle e ERP Philips Tasy) é a fundação; veja [Como estruturar BI em operadoras](/blog/01-como-estruturar-bi-operadoras).

### Etapa 2 — Defina indicadores

Sugestão inicial: valor glosado e proporção sobre o valor apresentado, glosa por motivo, glosa por prestador, taxa de contestação e taxa de reversão, tempo de tratamento. A escolha final e as fórmulas devem ser alinhadas às definições da operadora e, quando aplicável, às da ANS: **[VERIFICAR NA FONTE]**. Para o panorama geral, consulte [Indicadores fundamentais](/blog/02-indicadores-fundamentais-operadoras).

### Etapa 3 — Priorize pelo impacto

Nem toda glosa merece o mesmo esforço. Priorize combinações de prestador, procedimento e motivo com maior valor ou recorrência.

### Etapa 4 — Feche o ciclo com a rede

Compartilhe com os prestadores informações claras sobre motivos e regras. Parte relevante das glosas recorrentes decorre de desencontro de informação, não de má-fé. Um diálogo baseado em dados reduz disputas improdutivas.

### Etapa 5 — Retroalimente a autorização

Se um procedimento é frequentemente glosado depois, talvez a regra deva ser comunicada ou tratada na autorização. A integração entre autorização e contas médicas é um dos pontos de maior ganho de visibilidade.

### Etapa 6 — Conecte ao resultado

Glosas influenciam a [sinistralidade](/blog/03-acompanhar-sinistralidade) e o resultado financeiro (ver [gestão financeira](/blog/04-gestao-financeira-saude-suplementar)). A plataforma dá visibilidade a esse efeito; **não garante** redução de sinistralidade ou economia. Há oportunidades que a inteligência pode ajudar a administrar, mas elas dependem de decisões e processos da operadora.

## Riscos e boas práticas

- **Fundamentação:** toda glosa precisa de motivo claro e rastreável.
- **Equilíbrio:** glosa excessiva ou mal fundamentada desgasta a rede e pode gerar judicialização.
- **Auditoria de regras:** revise periodicamente as regras automáticas de glosa.
- **Governança:** mantenha trilha de quem alterou regras e decisões, em linha com práticas de controles internos discutidas em [RN 518](/blog/07-rn-518-governanca-operadoras).
- **Atendimento:** divergências de cobrança podem refletir em demandas de beneficiários; veja [RN 623](/blog/08-rn-623-atendimento-beneficiarios).
- **LGPD:** limite o acesso a dados individuais; não publique dados de saúde.

## Perguntas frequentes

**Qual é uma taxa de glosa saudável?**
Não existe número único aplicável a todas as operadoras. Compare a sua série histórica e pares comparáveis. Para referências de mercado, consulte o painel da ANS: **[VERIFICAR NA FONTE]**.

**A plataforma glosa automaticamente?**
Não afirmamos isso. A plataforma oferece telas de análise e sugestão para apoio; as regras e a decisão são da operadora. Capacidade de automação por cliente: **[A CONFIRMAR]**.

**A ANS publica dados de glosa?**
Sim, a ANS disponibiliza um Painel de Indicadores de Glosa com dados do TISS (ver referências). Detalhes e atualização: **[VERIFICAR NA FONTE]**.

**Os números nas telas são reais?**
Não. Os exemplos usam dados fictícios da base "Operadora Modelo".

## Próximos passos

Se a sua operadora quer enxergar glosas por prestador, procedimento, beneficiário e outliers em um mesmo ambiente, conheça a [página da NeoHealth BI · OPS](/neohealth-bi-ops) [A CONFIRMAR: URL final da landing page].

**Solicite uma demonstração.**

*Conheça o potencial dos dados da sua operadora.*

## Leituras relacionadas

- [Gestão de prestadores](/blog/09-gestao-prestadores-operadoras)
- [Como acompanhar a sinistralidade](/blog/03-acompanhar-sinistralidade)
- [Indicadores assistenciais](/blog/05-indicadores-assistenciais)
- [Inteligência artificial na saúde suplementar](/blog/11-inteligencia-artificial-saude-suplementar)
- [Machine learning na saúde suplementar](/blog/12-machine-learning-saude-suplementar)

## Referências oficiais

| Fonte | URL | Data de consulta | Observação |
|---|---|---|---|
| ANS — Dados Abertos: novo conjunto sobre indicadores de glosa | https://www.gov.br/ans/pt-br/assuntos/noticias/operadoras/dados-abertos-ans-lanca-novo-conjunto-sobre-indicadores-de-glosa | 01/11/2026 | Localizado em busca; conteúdo resumido a partir do resultado, página não aberta integralmente |
| ANS — Painel de Indicadores de Glosa | http://www.ans.gov.br/perfil-do-setor/dados-e-indicadores-do-setor/painel-de-indicadores-de-glosa | 01/11/2026 | Localizado em busca |
| Portal de Dados Abertos — Painel de indicadores de Glosa | https://dados.gov.br/dados/conjuntos-dados/painel-de-indicadores-de-glosa | 01/11/2026 | Localizado em busca |
| ANS — Padrão TISS, componente organizacional (versão de setembro/2025) | https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/PadroTISS_ComponenteOrganizacional_202509.pdf | 01/11/2026 | Localizado em busca; versão vigente **[VERIFICAR NA FONTE]** |

---

**Funcionalidades citadas e status:** Gestão de Glosas (Por Prestador, Por Procedimento, Por Beneficiário, Dashboards, Outliers) [DISPONÍVEL]; Sugestão de Glosas na Rede [DISPONÍVEL; método: A CONFIRMAR]; Glosas em Autorizações e Intercâmbio (A550) [DISPONÍVEL]; Glosa × Painel ANS [DISPONÍVEL]; integração Oracle/Tasy [DISPONÍVEL].

**Nota de imagens:** capa real sugerida `ass-35.jpg` ou `ass-19`-equivalente disponível em assets_reais, com a nota "Imagem da plataforma com dados fictícios (base de demonstração)".

**LGPD / comunicação:** consentimento explícito e opt-out no formulário; sem dados pessoais de saúde.
