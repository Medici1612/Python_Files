from .base import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", movimento=9, infravisao=True, alinhamento="Tendem à Neutralidade")

    def habilidades(self):
        return ("Percepção Natural: detecta portas secretas (1 em 1d6, ou 1-2 se procurando).\n"
                "Graciosos: +1 em testes de Destreza.\n"
                "Arma Racial: +1 no dano com arcos.\n"
                "Imunidades: sono mágico e paralisia de Ghoul.")
