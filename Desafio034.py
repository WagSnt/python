sal = float(input('Qual é o seu salário? '))
if sal > 1250:
    s = sal + (sal * 10 / 100)
    print(f'Seu salário recebeu um aumento de 10% e a partir de agora será no valor de R${s}')
else:
    s = sal + (sal * 15 / 100)
    print(f'Seu salário recebeu um aumento de 15% e a partir de agora será no valor de R${s}')

