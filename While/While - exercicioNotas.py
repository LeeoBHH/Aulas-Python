import os
os.system("cls || clear")

soma = 0
NOTAS = 2

for i in range(NOTAS):
    nota = float(input(f"Digite a {i+1}º nota: "))
    while nota > 0 or nota < 10:
            break
            print("A nota tem que ser maior que 0 e menor que 10.")
    soma = soma + nota

        

media = soma / NOTAS
print(f"Nota: {soma}")
print(f"Média: {media}")

