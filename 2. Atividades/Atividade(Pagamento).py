import os
os.system("cls || clear")

#Solicitando dados.
parcela: int
desconto: float



valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = str(input("Digite a forma de pagamento: "))
desconto = valor_produto * 0.10

if forma_pagamento == 1:
    valor_produto - desconto
    
if forma_pagamento == 2:
    parcela = int(input("Digite a quantidade de parcelas (Digite de 2 a 6 para escolher): "))

match(forma_pagamento):
    case "1":
        desconto = valor_produto * 0.10
        preco_final = valor_produto - desconto

        print(f"\nValor do produto: R$ {valor_produto}")
        print(f"Forma de pagamento selecionada foi a vista.")
        print(f"Valor do desconto: R$ {preco_final}")
 

        


