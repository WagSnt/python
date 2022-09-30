def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


n = str(input('Digite o nome do jogador: '))
g = str(input(f'Digite quantos gols {n} marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
