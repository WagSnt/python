matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {somapar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é igual a {somacol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da linha 2 é {maior}')
