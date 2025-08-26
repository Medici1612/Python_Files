from .base import Classe

class Clerigo(Classe):
    def __init__(self):
        super().__init__("Clérigo", "1d8", "Todas exceto armaduras pesadas", "Armas simples (sem corte)")

    def habilidades(self):
        return ("Conjura magias divinas (Sabedoria).\n"
                "Pode expulsar mortos-vivos.\n"
                "Restrição: não usa armas cortantes.")
