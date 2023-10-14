# Projeto 1: Explorando IA Generativa em um Pipeline de ETL com Python

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

### Passo três: upload arquivo .csv e extrair informações de ID da API do Santander 
De início, criei uma variável com o endereço da API:
```
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'
```
A seguir, importei a biblioteca pandas para extrair os dados e carreguei o meu arquivo .csv com os IDs.
```
import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)
```
O print() retornou:
```
[4997, 4998, 4999, 5000, 5001]
```
Após isso, rodei o código para importar os dados dos usuários que gerei no [Swagger UI](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html#/Users%20Controller/findById).
```
import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))
```
Com isso, meus usuários foram retornados:
```
[
  {
    "id": 4997,
    "name": "Elisa",
    "account": {
      "id": 5303,
      "number": "34222-4",
      "agency": "0016",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4862,
      "number": "**** **** **** 5627",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 4998,
    "name": "Manu",
    "account": {
      "id": 5304,
      "number": "36222-4",
      "agency": "0016",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4863,
      "number": "**** **** **** 5796",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 4999,
    "name": "Isabela",
    "account": {
      "id": 5305,
      "number": "37222-4",
      "agency": "0016",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4864,
      "number": "**** **** **** 8963",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 5000,
    "name": "Bruno",
    "account": {
      "id": 5306,
      "number": "38222-4",
      "agency": "0016",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4865,
      "number": "**** **** **** 9262",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 5001,
    "name": "Luan",
    "account": {
      "id": 5307,
      "number": "39222-4",
      "agency": "0016",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4866,
      "number": "**** **** **** 7485",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  }
]
```
### Passo quatro: fase de transformação de dados, onde deve ser gerado uma mensagem de marketing personalizada para cada usuário utilizando a IA Generatira GPT-4
Primeiro, instalei o _openai_ para conseguir utilizar o GPT-4:
```
!pip install openai
```
Depois, informei minha API Key da Open IA para conseguir utilizar o Chat:
```
openai_api_key = 'inclua-key-aqui'
```
Depois, passei as instruções para o Python informando que eu queria que ele gerasse, via IA GPT-4, mensagens personalizadas para cada um dos 5 usuários que criei, informando sobre a importância do investimento no planejamento financeiro do cliente:
```
import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um gerente com conhecimento em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos no planejamento financeiro (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
```
Ao executar o código anterior, tive como retorno:
```

```
