import os
os.system("cls || clear")

nota = 0

nota = float(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    print("\nA nota deve ser maior que 0 e menor que 10.")
    nota = float(input("Digite sua nota: "))

print(f"Nota: {nota}")




    