import random

def inicio():
    print("Bem-vindo ao jogo 'Cideney e as Bananas'!")
    print("Cideney é um macaco que adora bananas.")
    print("Ajude Cideney a coletar bananas na floresta!")
    
    bananas = 0
    while True:
        print(f"\nCideney tem {bananas} banana(s).")
        escolha = input("Você quer (1) procurar bananas ou (2) descansar? ")

        if escolha == "1":
            bananas += procurar_bananas()
        elif escolha == "2":
            print("Cideney descansou e recuperou energia.")
        else:
            print("Escolha inválida. Tente novamente.")

        if bananas >= 10:
            print("\nParabéns! Cideney coletou 10 bananas e venceu!")
            break

def procurar_bananas():
    print("Cideney está procurando bananas...")
    resultado = random.choice(["bananas", "obstáculo", "nada"])

    if resultado == "bananas":
        quantidade = random.randint(1, 3)
        print(f"Cideney encontrou {quantidade} banana(s)! Yum!")
        return quantidade
    elif resultado == "obstáculo":
        print("Cideney esbarrou em um obstáculo e perdeu tempo!")
        return 0
    else:
        print("Cideney não encontrou nada. Vamos tentar de novo!")
        return 0

if __name__ == "__main__":
    inicio()
