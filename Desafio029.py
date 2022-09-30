v = float(input('Digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print(f'Seu carro está a {v}km/h e ultrapassou o limite de 80km/h.')
    print(f'você foi multado em R${m}. ')
else:
    print(f'Seu carro está a {v}km/h e está dentro do limite de 80km/h.')
print('Mantenha a atenção no transito. Tenha um ótimo dia!')
