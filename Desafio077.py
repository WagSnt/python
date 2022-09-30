lista = ('Aprender', 'Linguagem', 'Desenvolver', 'Python', 'Wagner', 'Stephanie', 'Otavio', 'Amanda', 'Internacional')
print('-='*15)
print('LEITOR DE VOGAIS')
print('-='*15)
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
