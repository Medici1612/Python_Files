from .base import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__("Halfling", movimento=6, infravisao=False, alinhamento="Tendem ao Bem")

    def habilidades(self):
        return ("Furtivos: chance de 1-2 em 1d6 para se esconder (+1 se ladrão).\n"
                "Destemidos: +1 em testes de Sabedoria.\n"
                "Bons de Mira: ataques com arremesso são fáceis.\n"
                "Pequenos: ataques de criaturas grandes são difíceis contra halflings.")
