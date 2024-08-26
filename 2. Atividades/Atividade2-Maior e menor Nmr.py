import os
os.system("Clear || clear")

# Solicitando dados.
numero1 = float(input("Primeiro valor: "))
numero2 = float(input("Segundo valor: "))
soma = numero1 + numero2
media = soma / 2
multiplicacao = numero1 * numero2

if numero1 > numero2:
    print("O maior valor é o primeiro: ")
else:
    print("o maior valor é o segundo: ")

#Exibindo resultados.
print("\nExibindo resultados: ")
print(f"A soma dos valores é igual a: {soma}")
print(f"A média dos valores é igual a: {media}")
print(f"A multiplicação dos valores é igual a: {multiplicacao}")






