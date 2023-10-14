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
        
        Continua (...)

2. Desafios de código: Aperfeiçoe sua lógica e pensamento computacional
3. Desafios Python: Equilibrando Saldo
4. Desafios Python: Organizando seus ativos
5. Desafios Python: Condicionalmente rico
6. Desafios Python: Juros compostos
7. Desafios Python: O grande depósito
8. Criando um relatório de vendas elegante com Power BI
9. Processando e transformando dados com Power BI

Neste curso, utilizei a liguagem de programação Python, além de ter explorado SQL e Power BI.
