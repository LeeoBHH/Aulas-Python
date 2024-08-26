import os

os.system("cls || clear")

media = 0
soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}º nota: "))
    soma = soma + nota

media = soma / 3

print(f"Média: {media}")


if media >= 7:
    print("O aluno esta aprovado.")

if media < 4 and media > 4:
    print("O aluno esta de recuperação. ")

if media < 7:
    print("O aluno está reprovado. ")



