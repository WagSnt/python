def leiaInt(msg):
    while True:
        try: # tenta isso
            n = int(input(msg))
        except (ValueError, TypeError): # se não der, tenta isso
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido\033[m')
            continue # retorna pro whilep para perguntar novamente
        except KeyboardInterrupt:
            print('\n\033[0;33mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else: # foi validado, finalizar
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;33mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {num} e {num2}')

