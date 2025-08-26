from .base import Classe

class Ladrao(Classe):
    def __init__(self):
        super().__init__("Ladrão", "1d6", "Leves", "Leves")

    def habilidades(self):
        return ("Furtividade, abrir fechaduras, detectar armadilhas.\n"
                "Ataque furtivo com dano extra ao surpreender inimigos.")
