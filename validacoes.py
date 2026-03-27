
def opcao_invalida():
    print('Opção Invalida. Tente novamente!')

def validar_campos_cadastro(campo, resposta):
    # > Verifica se o campo é vazio
    if not resposta.strip():
        return 'Falha ao Adicionar Livro, [Campo Vazio]'
    
    # > Verifica se o campo ano não é texto
    if campo == 'ano':
        if not resposta.isdigit():
            return 'Falha ao Adicionar Livro, [Dado Invalido]'

    # > Verifica se o campo genero não é numero
    if campo == 'genero':
        if resposta.isdigit():     
            return 'Falha ao Adicionar Livro, [Dado Invalido]'

    return None   

def verificar_exibicao(resposta):
    if not resposta.strip():
        return 'Falha, [Campo Vazio]'

    if resposta != '0':
        return 'Falha, [Dado Invalido]'
    
def verificar_busca_livros(resposta, livros_encontrados):
    if not resposta:
        return 'Falha ao Buscar Livro, [Campo Vazio]'

    if not livros_encontrados:
        return '    Nenhum livro foi encontrado     '

def validar_campo_alugar(resposta, planilha):
    if not resposta.strip():
        return ' Falha ao Adicionar Livro, [Campo Vazio]'
    
    for linha in range(2, planilha.max_row + 1):
        titulo = planilha[f'A{linha}'].value
        
        if resposta == titulo:
            return None

    return '  Livro não foi encontrado para alugar'    
    
def validar_livros(planilha):
    disponiveis = 0
    for linha in range(2, planilha.max_row + 1):
        if planilha[f'E{linha}'].value == 'Disponível':
            disponiveis += 1

    if disponiveis == 0:
        return '  Não há nenhum livro para ser alugado'
    
    return None

def validar_livros_listar(planilha):
    disponiveis = 0
    for linha in range(2, planilha.max_row + 1):
        if planilha[f'A{linha}'].value:
            disponiveis += 1

    if disponiveis == 0:
        return '  Não há nenhum livro para ser listado'
    
    return None

def validar_livros_alugados(planilha):
    disponiveis = 0

    for linha in range(2, planilha.max_row + 1):
        if planilha[f'E{linha}'].value == 'Alugado':
            disponiveis += 1
    
    if disponiveis == 0:
        return ' Não há nenhum livro para ser devolvido'

    return None

def validar_livros_remover(planilha):
    livros_disponiveis = 0

    for linha in range(2, planilha.max_row + 1):
        if planilha[f'A{linha}'].value:
            livros_disponiveis += 1
    
    if livros_disponiveis == 0:
        return '  Não há nenhum livro para ser removido'

    return
    
def validar_campo_remocao(resposta, planilha):
    if not resposta.strip():
        return '  Falha ao Remover Livro, [Campo Vazio]'
    
    for linha in range(2, planilha.max_row + 1):
        titulo = planilha[f'A{linha}'].value

        if titulo == resposta:
            return
    return '  Livro não foi encontrado para remoção'


def validar_campo_busca(planilha):
    livros_disponiveis = 0

    for linha in range(2, planilha.max_row + 1):
        if planilha[f'A{linha}'].value:
            livros_disponiveis += 1
    
    if livros_disponiveis == 0:
        return 'Não há nenhum livro para ser buscado'

    return

    

