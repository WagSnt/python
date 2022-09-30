num = (int(input('Digite um número: ')))
e = int(input('Qual será a base de conversão? 1-Binário, 2-octal e 3-hexadecimal: '))
if e == 1:
    b = bin(num)
    print(f'{num} binário é: {b[2:]}')
elif e == 2:
    o = oct(num)
    print(f'{num} octal é: {o[2:]}')
else:
    h = hex(num)
    print(f'{num} hexadecimal é: {h[2:]}')
