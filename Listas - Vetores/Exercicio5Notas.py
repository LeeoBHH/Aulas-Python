import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 5
lista_numeros = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}° número "))
    lista_numeros.append(numero)

# Processamento.
maior_numero = max(lista_numeros)
menor_numero = min (lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° nota: {nota}")

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")