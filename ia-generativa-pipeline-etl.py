# Projeto 1: Explorando IA Generativa em um Pipeline de ETL com Python

# Passo três: upload arquivo .csv e extrair informações de ID da API do Santander 
# De início, criei uma variável com o endereço da API:

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# A seguir, importei a biblioteca pandas para extrair os dados e carreguei o meu arquivo .csv com os IDs.

import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

# O print() retornou:

[4997, 4998, 4999, 5000, 5001]

# Após isso, rodei o código para importar os dados dos usuários que gerei no [Swagger UI](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html#/Users%20Controller/findById).

import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# Com isso, meus usuários foram retornados:

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

# Passo quatro: fase de transformação de dados, onde deve ser gerado uma mensagem de marketing personalizada para cada usuário utilizando a IA Generatira GPT-4
# Primeiro, instalei o openai para conseguir utilizar o GPT-4:

!pip install openai

# Depois, informei minha API Key da Open IA para conseguir utilizar o Chat:

openai_api_key = 'inclua-key-aqui'

# Depois, passei as instruções para o Python informando que eu queria que ele gerasse, via IA GPT-4, mensagens personalizadas para cada um dos 5 usuários que criei, informando sobre a importância do investimento no planejamento financeiro do cliente:

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

# Ao executar o código anterior, tive como retorno:

"Elisa, invista em seu futuro com segurança!"
"Manu, planeje hoje para colher amanhã!"
"Isabela, seu futuro merece investimentos inteligentes!"
"Bruno, construa riqueza com planejamento sólido!"
"Luan, investir agora é garantir seu amanhã!"

# Passo cinco: fase de carregamento dos dados transformados de volta para a API do Santander
# Para isso, solicitei que o Python atualizasse a lista de "news" em cada usuário

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")

# Recebi como resposta ao código

"User Elisa updated? True!"
"User Manu updated? True!"
"User Isabela updated? True!"
"User Bruno updated? True!"
"User Luan updated? True!"

# Para conferência, se você consultar cada um dos usuários acima no "Get a user by ID" no Swagger UI, você terá como retorno:
# Ao pesquisar o ID 4997

{
  "id": 4997,
  "name": "Elisa",
  "account": {
    "id": 5303,
    "number": "34222-4",
    "agency": "0016",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4862,
    "number": "**** **** **** 5627",
    "limit": 1000
  },
  "features": [
    {
      "id": 1562,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9339,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Elisa, invista em seu futuro com segurança!"
    }
  ]
}

# Ao pesquisar o ID 4998

{
  "id": 4998,
  "name": "Manu",
  "account": {
    "id": 5304,
    "number": "36222-4",
    "agency": "0016",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4863,
    "number": "**** **** **** 5796",
    "limit": 1000
  },
  "features": [
    {
      "id": 1563,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9340,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Manu, planeje hoje para colher amanhã!"
    }
  ]
}

# Ao pesquisar o ID 4999

{
  "id": 4999,
  "name": "Isabela",
  "account": {
    "id": 5305,
    "number": "37222-4",
    "agency": "0016",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4864,
    "number": "**** **** **** 8963",
    "limit": 1000
  },
  "features": [
    {
      "id": 1564,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9341,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Isabela, seu futuro merece investimentos inteligentes!"
    }
  ]
}

# Ao pesquisar o ID 5000

{
  "id": 5000,
  "name": "Bruno",
  "account": {
    "id": 5306,
    "number": "38222-4",
    "agency": "0016",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4865,
    "number": "**** **** **** 9262",
    "limit": 1000
  },
  "features": [
    {
      "id": 1565,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9342,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Bruno, construa riqueza com planejamento sólido!"
    }
  ]
}

# Ao pesquisar 5001

{
  "id": 5001,
  "name": "Luan",
  "account": {
    "id": 5307,
    "number": "39222-4",
    "agency": "0016",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4866,
    "number": "**** **** **** 7485",
    "limit": 1000
  },
  "features": [
    {
      "id": 1566,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9343,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Luan, investir agora é garantir seu amanhã!"
    }
  ]
}

# Esse é o final do código! Obrigada por acompanhar até aqui!

