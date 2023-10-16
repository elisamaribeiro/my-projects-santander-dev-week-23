# Desafios Python: Equilibrando Saldo

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#Calcular o saldo atualizado de acordo com a descrição deste desafio.

saldo_atualizado = float(saldo_atual + valor_deposito - valor_retirada)

#Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

print(f"Saldo atualizado na conta: {saldo_atualizado}")

# Exemplo de cálculo

saldo_atual = float(input(1000))
valor_deposito = float(input(500))
valor_retirada = float(input(200))

saldo_atualizado = float(saldo_atual + valor_deposito - valor_retirada)

print(f"Saldo atualizado na conta: {saldo_atualizado}")

"Saldo atualizado na conta: 1300.0"
