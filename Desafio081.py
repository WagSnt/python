lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if seguir == 'N':
        break
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True) # comando para exibição da lista de forma decrescente
print(f'Os números em forma decrescente ficaram {lista}.')
if 5 in lista: # verificação se possui o número 5 na lista e mostrar quantas vezes foi digitado
    print(f'O número 5 foi digitado {lista.count(5)} vezes')
else:
    print('O número 5 não foi adicionado a lista')
