import os
os.system("cls || clear")

"""
Crie um programa que ajude um usuário a controlar seus gastos mensais.
O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. 
O programa deve exibir o total gasto e o valor  excedente.
"""
gasto_total = 0
orcamento = float(input("Digite o orçamento: "))

while True:
    gasto_diario = float(input("Digite o gasto diario: "))
    gasto_total = gasto_total + gasto_diario

    if gasto_total > orcamento:
        print("Gasto total maior que orçamento")
        break
    else:
        print(f"O valor excedente foi de: {orcamento - gasto_total}")