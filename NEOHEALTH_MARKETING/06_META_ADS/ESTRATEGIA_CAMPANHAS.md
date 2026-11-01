# Estratégia Meta Ads — cenário R$ 600/mês (≈ R$ 19,7/dia)
Nada publicado nem gasto. Público B2B pequeno e nichado: Meta é **suporte de reconhecimento e remarketing**, não o canal principal de demanda (Google Pesquisa e LinkedIn são mais aderentes a cargo/empresa). Todas as faixas numéricas abaixo são hipóteses a validar com os dados reais.

## Estrutura (5 campanhas)
| # | Campanha | Objetivo Meta | R$/mês | Conceitos | Observação |
|---|---|---|---|---|---|
| 1 | Reconhecimento | Reconhecimento/Alcance | 150 | C01, C10 | Frequência ≤ 2/semana |
| 2 | Institucional | Tráfego (visitas à LP institucional) / Engajamento | 100 | C01, C10 (variações) | Pode unir à 1 se o público for pequeno |
| 3 | Vídeos demonstrativos | Visualizações de vídeo (ThruPlay, 15 s a 60 s) | 150 | C04, C05, C09 | Vídeos de `07_YOUTUBE`/tutoriais com cortes e nota fictícia; públicos de vídeo alimentam remarketing |
| 4 | Remarketing | Leads/Vendas (conversão no site) | 90 | C07, C08 | Visitantes da LP 30-90 dias + 50% de vídeo; **só se o público tiver tamanho mínimo** |
| 5 | Conversão LP | Leads (evento `generate_lead_demo` via Pixel/CAPI) | 110 | C02, C03, C06 | Iniciar com Tráfego/Visualização de LP até o Pixel acumular eventos |
Soma: R$ 600. Se o remarketing tiver audiência < mínimo, mover o saldo para a 5.

## Públicos
- **Frio (interesses/cargos):** cargos como diretor, gerente, superintendente, coordenador em áreas financeira, atuarial, médica/técnica, TI; setor "saúde" por empresa/cargo e interesses profissionais amplos (ex.: gestão em saúde, saúde suplementar, administração hospitalar). **Disponibilidade de opções detalhadas varia; validar no Gerenciador.** Não segmentar por condição de saúde.
- **Lookalike:** SOMENTE a partir de listas próprias com **consentimento documentado** (base legal LGPD, finalidade de publicidade, opt-out). Se a lista (clientes/leads) tiver < ~100 pessoas combináveis, o lookalike fica fraco [HIPÓTESE]. Nenhuma lista foi fornecida; **não subir listas** sem aprovação do DPO e termos da Meta (Públicos Personalizados) aceitos.
- **Remarketing:** visitantes do site (Pixel/CAPI com consentimento de cookies), engajamento Instagram/Facebook, visualizadores de vídeo. Janelas 30/60/90 dias.
- **Exclusões:** leads já convertidos, funcionários, públicos de remarketing nas campanhas frias.
- Local: Brasil (praças com operadoras, refinar depois). Idade ≥ 25. Sem segmentação por atributos pessoais.

## Posicionamentos
Feed Instagram e Facebook, Stories, Reels (vídeos 9:16) e Reels do Facebook. Desligar Audience Network e Mensagens (Messenger inbox) no início. Revisar "Vantagem+ posicionamentos" depois de 7 dias com dados.

## Formulário nativo x Landing page
| | Formulário nativo (Instant Form) | Landing page |
|---|---|---|
| Volume | Maior, menos atrito | Menor |
| Qualidade | Menor (e-mail pessoal, cliques acidentais) | Maior (intenção, explicação do produto) |
| Medição | Pixel/CAPI fraca; dado fica na Meta | UTM + gclid/fbclid + CRM |
| LGPD | Política/aviso dentro do formulário | Controle total de consentimento |
**Decisão proposta:** landing page como padrão (B2B, ticket alto, qualidade > volume). Teste opcional de Instant Form de "Mais volume" com **perguntas de qualificação** (cargo, tipo de operadora, e-mail corporativo obrigatório, nº de beneficiários em faixas) e passos de revisão; comparar custo por lead **qualificado**, não por lead. UTM: `utm_source=meta&utm_medium=paid_social&utm_campaign=<campanha>&utm_content=<conceito>&utm_term={{adset.name}}` (macros dinâmicas da Meta: `{{campaign.name}}`, `{{ad.name}}`). LP: `https://DOMINIO-A-CONFIRMAR/lp/...` [A CONFIRMAR].

## Orçamento e leitura
R$ 600 permite poucos testes. Rodar 2 conceitos por conjunto, ~2 semanas antes de trocar; não editar a cada dia. Fase de aprendizado exige volume que este orçamento pode não atingir: aceitar e priorizar otimizar por evento mais alto do funil possível (ThruPlay/Visualização de LP → lead). Métricas: alcance, frequência, ThruPlay, CTR link, custo por visita, custo por lead, **custo por lead qualificado**, taxa de leads descartados.
