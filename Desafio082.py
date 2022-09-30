lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar?[S/N] ')).upper().strip()
    if seguir == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os números digitados foram {lista}')
print(f'Os números pares da lista são {pares}')
print(f'Os números impares da lista são {impares}')
