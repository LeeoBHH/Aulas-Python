import os
os.system("cls || clear")
# CRUD
from dataclasses import dataclass

# Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_ALUNOS = 4
lista_de_clientes = []

for i in range(QUANTIDADE_ALUNOS):
    cliente = Cliente(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    lista_de_clientes.append(cliente)

# Salvar um arquivo chamado: carteira_de_clientes.txt
nome_do_arquivo = "carteira_de_clientes.txt"

# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal
with open(nome_do_arquivo, "a") as arquivo_clientes:
    # Percorrendo vetor/lista.
    for cliente in lista_de_clientes:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_clientes.write(f"{cliente.nome}, {cliente.sobrenome}, {cliente.idade}, {cliente.peso}, {cliente.altura}\n")

# Fechar conexão com o arquivo.
arquivo_clientes.close()

print("\n=== Dados dos clientes salvos com sucesso! ===")
for aluno in lista_de_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")