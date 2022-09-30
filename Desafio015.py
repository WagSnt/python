km = float(input('Quantos KM foram percorridos com o veículo? '))
d = int(input('Quantos dias foram usados o veículo? '))
r = (km * 0.15) + (d * 60)
print(f'O total a pagar pelo aluguel do veículo: R${r:.2f}.')