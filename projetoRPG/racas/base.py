from abc import ABC, abstractmethod

class Raca(ABC):
    def __init__(self, nome, movimento, infravisao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    @abstractmethod
    def habilidades(self) -> str:
        pass
