resposta = ''
cont = soma = maior = menor = 0
while resposta != 'N':
    num = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Você digitou {cont} números. A média entre eles é de {media:.2f}')
print(f'O menor número digitado foi o {menor} e o maior número digitado foi o {maior}')