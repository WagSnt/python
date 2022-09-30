#from math import factorial
#n = int(input('Digite um número para saber o seu fatorial: '))
#f = factorial(n)
#print(f'O fatorial de {n}! é {f}')

# Opção tradicional

n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
while c > 0: # Enquanto contador for maior que 0
    print(f'{c}', end='') # Mostrar o fatorial desejado
    print(' x ' if c > 1 else ' = ', end='') # adicionar o 'x' de vezes e no fim quando chegar ao 1 acrescentar o '='
    f *= c # f x (5, 1)
    c -= 1 # para diminuir um número do contador a cada operação 5 x 4 next - > 5 x 3 e assim por diante
print(f'{f}')