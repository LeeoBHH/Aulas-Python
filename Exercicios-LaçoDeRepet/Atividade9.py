import os
os.system("cls || clear")
"""
 Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).
 """


linhas = 4
colunas = 6

# Laço externo para as linhas
for i in range(linhas):
    # Laço interno para as colunas
    for j in range(colunas):
        # Imprimir um asterisco sem pular linha
        print('*', end='')
    # Pular para a próxima linha após terminar a linha atual
    print()