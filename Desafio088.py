from random import randint
from time import sleep
jogos = []
dados = []
print('-=' * 15)
print('     ROBÔ DA MEGA SENA     ')
print('-=' * 15)
quant = int(input('Quantos jogos você quer que eu faça? '))
totjogos = 1
while totjogos <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
    totjogos += 1
print('-=' * 3, f'CALCULANDO {quant} JOGO(S)', '-=' * 3)
sleep(2)
for i, j in enumerate(jogos):
    print(f'JOGO {i+1}: {j}')
    sleep(1.5)
print('JOGOS GERADOS COM SUCESSO. BOA SORTE!')
