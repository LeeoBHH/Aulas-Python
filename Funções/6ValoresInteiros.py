import os
os.system("cls || clear")
"""
Crie um algoritimo que aceite apenas 6 valores inteiros, positivos e pares,
em seguida, mostra na tela os valores lidos na ordem inversa.

Caso seja informado um número diferente dos critérios apresentadosa cima,
repita a pergunta para o usuário.
"""
import os
os.system("cls||clear")
QUANTIDADE = 6
numeros = []

def solicitar_numeros():
    for i in range(QUANTIDADE):
        while True:
            numero = int(input(f"Digite o {i+1}° número: "))

            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("Numero invalido. \nTente novamente.\n\n")

    return lista_pares_positivos
            

# Saída.
print("\n=== Solicitando dados ===")
for i, numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros)-1}° - {numero}")
    
