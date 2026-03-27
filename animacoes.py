    
import os
import time

def loading_saindo():
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        # .ljust(3) -> Mantem sempre o mesmo tamanho
        pontos = ('.' * i).ljust(10)
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║                   Saindo{pontos}          ║
            ╚═════════════════════════════════════════════╝
        \033[0m''')
        time.sleep(0.4)

def loading_adicionando_livro():
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        # .ljust(3) -> Mantem sempre o mesmo tamanho
        pontos = ('.' * i).ljust(13)
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║              Adicionando Livro{pontos} ║
            ╚═════════════════════════════════════════════╝
        \033[0m''')
        time.sleep(0.4)

def loading_alugando_livro():
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        # .ljust(3) -> Mantem sempre o mesmo tamanho
        pontos = ('.' * i).ljust(13)
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║              Alugando Livro{pontos}    ║
            ╚═════════════════════════════════════════════╝
        \033[0m''')
        time.sleep(0.4)

def loading_devolvendo_livro():
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        # .ljust(3) -> Mantem sempre o mesmo tamanho
        pontos = ('.' * i).ljust(13)
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║             Devolvendo Livro{pontos}   ║
            ╚═════════════════════════════════════════════╝
        \033[0m''')
        time.sleep(0.4)

def loading_removendo_livro():
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        # .ljust(3) -> Mantem sempre o mesmo tamanho
        pontos = ('.' * i).ljust(13)
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║               Removendo Livro{pontos}  ║
            ╚═════════════════════════════════════════════╝
        \033[0m''')
        time.sleep(0.4)