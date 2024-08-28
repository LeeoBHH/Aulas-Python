import os
os.system("cls || clear")

print("""""
CÓDIGO  | PRATO      | VALOR
_______________________________     
   1    | picanha       25,06  |
   2    | lasanha       20,00  |
   3    | Strogonoff    18,00  |
   4    | Bife Aceb     15,00  |
   5    | Pão c Ovo     05,00  |
_______________________________|      
      """"") 

opcao = input("Digite o código do pedido: ")

match(opcao):
    case "1":
        print("""
Prato: Picanha.
Preço: RS: 25,00
              """)
    case "2":
        print("""
Prato: Lasanha.
Preço: R$: 20,00
              """)
    case "3":
        print("""
Prato: Strogonoff.
Preço: R$: 18,00
              """)
    case "4":
        print("""
Prato: Bife Acebolado.
Preço: R$: 15,00
              """)
    case "5":
        print("""
Prato: Pão com ovo.
Preço: R$: 05,00
              """)
        
