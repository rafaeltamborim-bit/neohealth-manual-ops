# Riscos, Compliance e LGPD
Não é parecer jurídico. Revisão por DPO/advogado é obrigatória antes de publicar [A CONFIRMAR]. Pesquisa de 01/11/2026 por WebSearch (acesso direto às páginas oficiais de políticas foi bloqueado no ambiente) — **toda afirmação sobre políticas de plataformas deve ser reconferida nas páginas oficiais** [VERIFICAR NA FONTE].

## 1. LGPD (Lei 13.709/2018)
Fonte: texto oficial https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm (consulta via buscador; artigos a reconferir no texto).
- **Dado sensível** (art. 5º, II) inclui dado referente à saúde. Materiais de marketing **não devem conter nem coletar dados de saúde de pessoas**. O público é B2B (profissionais), mas e-mail/cargo/empresa são dados pessoais.
- **Base legal** (art. 7º): para captação, adotar consentimento explícito em formulários/newsletter; legítimo interesse (art. 7º, IX; art. 10) só com teste de balanceamento documentado, e comunicação de abordagem direta com opt-out. Uma fonte secundária cita orientação da ANPD de que dado sensível não se ampara em legítimo interesse — confirmar na ANPD.
- **Direitos do titular** (art. 18): canal para acesso, correção, eliminação, revogação; prazo de resposta [VERIFICAR NA FONTE].
- **Opt-out** em todo e-mail/WhatsApp; registro de consentimento (data, texto, origem/UTM).
- **Minimização**: formulário curto (nome, e-mail corporativo, empresa, cargo); sem campos de saúde.
- **Política de privacidade e aviso de cookies** no site; DPO/encarregado identificado [A CONFIRMAR].
- **Operadores/transferência internacional**: ferramentas de CRM/anúncios podem transferir dados ao exterior — checar contratos (art. 33) [VERIFICAR NA FONTE].
- **Listas compradas**: não usar.
- **Plataforma NeoHealth** como operador/controlador dos dados dos clientes: contrato, segurança e retenção são fora do escopo de marketing [A CONFIRMAR].

## 2. Políticas de anúncios (saúde/dados) — o que a pesquisa indicou
(fontes secundárias; reconferir nas páginas oficiais)
- **Meta:** saúde tratada como categoria sensível; restrição de eventos de conversão e de segmentação; não enviar dados sensíveis via Pixel/Conversions API; lead ads não devem pedir informação de saúde. Fontes: https://oursprivacy.com/learn/platform-guides/meta-ads-for-healthcare-navigating-the-restricted-category-minefield ; https://www.gomarble.ai/blog/meta-special-ad-category-restrictions-guidelines. Ação: configurar pixel sem eventos de saúde; revisar categoria do anúncio; remarketing com cautela.
- **Google Ads:** política de anúncios personalizados restringe categorias sensíveis (incl. estado de saúde), podendo desativar públicos definidos pelo anunciante; há menção a flexibilização B2B em 2025 em fonte secundária (https://www.accelerateddigitalmedia.com/insights/health-marketing-policy-updates-2025/). Oficial: https://support.google.com/adspolicy [VERIFICAR NA FONTE]. Ação: priorizar pesquisa e contextual; evitar remarketing se vedado; não sugerir que se conhece a condição de saúde do usuário.
- **LinkedIn:** a pesquisa não retornou política específica de dados de saúde para segmentação; só política de conteúdo de saúde/imagem corporal. Oficial: https://www.linkedin.com/legal/ads-policy [VERIFICAR NA FONTE]. Ação: segmentar por cargo/setor, sem atributos de saúde.
- **Geral:** evitar linguagem que sugira diagnóstico ou dado pessoal ("você tem..."); público é gestor, não paciente.

## 3. Dados fictícios nas telas
- Todo criativo com tela deve levar a nota: **"Imagem da plataforma com dados fictícios (base de demonstração)"** (Ficha, regra 3).
- Usar só capas reais de `08_CRIATIVOS/assets_reais/`; sem telas fabricadas.
- Verificar em cada captura se não há nome real, CPF, carteirinha ou dado pessoal (a base é "Operadora Modelo" — confirmar com o proprietário que nada é real) [A CONFIRMAR].
- Nomes de operadoras, hospitais, médicos reais nas telas: proibidos.
- Vídeos: mesmo cuidado; legenda da nota no início/rodapé.

## 4. Matriz de riscos
| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Reprovação de anúncios por política de saúde | Média | Médio | Linguagem B2B; sem dados de saúde; revisão prévia |
| Alegação indevida (superioridade/resultado) | Média | Alto | Regras da Ficha; revisão jurídica; seção "o que não afirmar" |
| Dados pessoais sem base legal | Média | Alto | Consentimento, opt-out, minimização, DPO |
| Pixel/eventos com dado de saúde | Baixa | Alto | Eventos genéricos; auditoria de tags |
| Tela com dado real vazando | Baixa | Alto | Revisão de captura; nota de dados fictícios |
| Citação errada de norma ANS | Média | Médio | Link gov.br/ans; [VERIFICAR NA FONTE] |
| Funcionalidade prometida inexistente (ML, chat, WhatsApp, mobile) | Média | Alto | Status por item; [A CONFIRMAR] |
| Capacidade comercial insuficiente | Média | Médio | Escalar só após confirmação |
| Dependência de uma plataforma | Média | Médio | Mix de canais, SEO |
| Disparo de e-mail/WhatsApp sem opt-in | Baixa | Alto | Nenhum disparo sem aprovação e base consentida |
