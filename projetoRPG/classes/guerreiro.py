from .base import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__("Guerreiro", "1d10", "Todas", "Todas")

    def habilidades(self):
        return ("BA mais rápido, pode usar todas as armas e armaduras.\n"
                "Recebe ataques extras conforme evolui.")
