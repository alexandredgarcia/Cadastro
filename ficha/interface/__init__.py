"""
Módulo de Interface do Usuário

Contém funções utilitárias para exibição de cabeçalhos,
formatação de menus no terminal e validação de dados de entrada.

"""

def titulo(msg):
    """
        Exibe um título formatado e centralizado entre duas linhas divisórias.

        :param msg: Texto que será exibido no título.
    """
    print('-'*40)
    print(f'{msg}'.center(40))
    print('-'*40)


def menu(itens):
    """
        Gera um menu de opções dinâmico e colorido a partir de uma lista de itens.

        :param itens: Lista de strings contendo as opções do menu.
        :return: Retorna a opção inteira escolhida pelo usuário.
        """
    titulo('MENU PRINCIPAL')
    c = 1
    for item in itens:
        # Exibe o número em amarelo e o texto da opção em azul
        print(f'\033[33m{c} -\033[m \033[34m{item}\033[m')
        c = c + 1
    print('-'*40)
    op = leiaint('\033[32mSua opção: \033[m')
    return op


def leiaint(msg):
    """
        Lê um número inteiro digitado pelo usuário com tratamento de exceções.

        Continua solicitando a entrada até que um número válido e maior que zero seja fornecido.
        Trata erros de digitação de texto e interrupção forçada pelo usuário.

        :param msg: Mensagem de prompt exibida para o usuário.
        :return: Retorna o número inteiro validado ou 0 caso o usuário interrompa.
    """
    while True:
        try:
            verificarinteiro = int(input(msg).strip())
            if verificarinteiro <= 0:
                print('\033[31mErro! Digite uma opção válida!\033[m')
            else:
                return verificarinteiro
        except(ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido!\033[m')
        except(KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar a opção!\033[m')
            return 0
