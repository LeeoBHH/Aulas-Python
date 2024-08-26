import os
os.system("cls || clear")
"""
 Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7. 
 Exiba esse número.
"""
# Começamos com o número 51, pois precisamos encontrar um número maior que 50.
numero = 51
# Laço while para encontrar o número divisivel por 7.
while numero % 7 != 0:
    numero = numero + 1
# Exiba o número encontrado.
print("O primeiro número maior que 50 divisivel por 7 é: ", numero)



