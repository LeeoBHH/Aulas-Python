import os
os.system("cls || clear")

contador = 0

while True:
     login = input(f"Digite o login: ").lower().strip()
     senha = input(f"Digite sua senha: ").lower().strip()
     contador = contador + 1
    
     if login == "leo13" and senha == "1307":
        print("Bem vindo! ")
        break
     else:
        print("Acesso negado! ")
        print(f"Tentativa: {contador} \n")
        if contador == 3: 
           break
        