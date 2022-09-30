num = int(input('Digite um número para saber se ele é par ou impar: '))
r = num % 2
if r == 0:
    print(f'O número{num} é PAR')
else:
    print(f'O número {num} é IMPAR')
