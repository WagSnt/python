pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r
for c in range (pt, decimo + r, r):
    print(f'{c}', end=' ')
