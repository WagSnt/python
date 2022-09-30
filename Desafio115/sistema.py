from Desafio115.lib.interface import *
from Desafio115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'                                                                            # nome do arquivo

if not arquivoExiste(arq):                                                          # Se não tiver o arquivo com o nome criado obs: função criada em arquivo para ler
    criarArquivo(arq)                                                                               # criar arquivo obs: função está em arquivo

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])                   # resposta do usuário
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        while True:
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)                                                            # função cadastrar adicionando ao arq, o nome e idade
            seguir = ' '
            if seguir not in 'SN':
                seguir = str(input('Deseja cadastrar outra pessoa?[S/N] ')).strip().upper()[0]
                if seguir == 'N':
                    cabeçalho('RETORNANDO AO MENU PRINCIPAL...')
                    break
    elif resposta == 3:
        # Opção para sair do sistema
        cabeçalho('Finalizando o sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO: Digite uma opção válida.\033[m')                                   # para opções acima do número do menu.
    sleep(2)
print('Finalizado')
