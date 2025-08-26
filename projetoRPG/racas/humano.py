from .base import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", movimento=9, infravisao=False, alinhamento="Qualquer")

    def habilidades(self):
        return ("Aprendizado: +10% em toda XP recebida.\n"
                "Adaptabilidade: +1 em uma Jogada de Proteção à escolha.")
