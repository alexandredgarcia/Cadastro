from Cadastro.ficha.interface import titulo
from Cadastro.ficha.interface import menu
from Cadastro.ficha.telaconsulta import arquivoExiste
from Cadastro.ficha.telaconsulta import criarArquivo
from Cadastro.ficha.telaconsulta import lerArquivo
from Cadastro.ficha.interface import leiaint
from Cadastro.ficha.telacadastro import cadastrar
from Cadastro.ficha.telacadastro import leianome
from time import sleep

print('== DESAFIO 115 ==')
print('-'*20)

#Programa Principal
arq = 'cadastro.txt'
if arquivoExiste(arq):
    print('Arquivo já existe')
else:
    print('\033[31mARQUIVO INEXISTENTE\033[m')
    criarArquivo(arq)



while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resp == 1:
        titulo('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    else:
        if resp == 2:
            titulo('NOVO CADASTRO')
            nome = leianome('Nome: ')
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
        else:
            if resp == 3:
                titulo('SAINDO DO SISTEMA.....ATÉ LOGO!!!')
                break
            else:
                print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1)