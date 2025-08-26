from .base import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__("Mago", "1d4", "Nenhuma", "Adagas, cajados, dardos")

    def habilidades(self):
        return ("Conjura magias arcanas (Inteligência).\n"
                "Grande conhecimento arcano.\n"
                "Muito frágil em combate físico.")
