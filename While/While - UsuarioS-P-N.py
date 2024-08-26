import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador = contador + 1
    soma = soma + nota
    media = soma / contador
    
    resposta = input("Deseja inserir mais uma nota? ").upper()

    if resposta == "P":
        print(f"Quantidade de notas inseridas: {contador}")
    if resposta == "N":
        print(f"A média das notas é {media}")
        break