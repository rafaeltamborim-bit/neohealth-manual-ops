# Comparativo de opções econômicas (sem contratar nada)
Pesquisa em 01/11/2026 via busca web. **Os valores abaixo vêm de resultados de busca (blogs, comparadores e páginas oficiais), frequentemente divergentes e datados. Conferir SEMPRE nas páginas oficiais antes de decidir** [VERIFICAR NA FONTE]. Preços em USD ou BRL conforme a fonte. Nenhuma conta foi criada.

## Informações levantadas
| Opção | O que é | Dados encontrados | Fonte(s) |
|---|---|---|---|
| **HubSpot Free** | CRM + marketing básico | Contas novas: 2 usuários, ~1.000 contatos, ~2.000 envios de e-mail marketing/mês, 10 propriedades personalizadas; sem workflows e sem sequences no plano gratuito; e-mails com marca HubSpot. Fontes divergem (contas antigas com limites maiores). | [HubSpot FAQ](https://knowledge.hubspot.com/getting-started/frequently-asked-questions), [vedain.com](https://vedain.com/blog/7-hubspot-free-plan-limitations-2026-hidden-caps), [usecarly.com](https://www.usecarly.com/blog/hubspot-free-plan-limits/) |
| **RD Station Marketing** (BR) | Automação de marketing | Página oficial (via busca): Light R$ 50/mês (promo), Basic R$ 178/mês, Pro R$ 1.121/mês, Advanced sob consulta; Light até 3 usuários, Basic 7, Pro 15; Pro/Enterprise com contrato mínimo de 12 meses; **lead scoring, lead tracking e automação de segmentação só em Pro/Enterprise**. Valores variam por tamanho da base e promoções (outras fontes citam valores bem diferentes). | [RD Station – planos](https://www.rdstation.com/planos/marketing/encontre-seu-plano-ideal/), [blog RD Station](https://www.rdstation.com/blog/marketing/planos-precos-rd-station-marketing/) |
| **Pipedrive** | CRM de vendas (pipeline) | Cobrança por usuário. Faixas citadas (USD, cobrança anual): Essential ~US$ 12,50–14,90; Advanced ~24,90–29; Professional ~49–59; mensal mais caro. Fontes divergem/datadas. | [Capterra](https://www.capterra.com/p/132666/Pipedrive/pricing/), [emailtooltester](https://www.emailtooltester.com/en/crm/pipedrive-review/pricing/), [saasgenius](https://www.saasgenius.com/reviews/pipedrive-pricing) |
| **n8n** | Automação (workflows) | Community Edition self-hosted gratuita sob licença "fair-code" (uso interno de negócio; recursos como SSO/permissões avançadas são pagos); custo principal é hospedagem (fontes citam ~US$ 4–7/mês em VPS). Cloud: ~US$ 20–24/mês (Starter), fontes divergem. Cobra por execução de workflow. | [cloudzero](https://www.cloudzero.com/blog/n8n-pricing/), [toolradar](https://toolradar.com/blog/n8n-pricing-2026), [nocode.mba](https://www.nocode.mba/articles/n8n-pricing) |
| **Make** | Automação visual (cloud) | Plano gratuito: 1.000 operações/mês (página oficial de parâmetros de preço), 2 cenários ativos, intervalo mínimo de 15 min; sem self-hosting; cobra por operação (módulo). Core ~US$ 9–10,59/mês (anual). | [Make – pricing parameters](https://www.make.com/en/help/general/pricing-parameters), [costbench](https://www.costbench.com/software/ai-automation/make/free-plan/) |
| **Planilha + Apps Script** | Google Sheets + script | Sem custo de licença para conta Google pessoal/Workspace já existente; limites de cota do Apps Script existem [VERIFICAR NA FONTE: developers.google.com/apps-script/guides/services/quotas]. Protótipo incluso em `prototipo/`. | — (documentação do Google) |

## Comparação funcional (qualitativa)
| Critério | HubSpot Free | RD Station | Pipedrive | n8n (self-host) | Make | Planilha + Apps Script |
|---|---|---|---|---|---|---|
| CRM/pipeline | Sim | Parcial (CRM próprio, planos) [VERIFICAR] | Sim (núcleo) | Não (orquestra) | Não | Manual |
| Formulários + captura | Sim | Sim | Via complementos | Via webhook | Via webhook | Via Google Forms/webhook |
| Lead scoring | Limitado/pago [VERIFICAR] | Só Pro+ | Via regras/campos | Código/função | Módulos | Script (protótipo) |
| Automação de e-mail | 2.000 envios/mês, sem workflows no Free | Sim (planos) | Add-on | Via SMTP/serviço | Via módulos | Limitado (cotas) |
| Suporte em português | Parcial | Sim | Parcial | Comunidade | Comunidade | — |
| Custo inicial | Zero licença | Baixo a alto | Por usuário | Hospedagem + tempo | Zero a baixo | Zero |
| Esforço técnico | Baixo | Baixo/médio | Baixo | Médio/alto | Médio | Médio |
| LGPD/dados | Dados em provedor externo (transferência internacional: avaliar) | Provedor brasileiro [VERIFICAR localização] | Provedor externo | Dados no seu ambiente | Provedor externo | Dados na conta Google |
| Escala | Limite baixo no Free | Boa | Boa | Boa | Limite de operações | Baixa |

## Recomendação (por fase, a validar com o proprietário)
1. **Fase 1 (dias 1–30, volume baixo, custo mínimo):** **HubSpot Free** como CRM + formulários (limites de contatos/envios atendem a um piloto B2B de nicho) **e/ou** planilha-modelo do `12_CRM` + protótipo de score. Justificativa: custo de licença zero, menor esforço, pipeline e propriedades prontos. Limitações: sem workflows/sequences no Free → follow-up manual com tarefas; verificar limites da conta no momento do cadastro.
2. **Fase 2 (dias 31–90, se houver tração):** avaliar **Pipedrive** (pipeline por usuário) ou **RD Station Pro** (se scoring/automação forem prioridade e houver orçamento) e **n8n self-hosted** se houver apoio de TI para orquestrar webhooks sem custo por operação.
3. **Evitar** no início: contratos com fidelidade de 12 meses (ex.: RD Pro) antes de validar o processo.
Decisão final, custos e transferência internacional de dados dependem de aprovação e do jurídico [A APROVAR].

## Observação metodológica
Resultados de busca incluem sites de afiliados e comparadores; nenhuma cotação foi confirmada com os fornecedores. Cada número deve ser reconfirmado na página oficial no dia da decisão.
