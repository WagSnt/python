from time import sleep


def numeros(*num):
    cont = maior = 0
    cont += 1
    print('Analisando os valores passados...')
    sleep(1)
    for v in num:
        print(f'{v}', end=', ')
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 30)



# Programa Principal
numeros(1, 2, 3)
numeros(3, 4, 6, 4, 8, 85)
numeros(9, 5, 9, 5, 3, 2, 9)
numeros()
print('PROGRAMA FINALIZADO')