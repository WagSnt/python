km = int(input('Digite a distância da viagem: '))
if km <= 201:
    p = km * 0.50
    print(f'Sua viagem é de {km}km, custando R$0.50 por km será gasto R${p:.2f}')
else:
    p = km * 0.45
    print(f'Sua viagem é de {km}km, custando R$0.45 por km será gasto R${p:.2f}')