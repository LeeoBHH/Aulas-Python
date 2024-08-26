import os
os.system("cls || clear")

def media(n1, n2):
    mediaAri = (n1 + n2) / 2
    return mediaAri

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))

mediaAri = media(numero1, numero2)

print(f"Média: {mediaAri}")   
               