# Importação dos módulos customizados do pacote Cadastro
from Cadastro.ficha.interface import titulo
from Cadastro.ficha.interface import menu
from Cadastro.ficha.telaconsulta import arquivoExiste
from Cadastro.ficha.telaconsulta import criarArquivo
from Cadastro.ficha.telaconsulta import lerArquivo
from Cadastro.ficha.interface import leiaint
from Cadastro.ficha.telacadastro import cadastrar
from Cadastro.ficha.telacadastro import leianome
from time import sleep

"""
Este script é o módulo principal do sistema. Ele gerencia o fluxo de execução,
verificando a existência do arquivo de dados e exibindo um menu interativo 
para consulta e cadastro de pessoas.
"""



#Programa Principal
# --- CONFIGURAÇÃO INICIAL DO BANCO DE DADOS ---
arq = 'cadastro.txt'
# Verifica se o arquivo de texto existe; caso contrário, cria um novo
if arquivoExiste(arq):
    print('Arquivo já existe')
else:
    print('\033[31mARQUIVO INEXISTENTE\033[m')
    criarArquivo(arq)


# --- LOOP PRINCIPAL DO SISTEMA ---
while True:
    # Exibe o menu principal e captura a opção escolhida pelo usuário
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resp == 1:
        # Opção 1: Listar pessoas salvas no arquivo
        titulo('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    else:
        if resp == 2:
            # Opção 2: Cadastrar uma nova pessoa
            titulo('NOVO CADASTRO')
            nome = leianome('Nome: ')
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
        else:
            if resp == 3:
                # Opção 3: Encerrar o programa
                titulo('SAINDO DO SISTEMA.....ATÉ LOGO!!!')
                break
            else:
                # Trata opções fora do intervalo (1, 2 ou 3)
                print('\033[31mErro! Digite uma opção válida!\033[m')
    # Pausa de 1 segundo para melhorar a experiência do usuário 
    sleep(1)