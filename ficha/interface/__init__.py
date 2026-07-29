def titulo(msg):

    print('-'*40)
    print(f'{msg}'.center(40))
    print('-'*40)


def menu(itens):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in itens:
        print(f'\033[33m{c} -\033[m \033[34m{item}\033[m')
        c = c + 1
    print('-'*40)
    op = leiaint('\033[32mSua opção: \033[m')
    return op


def leiaint(msg):
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
