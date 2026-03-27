from interface import Interface
from cadastrar import Cadastrar
import validacoes
import time

def main():
    # Instanciando Interface
    interface = Interface()

    # Status do sistema
    sistema_ativo = True

    while sistema_ativo:
        interface.menu()

        # Instanciando dentro do while para sempre atualizar as informações
        # sem precisar reiniciar o sistema
        cadastrar = Cadastrar()

        # Escolha do usuario
        user_opcao_menu = input('\033[38;2;222;184;135m⤷ \033[0m')
        
        match user_opcao_menu:
            case '1':
                cadastrar.adicionar_livro(interface)

            case '2':
                cadastrar.listar_livros(interface)

            case '3':
                cadastrar.buscar_livros(interface)

            case '4':
                cadastrar.alugar_livro(interface)

            case '5':
                cadastrar.devolver_livro(interface)

            case '6':
                cadastrar.remover_livro(interface)

            case '0':
                sistema_ativo = False
                
            case _:
                validacoes.opcao_invalida()
                time.sleep(1.5)

if __name__ == '__main__':
    main()