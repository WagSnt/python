from time import sleep
from random import randint
computador = randint(0, 10)
acertou = False
palpite = 0
print('Olá! Eu sou o seu computador, vamos jogar um jogo de adivinhação...')
sleep(0.5)
print('Eu vou pensar em um número de 0 a 10 e você deve adivinhar em qual eu pensei')
sleep(0.5)
print('PENSANDO...')
sleep(3)
print('pronto')
while not acertou:
    jogador = int(input('Digite o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('É menos, tente novamente...')
        elif jogador < computador:
            print('É mais, tente novamente...')
print(f'Acertou com {palpite} tentativas!')
