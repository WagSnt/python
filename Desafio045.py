from random import randint
from time import sleep
import pygame
#pygame.init()
#pygame.mixer.music.load('rocky.mp3')
#pygame.mixer.music.play()
#input()
#pygame.event.wait()
print('-='*10)
print('JOKENPO GAME!')
print('-='*10)
pygame.init()
pygame.mixer.music.load('rocky.mp3')
pygame.mixer.music.play()
itens = ('PEDRA 👊', 'PAPEL 🤚', 'TESOURA ✌')
computador = randint(0, 2)
print('''ESCOLHA UMA OPÇÃO:
[0] - PEDRA 👊
[1] - PAPEL 🤚
[2] - TESOURA ✌''')
jogador = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*15)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('-='*15)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE!')
elif jogador >= 3:
    print('')
#pygame.init()
#pygame.mixer.music.load('rocky.mp3')
#pygame.mixer.music.play()
input()
pygame.event.wait()


