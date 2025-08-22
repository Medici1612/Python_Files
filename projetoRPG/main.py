import random
import time
import os
from abc import ABC, abstractmethod
from typing import List, Dict

# ================== CORES ==================
class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[91m"
    AZUL = "\033[94m"
    ROXO = "\033[95m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    NEGRITO = "\033[1m"

# ================== FUNÇÕES DE ESTILO ==================
def linha(tam=50, char="="):
    return f"{Cores.AMARELO}{char * tam}{Cores.RESET}"

def titulo(texto: str):
    borda = linha(len(texto) + 6, "=")
    return f"\n{borda}\n{Cores.NEGRITO}{Cores.VERDE}|| {texto.upper()} ||{Cores.RESET}\n{borda}"

def bloco(texto: str):
    linhas = texto.split("\n")
    return "\n".join([f"{Cores.CYAN}   > {l}{Cores.RESET}" for l in linhas])

def pausa(seg=1.5):
    time.sleep(seg)

# ================== ATRIBUTOS ==================
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

# ================== MÉTODOS DE DISTRIBUIÇÃO DE ATRIBUTOS ==================
class MetodoGeracao(ABC):
    @abstractmethod
    def gerar(self) -> Status:
        pass

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
            pausa(0.7)
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

# ================== PERSONAGEM ==================
class Personagem:
    def __init__(self, nome: str, metodo: MetodoGeracao):
        self.nome = nome
        self.atributos = metodo.gerar()

    def ficha(self):
        print(titulo(f"Ficha de {self.nome}"))
        print(bloco(self.atributos.resumo()))
        pausa(1)

# ================== MAIN ==================
def main():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        print(titulo("OLD DRAGON RPG"))
        print(titulo("CRIAÇÃO DE PERSONAGEM"))
        print("Escolha o método de distribuição de atributos:")
        print(f"{Cores.VERDE}1{Cores.RESET} - Clássico (3d6 em ordem)")
        print(f"{Cores.VERDE}2{Cores.RESET} - Aventureiro (3d6, escolha livre)")
        print(f"{Cores.VERDE}3{Cores.RESET} - Heróico (4d6, drop lowest)")
        print(f"{Cores.VERDE}4{Cores.RESET} - Sair")

        escolha = input("Opção: ").strip()
        if escolha == "4":
            print(f"{Cores.AMARELO}Até a próxima aventura!{Cores.RESET}")
            break
        elif escolha in ["1","2","3"]:
            nome = input("Nome do personagem: ").strip()
            if escolha == "1":
                metodo = MetodoClassico()
            elif escolha == "2":
                metodo = MetodoLivre()
            else:
                metodo = MetodoHeroico()

            p = Personagem(nome, metodo)
            p.ficha()
        else:
            print(f"{Cores.VERMELHO}Opção inválida!{Cores.RESET}")

if __name__ == "__main__":
    main()
