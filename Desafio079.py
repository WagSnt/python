valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('VALOR JÁ ADICIONADO, não será incluso na lista.')
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N] ')).upper().strip()
    if seguir == 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')
