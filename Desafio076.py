lista = ('i30', 48.900, 'Hb20', 35.900, 'Stepway', 38.900)
print('-='*20)
print('LISTAGEM DE PREÇOS DOS VEÍCULOS')
print('-='*20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.3f}')
