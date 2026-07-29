import re
def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()






def leianome(msg):
    n = str(input(msg)).strip()
    while True:
        try:
            if n == '':
                print('\033[31mErro! Digite um nome válido.\033[m')
                n = str(input(msg)).strip()
            else:
                padrao = r'^[a-zA-ZáàâãéèêíïóôõöúçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ\s]+$'
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
            print('\033[31mUsuário preferiu não informar o campo nome.\033[m')
            return 'desconhecido'





