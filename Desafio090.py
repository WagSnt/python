boletim = {}
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Media'] = float(input(f'Digite a média de {boletim["Nome"]}: '))
if boletim['Media'] >= 7.0:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in boletim.items():
    print(f'{k} do aluno é {v}')
