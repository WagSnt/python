def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('   PROGRAMA DE TERRENOS   ')


def calculo(largura, comprimento):
    a = largura + comprimento
    print(f'A área de um terreno de {largura} por {comprimento} é de {a} m².')


l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
calculo(l, c)
