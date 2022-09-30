lista = [[], []]
for v in range(0, 7):
    num = int(input('Digite um valor: '))
    if v % 2 == 0:
        lista[0].append(v)
    elif v % 2 == 1:
        lista[1].append(v)
lista.sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')
