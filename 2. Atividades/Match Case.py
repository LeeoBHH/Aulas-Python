import os
os.system("Clear || clear")

print("""
(+) para soma
(-) para subtração
(*) para multiplicacao
(/) para divisao
      """)

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
opcao = input("Escolha a operação: ")

match(opcao):
    case "+":
        resultado = valor1 + valor2
    case "-":
        resultado = valor1 - valor2
    case "*":
        resultado = valor1 * valor2
    case "/":
        resultado = valor1 * valor2


print(f"O resultado dos valores é igual a: {resultado}" )

