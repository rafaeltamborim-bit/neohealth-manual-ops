# Manual de Identidade Visual — NeoHealth BI · OPS
Versão 1.0 · 01/11/2026 · Derivado das capas reais (`08_CRIATIVOS/assets_reais/`) e da `00_FICHA_DE_FATOS.md`. Versão navegável: `manual.html`. Tokens: `tokens.css` / `tokens.json`.

Marca: **"Transforme dados em decisões. Decisões em resultados."**
Posicionamento: plataforma especializada em inteligência estratégica para operadoras de planos de saúde (não "mais um BI de dashboards").

## 1. Princípios
Minimalista, tecnológico, institucional. Fundo azul-marinho escuro, destaque em azul e ciano, muito espaço em branco (escuro), tipografia condensada. Sem fotos genéricas de médicos; sem telas fictícias — somente capas/telas reais da plataforma.

## 2. Paleta (hex amostrados das capas reais)
| Token | Hex | Origem | Uso |
|---|---|---|---|
| bg-900 | #060A15 | fundo das capas (amostra #070B16) | fundo base |
| bg-800 | #0F172A | brief | superfícies/cartões |
| bg-700 | #16213A | [A CONFIRMAR] derivado | cartões elevados |
| blue | #4190D3 | ícone do logotipo | botões, links, elementos de dados |
| cyan | #5FBEEC | "BI" do logotipo | títulos de destaque, links |
| mint | #A9EFE5 | ficha de fatos | destaque pontual, numeração, tags |
| mint-soft | #C4F1EE | etiquetas das capas | texto de tag |
| white | #FFFFFF | títulos nas capas | títulos e corpo sobre escuro |
| gray-400 | #98A5B6 | "OPS" do logotipo | texto secundário |
| gray-300 | #95A4B9 | subtítulos das capas | legendas |
Cores de estado (ok #2DD4BF, alerta #F5B942, erro #F87171) são **[A CONFIRMAR]**: não aparecem como identidade nas capas.
Contraste: branco sobre #060A15 e cyan #5FBEEC sobre #060A15 passam AA para texto normal; gray-400 sobre bg-900 é para texto ≥ 14px. Botão primário: fundo #4190D3 com texto #060A15 (verificar AA na homologação) — ver QA.

## 3. Tipografia
Família da marca: **Roboto Condensed** (400 e 700). Fallback: `"Arial Narrow", Arial, "Helvetica Neue", sans-serif`. Observação: as capas reais usam uma sans geométrica nos títulos; seguimos o brief (Roboto Condensed) e registramos a divergência em Pendências (confirmar fonte oficial).
Escala: display clamp(2.4–4rem) · H1 clamp(2–3rem) · H2 clamp(1.6–2.25rem) · H3 1.25rem · corpo 1.0625rem/1.6 · legenda 0.875rem. Títulos em 700, entrelinha 1.12. Sem caixa-alta contínua em frases; sentence case.
A landing page referencia a fonte por `font-family` com fallback e, **se a fonte não estiver instalada, cai no fallback** (sem baixar de terceiros, por LGPD/performance; incorporar arquivo local é pendência de licença/hospedagem).

## 4. Logotipo
- O logotipo é o que aparece nas capas reais: ícone de pixels/barras em azul (#4190D3) + "NeoHealth" em branco + "– BI" em ciano (#5FBEEC) + "OPS" em cinza (#98A5B6). **Não redesenhar, recolorir livremente, redistribuir ou recriar em SVG.**
- Não existe arquivo original de logotipo no repositório. Foi extraído apenas um **recorte provisório** de uma capa real (`referencias/logo-recorte-capa-PROVISORIO.png`, 400×72 px) para uso interno/homologação. Para produção: **[PENDÊNCIA P-01] solicitar SVG/PNG originais ao proprietário.**
- Versão escura (principal): sobre #060A15 / #0F172A, como nas capas.
- Versão clara: **[PENDENTE]** — não existe nas capas; não criar. Sobre fundos claros, usar a versão a ser fornecida pelo proprietário.
- Área de proteção: margem mínima = 50% da altura do ícone em todos os lados; nada (texto, borda, imagem) dentro dela.
- Tamanho mínimo: 120 px de largura em tela (recorte provisório: não ampliar além de 100%; fica serrilhado).
- Proibido: esticar, girar, aplicar sombra/brilho, trocar cores, colocar sobre fundo de baixo contraste, fotos ocupadas, reescrever o nome em outra fonte.

## 5. Grid e layout
Container 1200 px, 12 colunas, calha 24 px, base de espaçamento 8 px. Breakpoints de teste: 375 / 768 / 1440 px. Mobile: 1 coluna; tablet: 2; desktop: 3–4 (ou 12 colunas em seções com texto + imagem). Seções com padding vertical 64–96 px. Raios 12 px (cartões) e 999 px (tags/pílulas). Bordas 1 px rgba(95,190,236,.22).

## 6. Screenshots reais e nota de dados fictícios
- Usar **somente** as capas JPG 1920×1080 reais (`08_CRIATIVOS/assets_reais/`). Não montar mockups, não editar números, não cortar a ponto de remover o contexto, não sobrepor dados inventados.
- **Toda imagem com tela** leva a legenda: "Imagem da plataforma com dados fictícios (base de demonstração)." (fonte ≥ 12 px em peças digitais; em vídeo, ≥ 3 s visível).
- Cantos 12 px, borda 1 px, sombra suave; proporção 16:9 preservada. Alt text descreve o módulo (ex.: "Cockpit Executivo da plataforma NeoHealth BI com dados fictícios") e nunca cita valores como resultado.
- Não vender quantidade de telas.

## 7. Tom de voz
Consultivo, claro, técnico sem jargão desnecessário, especializado em operadoras. Verbos: ajuda a identificar, apoia, dá visibilidade a, permite acompanhar, antecipar cenários. Português do Brasil, sentence case, frases curtas, "sua operadora".
Nunca: garantir redução de sinistralidade/economia; prometer resultado; "o melhor", "líder", "único" sem evidência; citar clientes, depoimentos, certificações ou números de mercado; afirmar normas ANS sem fonte oficial (gov.br/ans) — usar [VERIFICAR NA FONTE].
CTA principal: "Solicite uma demonstração." · Secundário: "Conheça o potencial dos dados da sua operadora."

## 8. Do / Don't
| Faça | Não faça |
|---|---|
| Fundo escuro #060A15/#0F172A e destaque ciano/azul | Fundos claros chapados sem versão clara do logo |
| Usar capas reais com a nota de dados fictícios | Telas inventadas, mockups, médicos de banco de imagem |
| "Ajuda a identificar oportunidades" | "Reduza sinistralidade em X%" |
| Falar de módulos (financeiro, sinistralidade…) | Falar de "170 telas" como argumento de venda |
| Marcar [A CONFIRMAR] o que não está na ficha | Citar integrações, clientes ou prêmios não confirmados |
| Legendas ≥ 12 px, contraste AA | Texto cinza pequeno sobre imagem |

## 9. Especificações por canal
Medidas são referências de mercado a **validar na plataforma de cada canal no momento da produção** [VERIFICAR NA FONTE]; não foram conferidas automaticamente.
| Canal | Formatos de imagem | Texto/uso | Notas |
|---|---|---|---|
| LinkedIn | Imagem única 1200×627 (1.91:1) e 1080×1080 (1:1); carrossel 1080×1080/1080×1350; vídeo 16:9 ou 1:1 | Título curto; texto principal conciso, CTA claro | Capa 1920×1080 recortada com margem de segurança de 8%; logo no canto superior esquerdo |
| Google Ads | Display responsivo: 1200×628 (1.91:1), 1200×1200 (1:1), logo 1200×1200 e 1200×300 (4:1) | Títulos ≤ 30 car., descrições ≤ 90 car. (RSA) | Logo: **exige arquivo original** (P-01); sem texto sobreposto excessivo |
| Meta (Facebook/Instagram) | Feed 1080×1080 / 1080×1350 (4:5); Stories/Reels 1080×1920 (9:16) | Texto principal curto; evitar mais de 20% da imagem em texto | Zona segura de 14% superior/inferior em 9:16 |
| YouTube | Miniatura 1280×720 (16:9), vídeo 1920×1080; banner do canal 2560×1440 (zona segura 1546×423) | Títulos ≤ 60 car.; nota de dados fictícios visível ao mostrar telas | Capas reais 1920×1080 servem de base de miniatura com título grande |
| E-mail | Largura 600 px (retina 1200 px); peso total < 100 KB por imagem; texto alternativo obrigatório | Assunto ≤ 50 car.; botão ≥ 44×44 px; rodapé com opt-out e identificação do remetente (LGPD) | Fundo escuro pode inverter em clientes de e-mail: testar; fallback de cor de fundo `bgcolor` |

## Pendências
- **P-01** Logotipo original (SVG/PNG, versão escura e clara, favicon) — não existe no repositório; recorte provisório de capa.
- **P-02** Confirmar a fonte oficial (capas parecem usar sans geométrica; brief define Roboto Condensed) e licença/arquivos de fonte para hospedagem local.
- **P-03** Confirmar cores de estado (ok/alerta/erro) e bg-700.
- **P-04** Versão clara do logotipo e regras de uso em fundo claro.
- **P-05** Validar especificações dos canais nas plataformas no momento da produção [VERIFICAR NA FONTE].
