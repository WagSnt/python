somaidade = 0 # variável para soma da idade necessária para calculo de divisão de média
mediaidade = 0 # variável para média de idade
maioridadeh = 0 # váriável para idade mais velha
nomevelho = '' # variável para nome do mais velho
totmulher20 = 0 # variável para menos de 20 anos
for p in range(1, 5):
    print('-'*5, f'{p}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'mM': #padronizando a 1ª pessoa
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadeh: # comparando a 1ª pessoa com as demais
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20: # mulheres com menos de 20 anos
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadeh} anos e se chama {nomevelho}.')
print(f'Ao todo, {totmulher20} mulher(es) tem menos de 20 anos.')
