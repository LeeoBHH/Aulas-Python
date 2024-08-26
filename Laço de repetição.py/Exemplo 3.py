import os
<<<<<<< HEAD
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





=======
import time
os.system("cls || clear")

print("Laço da repetição - For")
for i in range(1,90, 2): 
        print(f"Conteúdo da variável i = {i}")
        time.sleep(2) # Vai esperar 2 segundos.
        
print("=== FIM ===")
>>>>>>> 713a841 (Python)
