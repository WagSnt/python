from datetime import date
data = int(input('Qual o seu ano de nascimento? '))
aa = date.today().year - data
if aa < 18:
    r = 18 - aa
    print(f'Você deverá realizar o alistamento militar daqui a {r} ano(s).')
elif aa == 18:
    print('Já está na hora de você realizar seu alistamento militar')
else:
    t = aa - 18
    print(f'Seu prazo de alistamento foi a {t} anos atrás')
