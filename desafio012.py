v = float(input('Qual o valor atual do produto? R$'))
d = float(input('Quantos % de desconto será dado na promoção? '))
p = v - (v * d / 100)
print(f'O valor final do produto de R${v} com o desconto de {d:.0f}% ficará no valor promocional de: R${p:.2f}')


