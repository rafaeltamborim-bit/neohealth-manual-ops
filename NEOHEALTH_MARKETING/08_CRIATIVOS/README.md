# 08_CRIATIVOS

Peças editáveis em HTML/CSS (um arquivo por peça), exportáveis para PNG.

- `assets_reais/`: 28 capas reais 1920×1080 (dados fictícios, base "Operadora Modelo"). **Não alterar.** As peças só as recortam por CSS (`.shot`, variáveis `--rx/--ry/--rw/--rh`).
- `pecas/`: banners_institucionais (10), anuncios_comerciais (10), carrosseis (5, 31 slides), infograficos (5, só conceitos, sem números), capas_video (5), thumbnails_youtube (5, 1280×720), stories (10, 1080×1920), remarketing (5). Total 55 arquivos.
- `catalogo_criativos.csv`: ID, formato, tamanho, texto, CTA, asset, canal, status (+ funcionalidades e arquivo).
- `gerar_pecas.py`: regenera HTML e catálogo a partir dos dados (textos/IDs no próprio script). Opcional; os HTML também podem ser editados à mão.
- `render.py`: `python3 render.py [filtro]` exporta PNGs em `exportados/` (81 PNGs; carrosséis = 1 PNG por slide). Usa Playwright com `chromium.launch()`.
- `PENDENCIAS.md`.

Regras: toda peça com tela traz a nota "Imagem da plataforma com dados fictícios (base de demonstração)". Sem promessas de resultado. Nada é publicado sem aprovação.
Fonte: Roboto Condensed com fallbacks (Arial Narrow, Carlito, Inter). Instale Roboto Condensed na máquina de exportação para fidelidade final.
