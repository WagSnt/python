totgol = 0
dicionario = {}
golpartida = []
dicionario['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicionario["Nome"]} jogou? '))
for p in range(partidas):
    gol = int(input(f'Quantos gols ele fez na partida {p+1}? '))
    golpartida.append(gol)
    totgol += gol
dicionario['Gols'] = golpartida[:]
dicionario['Total'] = totgol
print('-=' * 30)
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O jogador {dicionario["Nome"]} jogou {partidas} partidas:')
for c, v in enumerate(golpartida):
    print(f'  => Na partida {c + 1}, fez {v} gols')
print(f'Foi um total de {totgol} gol(s) no campeonato')
