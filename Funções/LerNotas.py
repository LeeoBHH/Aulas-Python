import os
os.system("cls || clear")

"""
Escreva um programa que permita ler 2 notas de um aluno e:
- Informe por meio de uma função a média;
- Informe por meio de uma função se a media for maior ou igual a 7, o aluno está aprovado.
caso contrario, estará reprovado.
"""

def media(n1, n2):
    mediaAri = (n1 + n2) / 2
    return mediaAri

def resultado(media):
    if media >= 7:        
        return "Aprovado."   
    else:
        return "Reprovado."

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

mediaAri = media(nota1, nota2)
status = resultado(mediaAri)


def resultado(media):
    if media >= 7:
        print("Você está aprovado.")
        return resultado   
    if media <= 7:
        print("Você está reprovado. ")
        return resultado    


print(f"Sua média é: {mediaAri} ")
print(f"O resultado é: {status} ")