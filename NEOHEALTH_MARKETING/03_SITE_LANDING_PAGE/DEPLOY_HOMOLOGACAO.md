# Guia de deploy em homologação (apenas instruções — NÃO executado)
Objetivo: hospedar a landing page em ambiente de **staging**, restrito e sem indexação. Nenhuma publicação foi feita; execute somente com aprovação (ver `15_RELATORIOS/pendencias_e_aprovacoes.md`).

## Opção A — GitHub Pages em branch separada (exemplo)
1. Confirmar com o proprietário se o repositório pode ser público: GitHub Pages em repositório gratuito exige repositório público. Se o conteúdo não puder ser público, use a opção B.
2. Criar branch de homologação contendo só o site: `git checkout --orphan homolog-site` e copiar o conteúdo de `03_SITE_LANDING_PAGE/` (sem `qa/` e sem `*.md`) para a raiz.
3. `git add . && git commit -m "Homologação landing NeoHealth BI" && git push origin homolog-site`.
4. Em Settings > Pages: Source = branch `homolog-site`, pasta `/ (root)`.
5. Manter `<meta name="robots" content="noindex,nofollow">` e `robots.txt` com `Disallow: /`.
6. Validar URL de staging com o roteiro de QA; **não** configurar domínio definitivo nem DNS.
## Opção B — staging com acesso restrito
Servidor interno, Netlify/Cloudflare Pages com proteção por senha ou Basic Auth. Mesma estrutura de arquivos.
## Antes de ir para produção (somente com aprovação)
- Preencher `NH_CONFIG.formEndpoint` (CRM/automação aprovado) e `schedulerUrl`; revisar CORS e política de privacidade com o jurídico.
- Trocar domínio em canonical, og:url, og:image, JSON-LD, sitemap e robots; trocar `noindex` por `index,follow`.
- Inserir GTM/GA4 apenas após banner de consentimento.
- Substituir o logotipo provisório pelo original; otimizar imagens; reexecutar `qa/qa_playwright.js`.
- Teste local rápido: `cd 03_SITE_LANDING_PAGE && python3 -m http.server 8080`.
