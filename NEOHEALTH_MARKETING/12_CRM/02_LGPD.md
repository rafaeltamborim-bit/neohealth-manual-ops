# LGPD no funil e no CRM
> Orientação operacional, **não é parecer jurídico**. Validar com advogado/encarregado (Lei 13.709/2018) [A CONFIRMAR]. Dispositivos legais devem ser conferidos na fonte oficial (planalto.gov.br) [VERIFICAR NA FONTE].

## 1. Princípios aplicados
Finalidade, adequação, necessidade (minimização), transparência, segurança, prevenção, não discriminação, responsabilização. **Não coletar dados pessoais de saúde** nem de beneficiários em nenhum formulário, campo livre, nota ou atividade.

## 2. Bases legais sugeridas (a validar)
| Tratamento | Base sugerida | Observações |
|---|---|---|
| Resposta a pedido de demonstração/contato | Procedimentos preliminares relacionados a contrato a pedido do titular, ou consentimento | Registrar o pedido |
| Download de e-book/checklist + envio de materiais | Consentimento (checkbox separado, não pré-marcado) | Double opt-in recomendado |
| Nutrição por e-mail | Consentimento; ou legítimo interesse em B2B com teste de balanceamento documentado [decisão do jurídico] | Opt-out em todo e-mail |
| WhatsApp marketing | Consentimento específico (opt-in) | Registrar data, origem e texto |
| Prospecção ativa (outbound, dados profissionais) | Legítimo interesse, com LIA documentada [jurídico] | Informar origem do dado e permitir oposição no 1º contato |
| Analytics/cookies | Consentimento via banner | Sem tags de marketing antes do aceite |
| Retenção de supressão (opt-out) | Cumprimento de obrigação/exercício regular de direitos/legítimo interesse | Manter só o mínimo para não recontatar |

## 3. Consentimento — requisitos
Livre, informado, inequívoco, finalidade específica; texto claro; separado por finalidade (contato x marketing x WhatsApp); sem pré-marcação; revogável a qualquer momento e tão fácil quanto dar. Guardar: texto/versão, data-hora UTC, URL, form_id, IP/hash [decisão do DPO], user-agent (opcional).

## 4. Registro de origem (obrigatório por contato)
Campos: origem (canal/campanha/UTMs), data da captura, página/form, base legal, consentimentos, responsável, histórico de alterações. Para listas/outbound: fonte (ex.: site institucional, LinkedIn profissional), data da coleta. **Proibido comprar listas.**

## 5. Retenção (proposta, a validar)
| Dado | Prazo sugerido | Ação ao fim |
|---|---|---|
| Lead sem interação / nutrição inativa | 24 meses desde a última interação [A CONFIRMAR] | Anonimizar/eliminar |
| Lead descartado | 6 meses (motivo mantido sem dados pessoais) | Eliminar |
| Negócio perdido | 24 meses | Anonimizar contato |
| Cliente (contrato) | Conforme contrato e obrigações legais | Política específica |
| Registro de opt-out | Enquanto necessário para não recontatar | Revisar anualmente |
| Logs de consentimento | Prazo prescricional aplicável [jurídico] | — |
Revisão trimestral de retenção (relatório "retencao_ate vencido").

## 6. Direitos do titular
Acesso, correção, anonimização/bloqueio/eliminação, portabilidade, informação sobre compartilhamento, revogação do consentimento, oposição. Procedimento: canal [E-MAIL DO ENCARREGADO — A CONFIRMAR]; confirmar identidade; responder em prazo legal [VERIFICAR NA FONTE]; registrar solicitação no CRM (data, tipo, resposta, responsável); propagar eliminação a ferramentas conectadas (e-mail, planilhas, backups conforme política).

## 7. Segurança e governança
Acesso por perfil e MFA; sem planilhas com dados pessoais em contas pessoais; exportações controladas; contratos com operadores (ferramentas SaaS) e avaliação de transferência internacional; plano de resposta a incidentes; treinamento do time; ROPA (registro de operações) atualizado; RIPD/DPIA se aplicável.

## 8. Checklist de conformidade por canal
- Formulário: consentimento separado, link da política, controlador/DPO visíveis.
- E-mail: remetente identificado, opt-out de um clique, endereço do controlador.
- WhatsApp: opt-in registrado, SAIR funciona, horário comercial.
- LinkedIn: sem automação massiva, respeitar termos da plataforma.
- Telefone: identificar-se, informar origem do contato, respeitar recusa.
