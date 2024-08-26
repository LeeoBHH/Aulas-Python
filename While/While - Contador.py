import os
os.system("cls || clear")
""""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais
uma nota, se a resposta di usuário for “N”, o programa fará a média
aritmética das notas informadas e mostrará a média aritmética para o
usuario
Obs.: Use um contador dentro do laço de repetição para contar a
quantidade de iterações (loops).
"""
soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador = contador + 1
    soma = soma + nota
    
    resposta = input("Deseja inserir mais uma nota? ").upper()

    if resposta == "QUERO NAO!!!":
        break

media = soma / contador
print(f"Média: {media}")
    