from random import randint
cont = 0
while True:
    num = int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    computador = randint(1, 10)
    while escolha not in 'PpIi':
        escolha = str(input('ESCOLHA INVÁLIDA! Par ou Impar [P/I]: ')).strip().upper()[0]
    computador = randint(1, 10)
    soma = computador + num
    if escolha in 'P' and not soma % 2 == 0:
        print(f'Eu joguei {computador} e você {num}, a soma foi {soma} deu IMPAR E VOCÊ PERDEU!')
        break
    if escolha in 'I' and soma % 2 == 0:
        print(f'Eu joguei {computador} e você {num}, a soma foi {soma}, deu PAR E VOCÊ PERDEU')
        break
    if escolha in 'I' and not soma % 2 == 0:
        print(f'Eu joguei {computador} e você {num}, a soma foi {soma}, deu IMPAR E VOCÊ VENCEU')
    if escolha in 'P' and soma % 2 == 0:
        print(f'Eu joguei {computador} e você {num}, a soma foi {soma} deu PAR E VOCÊ VENCEU!')
    cont +=1
    print('Vamos continuar...')
print(f'FIM DO JOGO!')
print(f'Você acertou {cont} rodadas consecutivas, parabéns!')



