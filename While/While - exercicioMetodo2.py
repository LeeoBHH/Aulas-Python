import os
os.system("cls || clear")

nota = 0

nota = float(input("Digite sua nota: "))

while True:
    nota = float(input("Digite sua nota: "))

    if nota < 0 or nota > 10:
        print("A nota deve sr maior ou igual a 0 e menor ou igual a 10.")
    else:
        break # Para o laço de repetição.

print(f"Nota: {nota}")