lista = []
acima = []
dados = {}
#total = 0
totidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados["sexo"] in 'MF':
            break
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    #total += 1
    totidade += dados['idade']
    while True:
        seguir = str(input('Quer continuar?[S/N]: ')).strip().upper()
        if seguir in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if seguir == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
media = totidade / len(lista)
print(f'A média de idade do grupo é de {media}')
print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=' ')
    print()
print('-=' * 30)
print('\nDados das pessoas acima da média de idade:')
for p in lista:
    if p["idade"] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')

