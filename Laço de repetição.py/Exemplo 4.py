import os
import time
os.system("cls || clear")

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma = soma + numero
    time.sleep(2)


print(f"Resultado: {soma}")



