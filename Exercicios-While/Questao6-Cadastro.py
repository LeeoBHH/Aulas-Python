import os
os.system("cls || clear")
"""
Crie um programa que ajude um estudante a calcular a média de suas notas. 
O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo. 
O programa deve calcular e exibir a média das notas inseridas.
"""
soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota > 0:
        contador = contador + 1
        soma = soma + nota
    else:
        if nota < 0:
            break


media = soma / contador
print(f"Média: {media}")