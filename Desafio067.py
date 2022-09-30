while True:
    print('-='*10)
    num = int(input('Digite um valor para ver sua tabuada: '))
    print('-=' * 10)
    if num < 0:
        break
    for t in range(1, 11):
        print(f'{num} x {t} = {num * t}')
print('Programa finalizado.')
