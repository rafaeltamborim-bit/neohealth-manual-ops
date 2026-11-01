# Guia: configurar o Google Ads (CSVs regerados em 01/11/2026)
Domínio: https://neohealth.com.br · Verba: R$ 400/mês para operadoras + R$ 400/mês para hospitais no Google (R$ 100 + R$ 100 de remarketing no Meta). **Nada foi importado, publicado ou gasto.**

## Campanhas regeradas (todas importam PAUSADAS)
| # | Campanha | Público | R$/mês | Status |
|---|---|---|---|---|
| 1 | Operadoras: inteligência de dados e decisão | Operadoras | 200 | Ativar primeiro |
| 2 | Operadoras: qualquer ERP | Operadoras | 200 | Ativar primeiro |
| 3 | Operadoras: sinistralidade | Operadoras | — | Fase 2 (orçamento "A DEFINIR") |
| 4 | Operadoras: inteligência regulatória ANS | Operadoras | — | Fase 2 |
| 5 | Hospitais: inteligência de dados e decisão | Hospitais | 200 | Ativar após levantamento de funcionalidades |
| 6 | Hospitais: qualquer ERP | Hospitais | 200 | Idem |
Mudanças: sem "BI para Tasy" (Tasy virou só palavra-chave de cauda), copy de inteligência de decisão sem comparativos nem "dashboard", hospitais adicionados (negativas de hospital removidas só neles), RSAs conferidos (títulos ≤30, descrições ≤90). Relatório: `csv_editor/VERIFICACAO_CARACTERES.md`.

## O que você precisa fazer
1. **Conta**: ads.google.com → modo especialista; moeda BRL, fuso Brasília; formas de pagamento.
2. **Medição**: GA4 + Google Tag Manager na landing; conversões `generate_lead_demo` (formulário) e clique em agendar (ver `PLANO_MEDICAO_CONVERSOES.md`); consentimento de cookies.
3. **Landing**: publicar as páginas de destino. As URLs nos CSVs usam `https://neohealth.com.br/lp/<slug>` (operadoras, operadoras-erp, hospitais, hospitais-erp, gestao-sinistralidade, inteligencia-regulatoria-ans, demonstracao…). **Essas páginas ainda não existem** (a landing atual é única e de operadoras). Publicar ou ajustar as URLs antes de ativar. Política de privacidade revisada pelo jurídico.
4. **Google Ads Editor** (gratuito): entrar na conta → Conta > Importar > Do arquivo. Ordem: campanhas, grupos, palavras, negativas, rsa, sitelinks, callouts, snippets. Preencha o orçamento diário das campanhas 3 e 4 (hoje "A DEFINIR (fase 2)") ou remova-as do arquivo.
5. **Lista compartilhada de negativas**: criar manualmente em Biblioteca compartilhada com `csv_editor/lista_compartilhada_negativas.csv` e aplicar às campanhas de operadoras.
6. **Revisar e publicar** no Editor; **ativar** só as campanhas 1 e 2 (hospitais após validar o conteúdo).
7. **Rotina**: conferir termos de pesquisa semanalmente e adicionar negativas; pausar campanha que gaste ~R$ 100 sem conversão; validar volumes/CPC no Planejador de Palavras-chave (não obtive esses dados).

## Cuidados
- Marca "Philips Tasy" só como palavra-chave, sem sugerir parceria; revisar política de marcas registradas do Google se usar em texto de anúncio.
- Callouts "Instalação on-premise" e "Auditoria e acesso" estão disponíveis conforme a ficha; manter só se o proprietário quiser divulgar.
- Hospitais: copy genérica (inteligência de dados e decisão, qualquer ERP) porque módulos hospitalares ainda não foram confirmados.
- Documentos antigos desta pasta (`ESTRATEGIA_LANCES_ORCAMENTO.md`, `PESQUISA_INTENCAO_SERP.md`, `PLANO_MEDICAO_CONVERSOES.md`) foram escritos antes do reposicionamento: valores e nomes de campanha estão defasados.

## Importação em um único arquivo (atualização)
`csv_editor/IMPORTACAO_UNICA.csv` reúne campanhas, grupos, palavras, negativas, anúncios, sitelinks, callouts e snippets das 4 campanhas prontas (todas Paused, orçamentos numéricos). Dois jeitos:
- **Google Ads Editor:** Conta > Importar > Do arquivo (ou Colar texto) > escolher esse arquivo > Processar > Revisar > Publicar.
- **Sem o Editor, pelo navegador:** Google Ads > Ferramentas > Ações em massa > Uploads > Novo upload > Procurar arquivo > Visualizar > Aplicar. (Não testado nesta conta: se reclamar de colunas, use o Editor.)
Fase 2 (sinistralidade e ANS) está em `csv_editor/fase2/` e não deve ser importada agora.
