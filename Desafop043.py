print('-='*20)
print('CALCULADORA IMC')
print('-='*20)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu imc é {imc:.1f}. Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.1f}. Você está com PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'Seu imc é {imc:.1f}. Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Seu imc é {imc:.1f}. Você está com OBESIDADE.')
elif 40 <= imc:
    print(f'Seu imc é {imc:.1f}. Você está com OBESIDADE MÓRBIDA.')
