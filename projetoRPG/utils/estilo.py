import time
from .cores import Cores

def linha(tam=50, char="="):
    return f"{Cores.AMARELO}{char * tam}{Cores.RESET}"

def titulo(texto: str):
    borda = linha(len(texto) + 6, "=")
    return f"\n{borda}\n{Cores.NEGRITO}{Cores.VERDE}|| {texto.upper()} ||{Cores.RESET}\n{borda}"

def bloco(texto: str):
    linhas = texto.split("\n")
    return "\n".join([f"{Cores.CYAN}   > {l}{Cores.RESET}" for l in linhas])

def pausa(seg=1.0):
    time.sleep(seg)
