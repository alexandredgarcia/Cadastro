"""
Módulo de Consulta e Gerenciamento de Arquivo

Contém funções para verificação de existência, criação e leitura/formatação
dos dados armazenados no arquivo de texto.
"""

def arquivoExiste(arquivo):
    """
        Verifica se um arquivo de texto já existe no diretório do projeto.

        :param arquivo: Caminho ou nome do arquivo a ser verificado.
        :return: Retorna True se o arquivo existir, ou False caso não exista.
    """
    try:
        # Tenta abrir o arquivo no modo leitura de texto ('rt')
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        # Retorna Falso caso o sistema operacional informe que o arquivo não existe
        return False
    else:
        return True


def criarArquivo(arquivo):
    """
        Cria um novo arquivo de texto vazio para ser utilizado como banco de dados.

        :param arquivo: Nome do arquivo a ser criado (ex: 'cadastro.txt').
    """
    try:
        # Modo 'wt+' abre o arquivo para escrita e criação, apagando conteúdo anterior se houver
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!!!')


def lerArquivo(arquivo):
    """
        Lê os dados do arquivo de texto e exibe na tela uma listagem
        formatada em colunas com Nome e Idade.

        :param arquivo: Nome do arquivo de onde os dados serão lidos.
    """
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo...')
    else:
        # Percorre cada linha presente no arquivo
        for linha in a:
            # Separa o nome da idade usando o ';' como delimitador
            dado = linha.split(';')
            # Remove a quebra de linha (\n) do final da idade
            dado[1] = dado[1].replace('\n','')
            # Exibe o nome alinhado à esquerda (30 caracteres) e a idade
            print(f'{dado[0]:<30} {dado[1]:<2} anos')
        print(a.read())
    finally:
        # Garante o fechamento do arquivo independente de erros durante a leitura
        a.close()
