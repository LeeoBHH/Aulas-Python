import os
os.system("Clear || clear")

# Solicitando dados.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media: float
media = (nota1 + nota2 + nota3) / 3


if media > 7:
    resultado =("Aprovado!")
else:
    resultado =("Reprovado!")



print("\nExibindo Resultados: ")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")
print(f"Resultado: {resultado}")
