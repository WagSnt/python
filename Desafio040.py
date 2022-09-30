n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print(f'Sua média é {m}. Parabéns, você foi \033[1;32mAPROVADO!\033[m')
elif m < 5.0:
    print(f'Sua média é {m}. Estude, você está \033[1;31mREPROVADO!\033[m')
elif 7 > m >= 5.0:
    print(f'Sua média é {m}. Estude, você está em \033[1;33mRECUPERAÇÃO!\033[m')
