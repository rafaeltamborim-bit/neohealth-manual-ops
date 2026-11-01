# Estrutura do CRM
## 1. Objetos
Empresa (operadora) 1—N Contatos; Empresa 1—N Negócios; Contato N—N Negócios; Atividades associadas a contato/negócio.

## 2. Propriedades
### Contato / Lead
| Propriedade (id) | Tipo | Obrigatório | Valores / observação |
|---|---|---|---|
| lead_id | texto | auto | |
| nome, sobrenome, email (chave), telefone | texto | email sim | e-mail minúsculo |
| cargo, persona | texto/lista | sim | Diretoria · Financeiro · Atuária · Assistencial · Regulatório · TI/BI · Outro |
| status_lead | lista | sim | Novo · Em qualificação · MQL · SQL · Nutrição · Descartado |
| score, classe | número/lista | auto | A/B/C/Descarte |
| pilar_interesse | multi | não | Financeira · Sinistralidade · Assistencial · Regulatória · Preditiva |
| desafios | multi | não | |
| origem (utm_*_first/last, pagina_origem, form_id, data_conversao) | texto | auto | registro de origem |
| consentimento_contato / consentimento_marketing / consentimento_whatsapp | booleano | sim | com data/hora, canal, versão do texto, prova |
| base_legal | lista | sim | Consentimento · Execução de procedimentos preliminares a contrato · Legítimo interesse [validar] |
| opt_out_data, opt_out_canal | data/texto | | |
| responsavel | usuário | sim | |
| proxima_acao, data_proxima_acao | texto/data | classe A/B | |
| motivo_descarte | lista | se descartado | Fora do ICP · Concorrente · Sem interesse · Dados inválidos · Opt-out |
| retencao_ate | data | auto | ver LGPD |
### Empresa
nome, dominio (chave), cnpj [opcional], tipo_operadora, porte_beneficiarios (faixa), uf, erp_utilizado, registro_ans [opcional, dado público — conferir na fonte], alternativa_atual, observacoes.
### Negócio
nome, empresa, contatos, etapa, probabilidade, valor_estimado [A DEFINIR], moeda, data_fechamento_prevista, pilares_escopo, modelo_implantacao, decisor, campeao, processo_decisao, janela_decisao, concorrencia/alternativa, motivo_perda, origem, responsavel, proxima_acao, data_proxima_acao.
### Atividade
tipo (E-mail · Ligação · Reunião/Demo · WhatsApp · LinkedIn · Nota · Tarefa), data_hora, responsavel, contato, negocio, assunto, resultado, observacao (sem dados de saúde).

## 3. Pipeline de negócios (probabilidades = hipótese inicial, calibrar com histórico real) [A CONFIRMAR]
| Etapa | Critério de entrada | Probabilidade |
|---|---|---|
| 1. Qualificação | SQL com dor confirmada | 10% |
| 2. Demonstração agendada | Data marcada com ≥1 stakeholder | 20% |
| 3. Demonstração realizada | Demo feita, próximo passo acordado | 35% |
| 4. Proposta enviada | Escopo validado, proposta entregue | 55% |
| 5. Negociação / Análise jurídica-compras | Revisão em curso | 75% |
| 6. Ganho (Contratação) | Contrato assinado | 100% |
| 7. Perdido | Decisão de não seguir, com motivo | 0% |
Regras: negócio parado > 14 dias em uma etapa → alerta; toda mudança exige próxima ação datada.
Mapeamento com o funil: Qualificação→etapa 1; Demonstração→2–3; Proposta→4; Contratação→5–6.

## 4. Views (listas salvas)
Leads novos sem contato · Classe A (4 h) · Classe B (1 dia) · Em nutrição · MQL sem responsável · Demos da semana · Negócios por etapa (kanban) · Negócios parados >14 dias · Propostas aguardando retorno · Opt-outs · Consentimentos ausentes · Leads por origem/campanha.

## 5. Relatórios
1. Leads por origem/campanha/mês. 2. Conversão por etapa do funil. 3. Tempo de resposta (SLA) por classe. 4. Distribuição de score/classes. 5. Demos agendadas x realizadas (no-show). 6. Pipeline ponderado (valor × probabilidade) [quando valores existirem]. 7. Ciclo de vendas. 8. Motivos de perda e de descarte. 9. Atividade por responsável. 10. Qualidade de dados (campos vazios, duplicidades). 11. Opt-outs e pedidos de titulares. Dashboard consolidado em `13_DASHBOARD_MARKETING`.
