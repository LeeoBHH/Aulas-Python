import os
os.system("cls || clear")


"""
escreva um algoritimo para ler 3 notas de um aluno.
caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.

"""

NOTAS = 3
soma = 0

for i in range(NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}º nota: "))
        if nota < 0 or nota > 10:
           print("A nota deve ser maior que 0 e menor que 10.")
        else:       
          soma = soma + nota
        break    
media = soma /2        

if media >= 7:
  print("Aprovado.")
elif media > 5 and media < 7:
  print("Recuperação.")
else:
  print("Reprovado.")
        

