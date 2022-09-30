n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(F'O \033[1;33m{n1}\033[m é maior.')
elif n2 > n1:
    print(f'O \033[1;33m{n2}\033[m é maior.')
else:
    print(f'\033[1;33mNão existe\033[m valor maior, {n1} e {n2} são iguais')
