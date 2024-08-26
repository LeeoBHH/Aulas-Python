import os
os.system("cls || clear")

contador = 0
continua = 's'

while continua == 's':
    print("repetindo...")

    contador +=1
    # contador = contador + 1

    continua = input("Tecle 's' se deseja continuar:").strip().lower()
    #.strip = apaga a barra de espaço se clicada acidentalmente no terminal.
    #.lower = deixa o caracter minusculo mesmo se digitar em maiusculo.



if contador == 0:
    print(f"O bloco NAO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes")