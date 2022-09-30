tot18 = toth = totf20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 21:
        totf20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar o cadastro de pessoa? ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {toth}')
print(f'Total de mulheres cadastradas com menos de 20 anos: {totf20}')


