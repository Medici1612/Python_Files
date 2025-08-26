from abc import ABC, abstractmethod

class Classe(ABC):
    def __init__(self, nome, dado_vida, armaduras, armas):
        self.nome = nome
        self.dado_vida = dado_vida
        self.armaduras = armaduras
        self.armas = armas

    @abstractmethod
    def habilidades(self) -> str:
        pass
