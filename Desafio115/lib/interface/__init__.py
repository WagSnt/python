def leiaInt(msg):
    while True:
        try:                                                                             # tenta isso
            n = int(input(msg))
        except (ValueError, TypeError):                                                  # se não der, tenta isso
            print('\033[0;31mERRO: Por favor, digite um número válido.\033[m')
            continue                                                                     # retorna pro while para perguntar novamente
        except KeyboardInterrupt:
            print('\n\033[0;33mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:                                                                             # foi validado, finalizar
            return n


def linha(tam=42):                                                                        # linha para estética
    return '-' * tam


def cabeçalho(txt):                                                                       # cria o cabeçalho, para criação do título do mesmo
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):                                                                          # Onde irá ficar as opções do menu
    cabeçalho('MENU PRINCIPAL')
    c = 1                                                                                 # criar um contador
    for item in lista:                                                                    # para cada item na lista
        print(f'\033[1;97m{c}\033[m - \033[;34m{item}\033[m')                             # 'c' é o número da opção do menu e item é o nome da opção
        c += 1                                                                            # a cada item, aumenta a contagem
    print(linha())
    opc = leiaInt('\033[1;97mSua Opção:\033[m ')                                          # opc vai fazer a leitura da opção escolhida pelo usuário através da função 'leiaInt
    return opc                                                                            # retornar da função com a 'opc' selecionada
