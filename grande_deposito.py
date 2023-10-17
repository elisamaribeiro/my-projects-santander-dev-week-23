# Desafio Python: O Grande Depósito

valor = float(input())

if valor > 0:
    saldo_formatado = "{:.2f}".format(valor).replace(',', '.')  # Formata o valor com 2 casas decimais e substitui ',' por '.'
    print("Deposito realizado com sucesso!\nSaldo atual: R$", saldo_formatado)
    
elif valor == 0:
    print("Encerrando o programa...")
   
else:
    print("Valor invalido! Digite um valor maior que zero.")

# Exemplo

valor = float(input(-100))

if valor > 0:
    saldo_formatado = "{:.2f}".format(valor).replace(',', '.')  # Formata o valor com 2 casas decimais e substitui ',' por '.'
    print("Deposito realizado com sucesso!\nSaldo atual: R$", saldo_formatado)
    
elif valor == 0:
    print("Encerrando o programa...")
   
else:
    print("Valor invalido! Digite um valor maior que zero.")

"Valor invalido! Digite um valor maior que zero."
