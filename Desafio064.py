cont = somanum = 0
num = int(input('digite um número [999 para parar]: '))
while num != 999:
    somanum += num
    cont += 1
    num = int(input('digite um número [999 para parar]: '))
#somanum = somanum - 999
#cont = cont - 1
print(f'Você digitou {cont} números e a soma entre eles foi {somanum}.')
