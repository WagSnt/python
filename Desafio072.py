num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))

    while 0 > escolha > 20:
        print('Escolha incorreta, tente novamente.')
        escolha = int(input('Digite um número entre 0 e 20: '))
    print(f'{escolha} por extenso é: {num[escolha]}')
    seguir = ' '

    while seguir not in 'SN': # Enquanto seguir não for a resposta correta, irá ficar repetindo a pergunta
        seguir = str(input('Quer continuar? [S/N] ')).upper().strip()
    if seguir == 'N':
        break
print('Programa finalizado')



