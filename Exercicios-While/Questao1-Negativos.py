import os
os.system("cls || clear")
"""
 Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. 
 O programa deve parar quando o usuário inserir 0 ou um número positivo. Mostre a quantidade de números negativos.
 """

numero = 0
contador = 0

while True:
    numero = int(input("Digite um número negativo: "))
    if numero < 0:
        contador = contador + 1
    else:
        print(f"Números negativos digitados: {contador}")
        break


