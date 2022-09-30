#Exercício Python 63:
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

t1 = 0
t2 = 1
cont = 3 # contagem a partir do 3, já que os dois termos iniciais "0 e 1" são padrão
print('-='*20)
print('Sequência de Fibonacci')
print('-='*20)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*40)
print(f'{t1} -> {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' -> FIM')
