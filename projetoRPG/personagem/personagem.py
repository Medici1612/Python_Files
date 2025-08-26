from utils.estilo import titulo, bloco, pausa, Cores

class Personagem:
    def __init__(self, nome, raca, classe, metodo):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = metodo.gerar()

    def ficha(self):
        print(titulo(f"Ficha de {self.nome}"))
        print(bloco(self.atributos.resumo()))
        print(f"\n{Cores.AMARELO}Raça:{Cores.RESET} {self.raca.nome}")
        print(f"Alinhamento: {self.raca.alinhamento}")
        print(f"Movimento: {self.raca.movimento}m")
        print(f"Infravisão: {'Sim' if self.raca.infravisao else 'Não'}")
        print(f"Habilidades Raciais:\n{bloco(self.raca.habilidades())}\n")
        print(f"{Cores.AMARELO}Classe:{Cores.RESET} {self.classe.nome}")
        print(f"Dado de Vida: {self.classe.dado_vida}")
        print(f"Armaduras: {self.classe.armaduras}")
        print(f"Armas: {self.classe.armas}")
        print(f"Habilidades de Classe:\n{bloco(self.classe.habilidades())}")
        pausa(2)
