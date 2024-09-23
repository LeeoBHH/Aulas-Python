"""
Informe o número da turma: 
Turma - 

Nome completo dos componentes.
1 - 
2 - 
"""


import os

# Limpa o terminal.
os.system("cls || clear") 

pedido = []
total = 0

# Escolhendo o prato.

while True:
    codigo = int(input("Insira o código do prato desejado: "))
    
    match codigo:

        case 1:
            pedido.append("Pão com ovo")
            total += 30
        case 2:
            pedido.append("Pizza")
            total += 25
        case 3:
            pedido.append("Danoninho")
            total += 5
        case 4:
            pedido.append("Frango desfiado")
            total += 35
        case 5:
            pedido.append("Banana")
            total += 4
        case 6:
            pedido.append("Sopa de letrinha")
            total += 22
        case 7:
            pedido.append("Salsicha com ovo")
            total += 18
        case _:
            print("Código inválido.")
            

# Forma de pagamento
    forma_pagamento = input("Escolha a forma de pagamento (à vista/cartão de crédito): ")
    if forma_pagamento == "à vista":
        total_final = total * 0.90  
        print(f"Desconto aplicado: R$ {total * 0.10:}")
    else:
        total_final = total * 1.10  
        print(f"Acréscimo aplicado: R$ {total * 0.10:}")
