import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º valor: "))
    
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")