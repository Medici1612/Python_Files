import random
from typing import Dict, List
from .estilo import titulo, pausa
from .cores import Cores

class Status:
    def __init__(self, str_: int, dex: int, con: int, int_: int, wis: int, cha: int):
        self.str_ = str_
        self.dex = dex
        self.con = con
        self.int_ = int_
        self.wis = wis
        self.cha = cha

    @classmethod
    def from_dict(cls, valores: Dict[str, int]):
        return cls(
            str_=valores.get("Força", 0),
            dex=valores.get("Destreza", 0),
            con=valores.get("Constituição", 0),
            int_=valores.get("Inteligência", 0),
            wis=valores.get("Sabedoria", 0),
            cha=valores.get("Carisma", 0),
        )

    def resumo(self) -> str:
        return (
            f"Força        : {self.str_}\n"
            f"Destreza     : {self.dex}\n"
            f"Constituição : {self.con}\n"
            f"Inteligência : {self.int_}\n"
            f"Sabedoria    : {self.wis}\n"
            f"Carisma      : {self.cha}"
        )

# ================== Métodos de Geração ==================
class MetodoGeracao:
    def gerar(self) -> Status:
        raise NotImplementedError

class MetodoClassico(MetodoGeracao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1,6) for _ in range(3))

    def gerar(self) -> Status:
        print(titulo("Método Clássico - 3d6 em ordem"))
        pausa()
        valores = {
            "Força": self._rolar_3d6(),
            "Destreza": self._rolar_3d6(),
            "Constituição": self._rolar_3d6(),
            "Inteligência": self._rolar_3d6(),
            "Sabedoria": self._rolar_3d6(),
            "Carisma": self._rolar_3d6()
        }
        for k, v in valores.items():
            print(f"{Cores.VERDE}{k:<13}{Cores.RESET} -> {Cores.AMARELO}{v}{Cores.RESET}")
            pausa(0.6)
        return Status.from_dict(valores)

class MetodoLivre(MetodoGeracao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1,6) for _ in range(3))

    def gerar(self) -> Status:
        print(titulo("Método Aventureiro - escolha livre"))
        pausa()
        rolagens = [self._rolar_3d6() for _ in range(6)]
        return self._distribuir(rolagens)

    def _distribuir(self, valores: List[int]) -> Status:
        atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        escolhidos = {}
        print(f"\nSeus números são: {Cores.AZUL}{sorted(valores, reverse=True)}{Cores.RESET}\n")
        for atributo in atributos:
            print(f"Números disponíveis: {Cores.MAGENTA}{valores}{Cores.RESET}")
            while True:
                try:
                    escolha = int(input(f"Escolha um valor para {atributo}: "))
                    if escolha in valores:
                        escolhidos[atributo] = escolha
                        valores.remove(escolha)
                        break
                    else:
                        print(f"{Cores.VERMELHO}Valor inválido!{Cores.RESET}")
                except ValueError:
                    print(f"{Cores.VERMELHO}Digite apenas números!{Cores.RESET}")
        return Status.from_dict(escolhidos)

class MetodoHeroico(MetodoLivre):
    def _rolar_4d6_drop1(self) -> int:
        dados = [random.randint(1,6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)

    def gerar(self) -> Status:
        print(titulo("Método Heróico - 4d6 Drop Lowest"))
        pausa()
        rolagens = [self._rolar_4d6_drop1() for _ in range(6)]
        return self._distribuir(rolagens)
