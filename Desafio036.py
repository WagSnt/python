import math
print('-='*20)
print('\033[1;49mSISTEMA APROVADOR DE EMPRÉSTIMO BANCÁRIO')
print('-='*20)
casa = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o seu salário atual? R$'))
a = float(input('Em quantos anos você irá pagar o imóvel? '))
p = casa / (a * 12)
if p > (sal * 30 / 100):
    print(f'\033[31mEMPRÉSTIMO NEGADO!\033[m A prestação de R${p:.2f} por mês, excede os 30% do seu salário de R${sal:.2f}.')
else:
    print(f'\033[32mEMPRÉSTIMO APROVADO!\033[m O valor da prestação mensal será de R${p:.2f} por mês. Pagos durante {a:.0f} anos.')
