import os
os.system("cls || clear")
"""
Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`.
"""
soma = 0


for i in range(1,10,2): 
    soma = soma + i    
    
print(soma)