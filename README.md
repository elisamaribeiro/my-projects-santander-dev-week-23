# Meus Projetos do Santander Dev Week 2023

Este repositório é reservado para os projetos que desenvolvi durante o **Santander Bootcamp 2023 - Ciência de Dados com Python**, que aconteceu entre os dias 16/08/2023 até 22/10/2023, no portal da **Digital Innovation One (DIO)**.

Aqui nesse repositório, você encontrará os projetos:

1. [Explorando IA Generativa em um Pipeline de ETL com Python](ia-generativa-pipeline-etl.py)

    Nesse projeto, o objetivo era realizar um Pipeline ETL, isto é, extrair dados de uma API do Banco Santander, transformar os dados gerando uma mensagem personalizada para cada usuário - utilizando a IA Generativa GPT-4 - e carregar os dados transformados para a API do Santander novamente.
        
    ### Passo um: criar usuários no API
    Iniciei o projeto criando 5 usuários na API do Santander, via [Swagger UI](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html#/Users%20Controller/findById), produzido e disponibilizado pela equipe da [DIO](https://www.dio.me/):
        
    | ID | Nome | Número | Agência | Limite Conta | Cartão | Limite Cartão |
    |---:|------|--------|---------|--------------|--------|---------------|
    | 4997 | Elisa | 34222-4 | 0016 | 500 | **** **** **** 5627 | 1000 |
    | 4998 | Manu | 36222-4 | 0016 | 500 | **** **** **** 5796 | 1000 |
   | 4999 | Isabela | 37222-4 | 0016 | 500 | **** **** **** 8963 | 1000 |
   | 5000 | Bruno | 38222-4 | 0016 | 500 | **** **** **** 9262 | 1000 |
   | 5001 | Luan | 39222-4 | 0016 | 500 | **** **** **** 7485 | 1000 |
        
   ### Passo dois: criar um arquivo .csv com os IDs criados
   Criei um arquivo .csv no meu computador com apenas a coluna ID e salvei com o nome _SDW2023.csv_
   | ID |
   |---:|
   | 4997 |
   | 4998 |
   | 4999 |
   | 5000 |
   | 5001 |
        
   [Continua (...)](ia-generativa-pipeline-etl.py)

2. [Desafios Python: Equilibrando Saldo](equilibrando_saldo.py)

   Nesse projeto, o desafio era para eu considerar que fui contratada por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: _um depósito e um saque_. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

   **Informação:** As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final seja realizado corretamente.

    ### Entrada

    _saldoAtual_: um número decimal representando o saldo atual da conta bancária.
    _valorDeposito_: um número decimal representando o valor a ser depositado na conta.
    _valorRetirada_: um número decimal representando o valor a ser retirado da conta.

    **Regra de Formatação:** Considere apenas uma casa decimal para esse desafio.

    ### Saída

    Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações. 

    [Continua(...)](equilibrando_saldo.py)
    
3. [Desafios Python: Organizando seus ativos](organizando_ativos.py)

    **Descrição do terceiro desafio:** Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancária, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

    ### Entrada

    A primeira entrada consiste em um número inteiro que representa a quantidade de ativos que o usuário possui. Em seguida, o usuário deverá informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

    ### Saída

    Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

    [Continua(...)](organizando_ativos.py)

4. [Desafios Python: Condicionalmente rico](condicionalmente_rico.py)

    **Descrição do quarto desafio:** Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint, como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.

    **Regras do saque:**

    - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
    - Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
    - Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
    - Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.

    ### Entrada
    A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.

    ### Saída
    Se o saque for realizado com sucesso, exibir a mensagem "Saque realizado com sucesso! Novo saldo: {saldo}", onde {saldo} é o novo saldo disponível na conta.

    Se o saque não for possível devido a saldo insuficiente, exibir a mensagem "Saldo insuficiente. Saque nao realizado!"

    [Continua (...)](condicionalmente_rico.py)

5. [Desafios Python: Juros compostos](juros_compostos.py)

    **Descrição do quinto desafio:** Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração os juros compostos.

    ### Entrada:
    A função deve receber os seguintes parâmetros:

    *valor_inicial:* um número inteiro ou decimal representando o valor inicial do investimento.
    *taxa_juros:* um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.
    *periodo:* um número inteiro representando a quantidade de anos do investimento.

    ### Saída:
    A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.

    [Continua (...)](juros_compostos.py) 

6. [Desafios Python: O grande depósito](grande_deposito.py)

    **Descrição do sexto desafio:** Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve soliticar apenas uma vez o valor de depósito.

    ### Entrada
    O programa deve utilizar o Scanner para receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.

    ### Saída
    O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

    [Continua (...)](grande_deposito.py)

7. [Criando um relatório de vendas elegante com Power BI](powerbi-vendas)

8. Processando e transformando dados com Power BI

Neste curso, utilizei a liguagem de programação Python, além de ter explorado SQL e Power BI.
