# Mensagens de WhatsApp (templates WhatsApp Business) — **NÃO DISPARAR sem aprovação**
> Nenhum template foi submetido à Meta, nenhum número foi configurado, nenhuma mensagem foi enviada. Estrutura compatível com a WhatsApp Business Platform [VERIFICAR NA FONTE: políticas e categorias vigentes em business.whatsapp.com / developers.facebook.com/docs/whatsapp].

## Regras
1. **Opt-in obrigatório**: só enviar a quem aceitou receber mensagens por WhatsApp (campo `consentimento_whatsapp` + data/origem no CRM). Telefone informado em formulário, por si só, não equivale a opt-in para marketing [validar com jurídico].
2. **Categorias** (conforme a plataforma): *Utilidade* (confirmações e lembretes de reunião já solicitada) e *Marketing* (conteúdo, convite). Templates de início de conversa precisam de aprovação prévia da Meta; conversa iniciada pelo contato pode ter resposta livre dentro da janela de atendimento vigente [VERIFICAR NA FONTE].
3. **Sem spam**: no máximo 1 mensagem de marketing por contato por semana; pausa de 30 dias sem resposta; opt-out imediato com "SAIR" (registrar no CRM e confirmar uma vez).
4. **Sem dados de saúde** e sem dados pessoais de beneficiários. Sem promessas de resultado.
5. Horário comercial (seg–sex 9h–18h, fuso do contato).
6. Variáveis `{{1}}` = primeiro nome, etc. Mensagem de opt-out incluída nos de marketing.
7. Responsável pelo número e perfil verificado: [A CONFIRMAR].

## Templates (nomes em snake_case)
| # | Nome | Categoria | Quando | Texto | Botões |
|---|---|---|---|---|---|
| 1 | confirmacao_demo | Utilidade | Após agendamento | Olá, {{1}}. Confirmamos sua demonstração da NeoHealth BI · OPS em {{2}} às {{3}}. Duração prevista: 30 a 40 minutos. Link: {{4}}. Se precisar reagendar, responda esta mensagem. | Reagendar (resposta rápida) |
| 2 | lembrete_demo_24h | Utilidade | 24h antes | Olá, {{1}}. Lembrete: sua demonstração é amanhã, {{2}}, às {{3}}. Link: {{4}}. | Confirmar / Reagendar |
| 3 | lembrete_demo_1h | Utilidade | 1h antes | Olá, {{1}}. Sua demonstração começa em 1 hora. Link: {{2}}. | — |
| 4 | convite_demo | Marketing | Lead A/B com opt-in WhatsApp, sem agendamento | Olá, {{1}}. Aqui é {{2}}, da NeoHealth BI · OPS. Você baixou nosso material sobre inteligência estratégica para operadoras. Podemos mostrar, em 30 a 40 minutos, como os dados da {{3}} podem apoiar decisões. Responda SIM para combinarmos um horário. Para não receber mais mensagens, responda SAIR. | SIM / SAIR |
| 5 | entrega_material | Utilidade/Marketing* | Após pedido do material com opt-in | Olá, {{1}}. Aqui está o material que você solicitou: {{2}}. Para não receber mais mensagens, responda SAIR. *Categoria a validar. | Abrir material |
| 6 | follow_pos_demo | Utilidade | 1 dia após demo | Olá, {{1}}. Obrigado pela conversa de ontem. Enviamos o resumo por e-mail para {{2}}. Alguma dúvida que possamos esclarecer? | Falar com {{responsável}} |
| 7 | retomada_30d | Marketing | Lead sem resposta há 30 dias (com opt-in) | Olá, {{1}}. Passando para saber se ainda faz sentido conversarmos sobre a visão de dados da {{2}}. Responda SIM para retomarmos ou SAIR para encerrar. | SIM / SAIR |
| 8 | confirmacao_optout | Utilidade | Após SAIR | Pronto, {{1}}. Você não receberá mais mensagens de marketing da NeoHealth por este canal. | — |

## Respostas livres (dentro da janela de atendimento) — roteiro
- "Quero saber mais": perguntar cargo e principal desafio (1 pergunta por vez), oferecer horário.
- "Quanto custa?": "As condições dependem do escopo; apresentamos em proposta após entender sua operação. Podemos conversar 30 minutos?"
- "Quem são os clientes?": "Não divulgamos referências sem autorização. Mostramos a plataforma em base de demonstração."

## Registro obrigatório no CRM
data/hora do opt-in, origem, texto do consentimento, template enviado, resposta, opt-out.
