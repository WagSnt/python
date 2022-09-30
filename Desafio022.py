nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Em letras maiúsculas, {nome.upper()}')
print(f'Em letras minúsculas, {nome.lower()}')
print('Seu nome tem ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))














