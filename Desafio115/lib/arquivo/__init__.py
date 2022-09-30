from Desafio115.lib.interface import *


def arquivoExiste(nome):
    try: # tente
        a = open(nome, 'rt')                                                  # irá abrir um arquivo e ler
        a.close()                                                             # depois irá fechar o arquivo
    except FileNotFoundError:                                                 # se apresentar erro de arquivo não existente
        return False                                                          # retornar como false
    else:
        return True                                                           # se não, retornar como True (existe um arquivo)


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo "{nome}" criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')                                                 # tente abrir  e ler o arquivo
    except:
        print('Erro ao ler o arquivo')                                       # se não der certo, ....
    else: # se tudo der certo
        cabeçalho('PESSOAS CADASTRADAS')                                     # título do conteúdo do arquivo
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao tentar abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso')
        finally:
            a.close()
