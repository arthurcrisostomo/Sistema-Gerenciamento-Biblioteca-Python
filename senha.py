
from interface import Interface

class Senha:
    def __init__(self):
        # > Define a senha correta de ADM
        self.senha_correta = '123'
        # > Define numero de tentativas
        self.tentativas = 3
        # > Instanciando a classe Inteface()
        self.interface = Interface()

    def verificar_senha(self):
        # > Enquanto self.tentativas for maior que 0 (3, 2, 1)
        while self.tentativas > 0:
            # > Imprime o modelo com as tentativas restantes
            self.interface.style_tentativas_senha_adm(self.tentativas)
            # > Captura a senha fornecida
            senha_informada = input(f'\033[1;38;2;101;67;33m⤷ 🔑\033[0m')

            # > Se a senha fornecida for igual a senha correta retorna True
            if senha_informada == self.senha_correta:
                return True
            # > Se chegar ate aqui não esta correta, diminui 1 tentativa
            self.tentativas -= 1
        # > Se não conseguir acertar retorna False
        return False
        
        
            