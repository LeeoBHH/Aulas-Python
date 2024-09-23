import os
os.system("cls || clear")

QUANTIDADE_NUMERO = 5
quantidade_pares_positivos = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
contador = 0
while True:
    numero = int(input(f"Digite os valores: "))
    contador += 1
    if numero % 2 == 0 and numero > 0:
        quantidade_pares_positivos += 1
    else:
        quantidade_impares += 1
    if numero > 0:
        quantidade_negativos += 1
    if numero == 0:
        break

print(f"A quantidade de números pares e positivos é: {quantidade_pares_positivos}")
print(f"A quantidade de números impares é: {quantidade_impares}")
print(f"A quantidade de números negativos é: {quantidade_negativos}")
print(f"A quantidade de números inseridos foi de: {contador}")

        
    

    



