import os
os.system("cls || clear")
"""
Crie funções que recebam 2 números e retorne a soma, subtração, divisão e a 
multiplicação destes 2 números.
"""

def somar(n1, n2):
    return (n1 + n2)

def subtrair(n1, n2):
    return n1 - n2

def  multiplicar(n1, n2):
    return n1 * n2

def  dividir(n1, n2):
    return n1 / n2 
    

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = somar(numero1, numero2)
subtracao = subtrair(numero1, numero2)
multiplicacao = multiplicar(numero1, numero2)
divisao = dividir (numero1, numero2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
