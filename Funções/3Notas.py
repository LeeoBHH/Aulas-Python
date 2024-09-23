import os
os.system("cls || clear")

"""
Escreva um programa quer permita ler 3 notas de um aluno,
usando laço de repetução e informe por meio de uma função a média.
"""

for i in range(3):
    nota = float(input(f"Digite a {i+1}° nota: "))
    soma = soma + nota

def mediaAri(n3):
    media = soma / 3
    return media

media = mediaAri(nota)
print("A média é igual a: {media}")

    