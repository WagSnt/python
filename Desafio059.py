from time import sleep
op = 0
print('\033[1;32m-=\033[m'*15)
print('\033[1;197mCALCULADORA SIMPLES 👩‍💻\033[m')
print('\033[1;32m-=\033[m'*15)
n1 = int(input('\033[1;197mPrimeiro valor:\033[m '))
n2 = int(input('\033[1;197mSegundo valor:\033[m '))
while op != 5:
    op = int(input('''OPERAÇÕES:
    \033[1;33m[1]\033[m SOMAR ➕
    \033[1;33m[2]\033[m MULTIPLICAR ✖
    \033[1;33m[3]\033[m MAIOR ⬆
    \033[1;33m[4]\033[m NOVOS NÚMEROS 🔄
    \033[1;33m[5]\033[m SAIR DO PROGRAMA 🔚
    >> Digite a operação que deseja realizar: '''))
    if op == 1:
        print(f'A soma de \033[1;33m{n1}\033[m + \033[1;33m{n2}\033[m = \033[1;34m{n1+n2}\033[m')
    elif op == 2:
        print(f'A multiplicação entre \033[1;33m{n1}\033[m x \033[1;33m{n2}\033[m = \033[1;34m{n1*n2}\033[m')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'\033[1;34m{maior}\033[m é o maior')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        sair = True
        print('Finalizando programa')
    print('\033[1;32m-=\033[m' * 25)
sleep(1)
print('Programa finalizado com sucesso. Volte sempre!')

