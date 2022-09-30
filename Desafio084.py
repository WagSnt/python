lista = []
dado = []
maior = []
menor = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    seguir = ' '
    if seguir not in 'NS':
        seguir = str(input('Quer continuar?[S/N] ')).strip().upper()
        if seguir == 'N':
            break
for p in lista:
    if p[1] >= 100:
        maior.append(p[0])
    elif p[1] <= 70:
        menor.append(p[0])
print(f'Ao todo, foram cadastradas {len(lista)} pessoas no sistema.')
print(f'Foram {len(maior)} pessoas mais pesadas: {maior}')
print(f'Foram {len(menor)} pessoas mais leves: {menor}')
