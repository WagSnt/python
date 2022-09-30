from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {num}')
print(f'O menor valor foi {min(num)}')
print(f'O maior valor foi {max(num)}')
