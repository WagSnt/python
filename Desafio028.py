from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
num = int(input('E aí, em que número eu pensei? '))
n = randint(0, 5)
print('TÃN TÃN TÃN TÃN...')
sleep(2)
if num == n:
    print(f'Boa! Você adivinhou o número {n}')
else:
    print(f'Você errou, o número que eu escolhi foi {n}')
