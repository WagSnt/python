from datetime import date
dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
ano = int(input('Digite seu ano de nascimento: '))
dicionario['Idade'] = date.today().year - ano
dicionario['CTPS'] = int(input('Digite o número da carteira de trabalho [Digite 0 se não tiver]: '))
if dicionario['CTPS'] != 0:
    dicionario['contratação'] = int(input('Digite seu ano de contratação: '))
    dicionario['Salário'] = float(input('Digite o seu salário: R$'))
    dicionario['Aposentadoria'] = (dicionario['contratação'] - ano) + 35
else:
    dicionario['CTPS'] = 'Não possui'
print(dicionario)
for k, v in dicionario.items():
    print(f'{k}: {v}')
