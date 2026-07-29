"""
Módulo de Cadastro de Pessoas

Contém funções para validação de nomes via expressão regular (Regex)
e salvamento/gravação de registros em arquivos de texto.
"""

import re

def cadastrar(arquivo, nome='desconhecido', idade=0):
    """
        Cadastra uma nova pessoa adicionando seu nome e idade ao arquivo de texto.

        Os dados são salvos no formato "Nome;Idade" em uma nova linha.

        :param arquivo: Caminho ou nome do arquivo .txt onde os dados serão armazenados.
        :param nome: Nome da pessoa a ser cadastrada (padrão: 'desconhecido').
        :param idade: Idade da pessoa a ser cadastrada (padrão: 0).
    """
    try:
        # Abre o arquivo para adição de texto ('at' = append text)
        a = open(arquivo, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo.\033[m')
    else:
        try:
            # Grava o nome e a idade separados por ponto e vírgula
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
        finally:
            # Garante que o arquivo seja fechado após a tentativa de gravação
            a.close()






def leianome(msg):
    """
        Solicita e valida o nome digitado pelo usuário.

        Usa expressões regulares (Regex) para garantir que o nome contenha
        apenas letras (incluindo caracteres acentuados) e espaços em branco.

        :param msg: Mensagem de prompt para ser exibida no terminal.
        :return: Retorna o nome validado em formato string ou 'desconhecido' se interrompido.
    """
    n = str(input(msg)).strip()
    while True:
        try:
            if n == '':
                print('\033[31mErro! Digite um nome válido.\033[m')
                n = str(input(msg)).strip()
            else:
                # Expressão regular para validar letras de A-Z, acentos e espaços
                padrao = r'^[a-zA-ZáàâãéèêíïóôõöúçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ\s]+$'
                # Valida se a string 'n' atende ao padrão da regex
                if re.match(padrao, n):
                    return n
                    break
                else:
                    print('\033[31mErro! Digite um nome válido.\033[m')
                    n = str(input(msg)).strip()
        except (ValueError,TypeError):
            print('\033[31mErro! Digite um nome válido.\033[m')
            n = str(input(msg)).strip()
        except KeyboardInterrupt:
            # Captura a interrupção via teclado (Ctrl + C)
            print('\033[31mUsuário preferiu não informar o campo nome.\033[m')
            return 'desconhecido'





