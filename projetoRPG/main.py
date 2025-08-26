import os
from utils.estilo import titulo, Cores
from utils.atributos import MetodoClassico, MetodoLivre, MetodoHeroico
from racas.humano import Humano
from racas.elfo import Elfo
from racas.anao import Anao
from racas.halfling import Halfling
from classes.guerreiro import Guerreiro
from classes.clerigo import Clerigo
from classes.ladrao import Ladrao
from classes.mago import Mago
from personagem.personagem import Personagem

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(titulo("OLD DRAGON RPG"))
    nome = input("Nome do personagem: ")

    # Raça
    racas = {"1": Humano(), "2": Elfo(), "3": Anao(), "4": Halfling()}
    print(titulo("Escolha a Raça"))
    for k, v in racas.items():
        print(f"{Cores.VERDE}{k}{Cores.RESET} - {v.nome}")
    raca = racas.get(input("Raça: "), Humano())

    # Classe
    classes = {"1": Guerreiro(), "2": Clerigo(), "3": Ladrao(), "4": Mago()}
    print(titulo("Escolha a Classe"))
    for k, v in classes.items():
        print(f"{Cores.VERDE}{k}{Cores.RESET} - {v.nome}")
    classe = classes.get(input("Classe: "), Guerreiro())

    # Método de atributos
    print(titulo("Método de Atributos"))
    print("1 - Clássico | 2 - Aventureiro | 3 - Heróico")
    escolha = input("Opção: ")
    metodo = MetodoClassico() if escolha == "1" else MetodoLivre() if escolha == "2" else MetodoHeroico()

    # Criar personagem
    p = Personagem(nome, raca, classe, metodo)
    p.ficha()

if __name__ == "__main__":
    main()
