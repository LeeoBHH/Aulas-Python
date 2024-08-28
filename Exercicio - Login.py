import os
os.system("cls || clear")

while True:
    login = input(f"Digite o login: ").lower().strip()
    senha = input(f"Digite sua senha: ").lower().strip()
    
    if login == "leo13" and senha == "1307":
        print("Bem vindo! ")
        break
    else:
        print("Acesso negado! ")