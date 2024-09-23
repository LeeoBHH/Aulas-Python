import os
os.system("cls || clear")

# Entrada.
lista_notas = []
QUANTIDADE_NOTAS = 4
soma = 0

for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota: "))
    lista_notas.append(nota) # Organiza a fila.
    
# Processamento.
soma = sum(lista_notas)
media = soma / 4

# Saída.
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}° Nota: {nota}") 
print(f"Média: {media}")

if media >= 7:
    print("Aprovado.")
elif media > 5 or media > 7:
    print("Recuperação.")
else:
    print("Reprovado.")