soma = 0
cont = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
      soma = soma + c
      cont = cont + 1
print(f'A soma dos números {cont} múltiplos de 3 é igual a {soma}')

