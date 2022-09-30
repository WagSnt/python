s = float(input('Qual o seu salário atual? R$'))
a = float(input('Qual a porcentagem de aumento que irá receber? '))
r = s + (s * a / 100)

print(f'Seu salário que antes era de R${s:.2f} recebeu um aumento de {a:.0f}% e agora será de R${r:.2f}. Parabéns!')
