import os
os.system("cls ||clear")

print("""
Dias da semana.
      
1 - Domingo
2 - Segunda-feira
3 - Terça-feira
4 - Quarta-feira
5 - Quinta-feira
6 - Sexta-feira
7 - Sabádo
""")

dia = int(input("Digite o número: "))

match(dia):
    case 1:
        print("Final de semana!")
    case 2:
        print("Dia útil.")
    case 3:
        print("Dia útil.")
    case 4:
        print("Dia útil.")
    case 5:
        print("Dia útil.")
    case 6:
        print("Dia útil.")
    case 7:
        print("Final de semana!")
    case _:
        print("inválido.")
  
          
