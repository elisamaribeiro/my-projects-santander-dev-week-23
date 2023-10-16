# Desafio Python: Condicionalmente Rico

# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
    saldo = int(saldo_total - valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
    
else:
    print("Saldo insuficiente. Saque nao realizado!")

# Exemplo

saldo_total = int(input(1000))
valor_saque = int(input(200))

if saldo_total >= valor_saque:
    saldo = int(saldo_total - valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
    
else:
    print("Saldo insuficiente. Saque nao realizado!")

"Saque realizado com sucesso. Novo saldo: 800"
