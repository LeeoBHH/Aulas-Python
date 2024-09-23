import os
os.system("cls || clear")

# Entrada.
lista_notas = []
soma = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) # Organiza a fila.
    
# Processamento.
soma = sum(lista_notas)
media = soma / 3

# Saída.
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}° Nota: {nota}") 
print(f"Média: {media}")