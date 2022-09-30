n = float(input('Digite quanto você possui em sua carteira, e veja quantos dólares você pode comprar: R$'))
d = n / 3.27
print('Com R${}, você pode comprar US${:.2f} Dólares.\n OBS: Valor do dólar utilizado: 3.27'.format(n, d))
