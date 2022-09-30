c = ('\033[m',       # 0 - SEM COR
     '\033[1;41m',   # 1 - VERMELHO
     '\033[1;107',   # 2 - BRANCO
     '\033[1;43m')


def ajuda(com):
    help(com)
    return com


def titulo(msg, cor=0):
    tam = len(msg + 4)
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
comando = ''
while True:
    comando = (str(input('Função ou Biblioteca: ')))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
