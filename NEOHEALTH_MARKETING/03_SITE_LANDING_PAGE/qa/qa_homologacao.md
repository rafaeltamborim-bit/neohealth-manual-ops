# QA de homologação — Landing Page NeoHealth BI · OPS
Data: 01/11/2026 · Ambiente: **local** (servidor HTTP efêmero em 127.0.0.1) · Chromium via Playwright 1.63 (`chromium.launch()`) · **Nada foi publicado.**
Reproduzir: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node qa/qa_playwright.js` (saída em `qa/saida_console.txt`, `qa/resultado.json`).

## Resultado: 23 de 23 verificações aprovadas
| Verificação | 375 | 768 | 1440 |
|---|---|---|---|
| Sem overflow horizontal (scrollWidth = clientWidth) | OK | OK | OK |
| 15 seções, 1 H1, todas as imagens com alt, nenhuma imagem quebrada | OK | OK | OK |
| Sem erros de console/JS | OK | OK | OK |
| Menu mobile abre | OK | n/a | n/a |
Verificações funcionais (1440): UTM/gclid/li_fat_id nos campos ocultos; dataLayer (lp_view, section_view, scroll_depth, faq_open, schedule_view); links internos (11 únicos) resolvem (âncoras e páginas); formulário vazio gera 8 erros; e-mail pessoal (gmail) rejeitado; consentimento obrigatório; honeypot bloqueia envio; envio válido sem endpoint leva a `obrigado.html?modo=homologacao`; política carrega; JSON-LD Organization e FAQPage parseiam.
Privacidade do teste: nenhuma requisição externa e nenhum POST/PUT; `formEndpoint` vazio = nenhum dado é enviado.

## Capturas (em `qa/`)
`landing-375-dobra.png`, `landing-375-full.png`, `landing-768-dobra.png`, `landing-768-full.png`, `landing-1440-dobra.png`, `landing-1440-full.png`, `obrigado-1440.png`, `politica-1440.png`.

## Limitações / não verificado
- Roboto Condensed não está instalada no ambiente de teste nem é carregada pelo site; as capturas mostram o fallback (Arial). Conferir visualmente com a fonte oficial (pendência).
- Logotipo é recorte provisório de capa real (baixa resolução em telas de alta densidade).
- Acessibilidade: não foi rodado axe/Lighthouse; contraste de botão (#060A15 sobre #4190D3) e demais itens devem ser medidos. Navegação por teclado e foco visível implementados mas só testados parcialmente.
- Testado apenas em Chromium; Firefox/Safari e dispositivos reais pendentes.
- Tags GTM/GA4 não existem (sem IDs); eventos dataLayer foram verificados só na página. Validação do JSON-LD em ferramenta externa (Rich Results Test) pendente.
- Desempenho: 29 JPGs de 1920×1080 (~6,7 MB no total) com lazy-loading; recomenda-se gerar versões WebP/menores antes da produção.
- Página `obrigado` e política: apenas conferidas visualmente/carregamento.
