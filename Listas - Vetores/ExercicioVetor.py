import os
os.system("cls || clear")

# Entrada.
lista_notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) # Organiza a fila.

# Saída.
for nota in lista_notas:
    print(f"Nota: {nota}") 