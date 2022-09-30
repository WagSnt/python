pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 10 # contador começa a partir do 10
contador = 0 # contador de termos
while c > 0: # enquanto c for maior que 0 (que vai ser sempre a não ser que o usuário queira fechar o programa
    print(f'{pt} > ', end='') # pt mostra a razão escolhida
    pt += razao # faz a soma correta para o cálculo
    c -= 1 # c -=1 diminui um valor de " c " nosso contador de termos a serem exibidos
    contador += 1 # contador de termos
    if c == 0: # se o usuário escolher c, programa é finalizado
        c = int(input('Deseja mostrar mais quantos termos na sequência? '))
print(f'Finalizado. Ao todo foram mostrados {contador} termos.')

