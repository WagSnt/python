soma = tot1k = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    soma += preço
    cont +=1
    if preço >= 1000:
        tot1k += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if seguir == 'N':
        break
print(f'O total da compra foi no valor de R${soma:.2f}')
print(f'Ao todo foram {tot1k} produtos acima de R$ 1000')
print(f'O produto mais barato foi o {barato}')
