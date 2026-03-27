import os
import time

class Interface:
    def __init__(self):
        self.limpar_tela()

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        self.limpar_tela()
        print(f'''\033[1;38;2;210;180;140m                                                                            
              ,,  ,,                                                                     
`7MMF'        db *MM                                            .M"""bgd                 
  MM              MM                                           ,MI    "Y                 
  MM        `7MM  MM,dMMb.`7Mb,od8 ,6"Yb.  `7Mb,od8 `7M'   `MF'`MMb.  `7M'   `MF',pP"Ybd 
  MM          MM  MM    `Mb MM' "'8)   MM    MM' "'   VA   ,V    `YMMNq.VA   ,V  8I   `" 
  MM      ,   MM  MM     M8 MM     ,pm9MM    MM        VA ,V   .\033[1;38;2;101;67;33m     `MM VA ,V   `YMMMa. 
  MM     ,M   MM  MM.   ,M9 MM    8M   MM    MM         VVV    Mb     dM  VVV    L.   I8 
.JMMmmmmMMM .JMML.P^YbmdP'.JMML.  `Moo9^Yo..JMML.       ,V     P"Ybmmd"   ,V     M9mmmP' 
                                                       ,V                ,V              
                                                    OOb"              OOb"\033[0m
        \033[38;2;222;184;135m╔═════════════════════════════════════╗\033[0m           
        \033[38;2;222;184;135m║     📔 SISTEMA DE BIBLIOTECA 📔     ║ \033[0m
        \033[38;2;222;184;135m╠═════════════════════════════════════╣     
        \033[38;2;222;184;135m║  1 🔁 Cadastrar Livro [ADMIN]       ║   #####################################\033[0m
        \033[38;2;222;184;135m║  2 📚 Listar Livros                 ║    📄\033[0m\033[1;37mPython + Excel \033[0m            
        \033[38;2;222;184;135m║  3 🔍 Buscar Livro                  ║    </> \033[0m\033[1;37marthur.dev \033[0m  
        \033[38;2;222;184;135m║  4 🤚 Alugar Livro                  ║    🖂 \033[0m\033[1;37m arthur.dev.crisostomo@gmail.com \033[0m
        \033[38;2;222;184;135m║  5 🗳️  Devolver Livro                ║   #####################################\033[0m\033[0m 
        \033[38;2;222;184;135m║  6 🚫 Remover Livro [ADMIN]         ║\033[0m
        \033[38;2;222;184;135m╠═════════════════════════════════════╣\033[0m
        \033[38;2;222;184;135m║  0 ⤵ Sair                           ║\033[0m     
        \033[38;2;222;184;135m╚═════════════════════════════════════╝\033[0m     
        \033[0m''')
    
    def style_erro_cadastro(self, mensagem):
        self.limpar_tela()
        self.style_aviso_adicionar_encerrar()
        if 'Campo Vazio' in mensagem:
            print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║   {mensagem.ljust(42)}║
            ╚═════════════════════════════════════════════╝\033[0m''')
        else:
            print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║  {mensagem.ljust(43)}║
            ╚═════════════════════════════════════════════╝\033[0m''')
        
    def style_cadastro_concluido(self):
        self.limpar_tela()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║        Livro Adicionado com Sucesso!        ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)

    def style_listar_encerrar(self):
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║          📚 LIVROS DA BIBLIOTECA 📚         ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ═══════════════════════════════════════════════════════
        \033[0m''')

    def style_exibir_erro_listar(self, mensagem):
        self.limpar_tela()
        self.style_listar_encerrar()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║  {mensagem}     ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)

    def style_exibir_livros(self, livros):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║          📚 LIVROS DA BIBLIOTECA 📚         ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ═══════════════════════════════════════════════════════
        \033[0m''')
    
        for titulo, autor, ano, genero, disponibilidade in livros:
            print(f'''\033[1;38;2;101;67;33m
                ╔══════════════════════════════════════╗
                ║ 📖 Livro: {titulo.ljust(27)}║
                ║ ✍️  Autor: {autor.ljust(27)}║
                ║ 📅 Ano: {ano.ljust(29)}║
                ║ 🎭 Gênero: {genero.ljust(26)}║
                ║ ☑  Disponibilidade: {disponibilidade.ljust(17)}║
                ╚══════════════════════════════════════╝
            \033[0m''')

    def style_aviso_adicionar_encerrar(self):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║             📚 ADICIONAR LIVRO 📚           ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ══════════════════════════════════════════════════════
        \033[0m''')
    
    def style_aviso_encerrar_busca(self):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║             📚 BUSCAR LIVRO 📚              ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ═══════════════════════════════════════════════════════
        \033[0m''') 

    def style_exibir_erro_busca(self, mensagem):
        self.limpar_tela()
        self.style_aviso_encerrar_busca()

        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║     {mensagem}    ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)


    def style_senha_adm(self):
        self.limpar_tela()

    def style_tentativas_senha_adm(self, tentativas):
        self.limpar_tela()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║    🛡️ Informe a Senha de Administrador 🛡️     ║
            ║            \033[1;38;2;101;67;33mTentativas Restantes {tentativas}\033[0m{" " * 11}║
            ╚═════════════════════════════════════════════╝
        \033[0m''')

    def style_livro_alugado_concluido(self):
        self.limpar_tela()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║          Livro Alugado com Sucesso!         ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(1.5)
    
    def style_aviso_encerrar_alugamento(self):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║              📚 ALUGAR LIVRO 📚             ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ═══════════════════════════════════════════════════════
        \033[0m''') 

    def style_exibir_livros_disponiveis(self, livros):
        self.limpar_tela()
        self.style_aviso_encerrar_alugamento()
    
        for titulo, autor, ano, genero, disponibilidade in livros:
            print(f'''\033[1;38;2;101;67;33m
                ╔══════════════════════════════════════╗
                ║ 📖 Livro: {titulo.ljust(27)}║
                ║ ✍️  Autor: {autor.ljust(27)}║
                ║ 📅 Ano: {ano.ljust(29)}║
                ║ 🎭 Gênero: {genero.ljust(26)}║
                ║ ☑  Disponibilidade: {disponibilidade.ljust(17)}║
                ╚══════════════════════════════════════╝
            \033[0m''')

    def style_aviso_encerrar_devolver(self):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║             📚 DEVOLVER LIVRO 📚            ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ══════════════════════════════════════════════════════
        \033[0m''')

    def exibir_livros(self, livros):
        for titulo, autor, ano, genero, disponibilidade in livros:
            print(f'''\033[1;38;2;101;67;33m
                ╔══════════════════════════════════════╗
                ║ 📖 Livro: {titulo.ljust(27)}║
                ║ ✍️  Autor: {autor.ljust(27)}║
                ║ 📅 Ano: {ano.ljust(29)}║
                ║ 🎭 Gênero: {genero.ljust(26)}║
                ║ ☑  Disponibilidade: {disponibilidade.ljust(17)}║
                ╚══════════════════════════════════════╝
            \033[0m''')

    def style_exibir_erro_busca(self, mensagem):
        self.limpar_tela()
        self.style_aviso_encerrar_busca()

        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║     {mensagem}    ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)

    def style_erro_alugar(self, mensagem):
        self.limpar_tela()
        self.style_aviso_encerrar_alugamento()

        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║  {mensagem.ljust(40)}   ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)

    def style_erro_devolver(self, mensagem):
        self.limpar_tela()
        self.style_aviso_encerrar_alugamento()

        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║  {mensagem.ljust(40)}   ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)

    def style_livro_devolvido_concluido(self):
        self.limpar_tela()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║         Livro Devolvido com Sucesso!        ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(1.5)

    def style_aviso_encerrar_remover(self):
        self.limpar_tela()
        print('''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║             📚 REMOVER LIVRO 📚             ║
            ╠═════════════════════════════════════════════╣
            ║  0 ⤵ Sair                                   ║
            ╚═════════════════════════════════════════════╝
        ═══════════════════════════════════════════════════════
        \033[0m''')

    def style_livro_removido_sucesso(self):
        self.limpar_tela()
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║         Livro Removido com Sucesso!         ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(1.5)

    def style_erro_remover(self, mensagem):
        print(f'''\033[38;2;222;184;135m
            ╔═════════════════════════════════════════════╗
            ║  {mensagem}    ║
            ╚═════════════════════════════════════════════╝\033[0m''')
        time.sleep(2)
        
        
        