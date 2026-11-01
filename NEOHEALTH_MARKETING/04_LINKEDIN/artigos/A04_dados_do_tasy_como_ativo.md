# A04 — Dados do Tasy como ativo estratégico da operadora

- **Formato:** Artigo LinkedIn
- **Objetivo:** Autoridade em dados; abrir conversa com operadoras que usam Philips Tasy
- **Público:** TI, BI, dados, diretoria de operadoras que usam o ERP Philips Tasy
- **CTA:** Conheça o potencial dos dados da sua operadora.
- **Hashtags:** #Tasy #DadosComoAtivo #GovernancaDeDados #OperadorasDeSaude #SaudeDigital #NeoHealth
- **Direção de arte (capa):** fluxo minimalista ERP, espelho analítico, decisão, em linhas azul #4190D3 e ciano; fundo #060A15; sem logotipos de terceiros [A CONFIRMAR uso da marca Philips Tasy; usar apenas texto].
- **Funcionalidades citadas / status:** integração com ERP Philips Tasy e Oracle; espelhamento analítico DuckDB; multi-tenant; governança e auditoria [DISPONÍVEL conforme Ficha]; detalhes de implantação [A CONFIRMAR]

---

## Texto

Um ERP hospitalar ou de operadora registra, minuto a minuto, o que acontece na operação: cadastros, contratos, autorizações, guias, cobranças, pagamentos. É um volume extraordinário de informação. E muitas vezes esse volume permanece onde nasceu, útil para a rotina transacional e subutilizado para a decisão estratégica.

Tratar os dados do ERP como ativo significa mudar a pergunta: em vez de "o sistema está registrando corretamente?", perguntar "o que esses registros poderiam nos ajudar a decidir?".

### Registro não é análise

O sistema transacional é otimizado para gravar e consultar eventos individuais com rapidez. A análise gerencial faz o oposto: agrega milhões de eventos, cruza dimensões e compara períodos. Quando as duas coisas disputam o mesmo banco de dados, aparecem lentidão, consultas pesadas e receio da TI de liberar acesso.

Uma resposta comum é extrair dados para planilhas. Funciona até o dia em que existem dez versões da mesma planilha e ninguém sabe qual é a correta. Outra resposta é criar um repositório analítico separado, atualizado de forma regular, onde as perguntas gerenciais possam ser respondidas sem afetar o ambiente de produção.

### A ideia do espelho analítico

Na NeoHealth BI · OPS, a integração com a base Oracle e o ERP Philips Tasy alimenta um espelhamento analítico local, construído sobre DuckDB, um motor de banco de dados analítico. A lógica é simples: a operação segue no sistema transacional; as análises rodam num espelho preparado para consultas agregadas. [DISPONÍVEL conforme Ficha de Fatos. Frequência de atualização, volumes suportados e escopo de tabelas por cliente: A CONFIRMAR.]

### Quatro características de um dado que virou ativo

**1. Origem conhecida.** Para cada indicador, é possível dizer de onde vem, como foi calculado e quando foi atualizado. Sem isso, qualquer discussão em reunião vira uma disputa sobre o número.

**2. Definição comum.** "Sinistralidade", "vida ativa" ou "glosa" têm a mesma definição em todas as áreas. Dicionário de termos e glossário integrado à análise ajudam a manter essa consistência.

**3. Acesso por perfil.** Dados de saúde são sensíveis. O ativo precisa estar disponível a quem precisa dele, no nível de detalhe adequado, e com registro de acesso. Controle de acesso e auditoria fazem parte do desenho, não são adicionais. Para ambientes multi-organização, o isolamento entre clientes (multi-tenant) é requisito básico.

**4. Qualidade monitorada.** Cadastros incompletos, códigos fora de padrão, lotes rejeitados: problemas de qualidade aparecem primeiro nos relatórios, mas nascem no processo. Identificá-los cedo é parte do valor.

### O que o dado do ERP pode apoiar

Sem prometer resultado específico, algumas famílias de decisão se beneficiam diretamente de dados bem organizados:

- **Sinistralidade:** decomposição por produto, prestador, procedimento e perfil de utilização.
- **Gestão assistencial:** estratificação de risco, acompanhamento de alto custo e leitura de padrões de internação.
- **Financeiro e contábil:** conciliação entre visão gerencial e contábil.
- **Rede e glosas:** análise por prestador, procedimento e padrão de outliers.
- **Regulatório:** cruzamento entre o que o sistema registra e o que é enviado e retornado nas obrigações.

### Um diagnóstico em sete perguntas

Antes de qualquer projeto, vale responder:

1. Quais três decisões a diretoria gostaria de tomar com mais informação?
2. Quais dados do ERP alimentam essas decisões?
3. Quem hoje extrai esses dados e com que frequência?
4. Existe uma definição única para os principais indicadores?
5. Há risco de consultas analíticas afetarem a operação?
6. Quem tem acesso a dados detalhados e como isso é auditado?
7. Quanto tempo se leva para responder uma pergunta nova?

As respostas indicam se o gargalo é de tecnologia, de processo ou de governança. Muitas vezes é uma combinação dos três.

### Cuidados com LGPD

Ativo não significa liberação geral. A análise estratégica quase sempre pode ser feita em visões agregadas; quando o detalhe individual for necessário (por exemplo, gestão de caso), o acesso deve ter base legal clara, finalidade definida e registro. Materiais de divulgação, como este, nunca devem conter dados pessoais de saúde. As telas mostradas pela NeoHealth em campanhas vêm da base de demonstração "Operadora Modelo", com dados fictícios.

### O papel da TI

Um projeto de dados bem-sucedido não tira a TI de cena; dá a ela um papel mais estratégico. Em vez de atender pedidos de extração, passa a cuidar da qualidade das fontes, da segurança e da arquitetura. A área de negócio ganha autonomia para explorar, e a TI ganha previsibilidade.

### Implantação: o que perguntar

Se a operadora avalia uma plataforma, convém perguntar: como se dá a conexão com o ambiente atual? Há opção de instalação on-premise? [A CONFIRMAR condições comerciais e técnicas.] Como é o isolamento de dados? Quanto tempo até as primeiras visões úteis? Essas respostas dependem de cada ambiente e devem ser tratadas em conversa técnica, sem promessas genéricas.

### Do ativo ao hábito: três sinais de maturidade

O primeiro sinal é a **autonomia**: gestores formulam e respondem perguntas sem abrir chamado para a TI a cada vez. O segundo é a **confiança**: em reunião, ninguém gasta tempo discutindo qual planilha está certa. O terceiro é a **continuidade**: o conhecimento sobre os dados não depende de uma única pessoa. Operadoras que chegam a esse estágio costumam discutir menos números e mais decisões, que é exatamente o objetivo.

### Erros frequentes

Três tropeços aparecem com regularidade: começar pela ferramenta sem definir as decisões a apoiar; tentar cobrir todos os temas de uma vez, em vez de escolher um de alto valor e expandir; e ignorar a governança até que um incidente a torne urgente. Evitá-los não exige grandes investimentos, apenas disciplina de escopo e de responsabilidade.

### Conclusão

Os dados do Tasy já existem; o investimento já foi feito. A questão é quanto desse patrimônio chega a quem toma decisões, com segurança e a tempo. Transformar registro em ativo é um trabalho de organização, definição e governança, e a tecnologia certa o torna mais rápido e repetível.

**Conheça o potencial dos dados da sua operadora.**
