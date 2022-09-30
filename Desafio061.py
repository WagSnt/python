pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 0
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += r
    cont += 1
print('FIM!')
