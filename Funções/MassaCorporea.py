import os
os.system("cls || clear")

"""
Escreva um programa que solicite ao utilizador o fornecimento
do seu peso em kg e da sua altura em M e a partir deles calcule
o índice de massa corpórea do utilizador.
"""

peso = float(input("Digite seu KG: "))
altura = float(input("Digite seus metros: "))

def indice_massa(peso, altura):
    imc = peso / (altura **2)
    return imc

imc = indice_massa(peso, altura)


def classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc > 18.5 and imc < 24.9:
        return "Peso normal"
    elif imc > 25 and imc < 29.9:
        return "Sobrepeso"
    elif imc > 30 and imc < 34.9:
        return "Obesidade I"
    elif imc > 35 and imc < 39.9:
        return "Obresidade II"
    else:
        return "Obesidade III"
    
imc = indice_massa(peso, altura)
elo = classificacao(imc)

print(f"Seu ELO é: {imc:.2f}")
print(f"Seu ranking é: {elo}")