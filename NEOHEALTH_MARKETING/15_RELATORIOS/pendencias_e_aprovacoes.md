# Relatório de pendências e aprovações — NeoHealth BI · OPS
Data-base: 01/11/2026 · Status geral: **preparado, aguardando aprovações. Nada foi publicado, disparado, contratado ou gasto.**
Detalhes por pasta: arquivos `PENDENCIAS*.md` em cada diretório.

## 1. Aprovações necessárias do proprietário (bloqueiam execução)
| # | Aprovação | Destrava |
|---|---|---|
| A1 | Aprovar estratégia, posicionamento, personas e mensagens (01_ESTRATEGIA) | Todo o restante |
| A2 | Escolher cenário de verba (R$ 3.000 / 5.000 / 10.000) e autorizar gasto | Campanhas Google, Meta e LinkedIn |
| A3 | Criar/autorizar contas de anúncio e faturamento (Google, Meta, LinkedIn) | Importar CSVs, publicar campanhas |
| A4 | Aprovar landing page e autorizar publicação (homologação → produção) | Tráfego pago, SEO |
| A5 | Aprovar publicações do LinkedIn (60 peças), calendário e perfil do fundador | Publicação orgânica |
| A6 | Aprovar artigos SEO (12) após revisão regulatória e jurídica | Publicação no site |
| A7 | Aprovar criativos (55 peças) e roteiros de vídeo (10); autorizar locutor, trilha e produção | Anúncios e canal YouTube |
| A8 | Autorizar publicação dos 223 tutoriais reais no canal YouTube | Playlists |
| A9 | Autorizar qualquer envio de e-mail/WhatsApp e escolher o CRM/ferramenta | Sequência de nutrição |
| A10 | Aprovar uso do nome "Philips Tasy" em anúncios e site (marca de terceiro) | Campanha de Tasy |

## 2. Informações que só o proprietário pode confirmar [A CONFIRMAR]
1. Status real de: machine learning (quais modelos), detecção de anomalias, chat inteligente, alertas por WhatsApp/e-mail, aplicativo mobile, instalação on-premise, integração Tasy/Oracle e atualização do espelho DuckDB. Hoje só o que tem tutorial/captura consta como DISPONÍVEL.
2. Confirmar que a base "Operadora Modelo" não contém dado real.
3. Logotipo oficial (SVG/PNG, claro/escuro, favicon) e licença da fonte (as capas parecem usar sans geométrica, não Roboto Condensed).
4. Razão social, CNPJ, domínio, e-mail do encarregado (LGPD), contato comercial.
5. Modelo comercial e preços (proposta está com [A DEFINIR]); duração da demonstração; formato de piloto.
6. Dados do fundador para bio, cargo, formação e foto; metas de CAC/ROI; critério de lead qualificado.
7. Concorrentes como palavra-chave no Google (recomendado não usar).

## 3. Verificações obrigatórias em fonte oficial [VERIFICAR NA FONTE]
- **Limitação do ambiente:** gov.br/ans, planalto.gov.br e páginas de políticas das plataformas não puderam ser abertas; só resumos de busca. Apenas a RN 505/2022 (IDSS) foi confirmada na página oficial.
- Revisar RN 518, RN 623 (vigência, alterações), IDSS (pesos/fórmulas por ano-base), TISS, ressarcimento ao SUS e LGPD antes de publicar os artigos 03, 06, 07, 08, 11, 12 e posts INS09, INS14, INS19, TEC07.
- Políticas de anúncios (Google, Meta, LinkedIn) para saúde e limites de caracteres; preços de BI genérico citados na matriz de concorrência (não citar externamente).
- Pesquisa de palavras-chave: volumes, CPCs e anunciantes não foram obtidos; validar no Planejador de Palavras-chave.

## 4. Pendências técnicas
- Endpoint real do formulário (hoje vazio, nada é enviado); URL de agendamento (Calendly/Cal.com); GTM/GA4, Pixel/CAPI Meta, Insight Tag LinkedIn e banner de consentimento (Consent Mode).
- Política de privacidade da landing é **modelo** para revisão jurídica.
- [FEITO] Imagens da landing otimizadas (6,7 MB → 2,9 MB, 1600 px, JPEG q80).
- Instalar Roboto Condensed na máquina de exportação (PNGs atuais usam fallback); exportar artes 1:1, 4:5, 9:16 e vídeos; só 5 de 10 thumbnails YouTube criadas (as demais usam capas CAP-01..05).
- Substituir `DOMINIO-A-CONFIRMAR` nos CSVs do Google Ads antes de importar; criar lista compartilhada de negativas.
- Substituir o logotipo provisório (recorte de capa) em landing e criativos.
- Slugs de blog `/blog/{slug}` e âncora `/#pilar` a confirmar com a estrutura final do site.
- Feriados (15/11, 20/11, 25/12, 01/01) não descontados no cronograma/calendário.
- E-book tem ~13 páginas (pedido 12–16): ampliar capítulos 4 e 7 se desejado.

## 5. Riscos de compliance monitorados
Linguagem sem garantia de resultado (varredura feita: sem ocorrências afirmativas); nota "dados fictícios" em toda peça com tela; sem clientes/depoimentos/certificações; LGPD (consentimento, opt-out, sem dado de saúde pessoal); Meta/Google restringem segmentação por atributos de saúde.

## 6. Atualização 01/11/2026 — decisões do proprietário
- Verba definida: **R$ 1.000/mês** (ver 01_ESTRATEGIA/05b_orcamento_1000.md). Falta ajustar os orçamentos de Google (05) e Meta (06) escritos para R$ 1.200/R$ 600.
- Funcionalidades da seção A da ficha autorizadas como [DISPONÍVEL] (ficha, seção E). Falta revisar as peças que ainda mostram [A CONFIRMAR] para esses itens.
- Domínio https://neohealth.com.br/ e logotipo: **site inacessível pelo ambiente** (host bloqueado na política de rede). Para liberar: menu do ambiente na barra de título da sessão > Edit > Network access, adicionando neohealth.com.br em Allowed domains. Alternativa: enviar o logotipo (SVG/PNG) ao repositório.
- Continuam sem decisão: contas de anúncio, faturamento, publicação da landing, endpoint do formulário, GTM/GA4, revisão jurídica, uso da marca Philips Tasy.
