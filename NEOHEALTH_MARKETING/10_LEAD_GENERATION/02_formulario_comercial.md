# Especificação do formulário comercial ("Solicite uma demonstração")
Uso: landing page (`03_SITE_LANDING_PAGE`), anúncios com lead form (LinkedIn/Meta) e e-book/checklist (versão curta).

## Campos — versão DEMONSTRAÇÃO
| # | Campo | Rótulo | Tipo | Obrig. | Validação / observação | Propriedade CRM |
|---|---|---|---|---|---|---|
| 1 | nome | Nome completo | texto | Sim | ≥2 palavras | firstname/lastname |
| 2 | email | E-mail corporativo | email | Sim | Rejeitar domínios gratuitos (gmail, hotmail, outlook, yahoo…) com mensagem amigável; permitir exceção manual | email |
| 3 | telefone | Telefone / WhatsApp | tel | Não* | Máscara BR (DDD). *Obrigatório só se marcar contato por WhatsApp | phone |
| 4 | empresa | Operadora / empresa | texto | Sim | — | company |
| 5 | tipo_operadora | Tipo de operadora | select | Sim | Medicina de grupo · Cooperativa médica · Autogestão · Seguradora de saúde · Odontológica · Filantropia · Outro · Não sou operadora | tipo_operadora |
| 6 | porte | Porte (nº de beneficiários) | select | Não | Faixas [A DEFINIR com o comercial]; opção "Prefiro não informar" | porte_beneficiarios |
| 7 | cargo | Cargo | texto/select | Sim | Lista: Diretoria · Financeiro · Controladoria/Contabilidade · Atuária · Assistencial/Médico · Regulatório/Compliance · TI/BI · Outro | cargo / persona |
| 8 | erp | Sistema de gestão (ERP) | select | Não | Philips Tasy · Outro (campo livre) · Não sei. *Não afirmar integração com outros ERPs* [A CONFIRMAR] | erp_utilizado |
| 9 | desafios | Principais desafios | multi-select (máx. 3) | Não | Visibilidade financeira · Sinistralidade · Gestão assistencial · Obrigações regulatórias/ANS · Previsão de cenários · Consolidação de dados | desafios |
| 10 | mensagem | Conte o que você gostaria de ver | textarea (≤500) | Não | Aviso: "Não informe dados pessoais de saúde de beneficiários." | mensagem |
| 11 | consent_contato | Consentimento (texto abaixo) | checkbox | **Sim** | Não pré-marcado | consentimento_contato + data/hora |
| 12 | consent_marketing | Receber conteúdos | checkbox | Não | Não pré-marcado; separado do 11 | consentimento_marketing + data/hora |

### Campos ocultos (preenchidos por script)
utm_source, utm_medium, utm_campaign, utm_content, utm_term, gclid/li_fat_id/fbclid (se existir), pagina_origem (URL), referrer, form_id, timestamp_utc, versao_texto_consentimento, ip_hash (se a ferramenta registrar; decidir com o encarregado [A CONFIRMAR]), campo honeypot (deve ficar vazio).

### Textos
- **Título**: "Solicite uma demonstração."
- **Subtítulo**: "Conheça o potencial dos dados da sua operadora. Uma conversa de 30 a 40 minutos, com telas da plataforma em base de demonstração."
- **Botão**: "Solicitar demonstração"
- **Consentimento (11)**: "Autorizo a NeoHealth a usar meus dados para entrar em contato sobre minha solicitação, conforme a Política de Privacidade [LINK A PUBLICAR]." 
- **Consentimento (12)**: "Quero receber conteúdos e novidades da NeoHealth por e-mail. Posso cancelar quando quiser."
- **Rodapé do form**: "Controlador: [RAZÃO SOCIAL/CNPJ — A CONFIRMAR]. Encarregado (DPO): [E-MAIL — A CONFIRMAR]. Seus direitos: acesso, correção, eliminação, revogação etc."
- **Nota de imagem** (se houver tela): "Imagem da plataforma com dados fictícios (base de demonstração)."
- **Confirmação**: "Recebemos sua solicitação. Nossa equipe entra em contato em até 1 dia útil [SLA A CONFIRMAR]."

## Versão E-BOOK / CHECKLIST (curta)
nome, email corporativo, empresa, cargo, tipo_operadora, consent_contato (ou consent_marketing, conforme a base legal escolhida — ver `12_CRM/02_LGPD.md`). Entrega por e-mail (double opt-in recomendado) ou download direto.

## Regras
1. Minimização: só pedir o necessário; nenhum dado pessoal de saúde.
2. Anti-spam: honeypot + reCAPTCHA/hCaptcha [A DECIDIR]; sem CAPTCHA que prejudique acessibilidade.
3. Acessibilidade: labels associados, contraste AA, navegação por teclado, mensagens de erro textuais.
4. Pós-envio: evento GA4 `generate_lead` (ver `11_AUTOMACOES/02_webhooks_utm_ga4.md`), redirecionar para `/obrigado` (sem dados na URL).
5. Payload ao CRM: JSON do `11_AUTOMACOES`. Duplicidade: chave = e-mail em minúsculas; se existir, atualizar e registrar nova conversão como atividade.
6. Registro de origem e consentimento obrigatório (ver LGPD).

## Testes de aceite
Envio válido cria lead; e-mail gratuito é barrado; consentimento desmarcado impede envio; UTMs persistem entre páginas (sessionStorage/cookie com consentimento); honeypot preenchido não cria lead; mobile 360 px utilizável.
