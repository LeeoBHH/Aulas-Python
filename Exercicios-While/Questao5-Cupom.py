import os
os.system("cls || clear")
"""
Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto. 
O código correto é "PROMO2024". O usuário tem 3 tentativas para acertar o código. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto. 
Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de "Código inválido".
"""
promocao = "PROMO2024"
contador = 0

while True:
    codigo = input("Digite o código do cupom de promoção: ")
    if codigo == promocao:
        print("Código aceito.")
    else:
        contador = contador + 1
        print(f"tentativa {contador}")
    if contador >= 3:
        print("codigo invalido")
        break