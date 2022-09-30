import random
compra = float(input('Qual o preço das compras? '))
print('FORMAS DE PAGAMENTO'
      '\n[1] - à vista dinheiro/cheque'
      '\n[2] - à vista cartão'
      '\n[3] - 2x no cartão'
      '\n[4] - 3x ou mais no cartão')
pag = int(input('Qual a opção de pagamento? '))
if pag == 1:
    av = compra - (compra * 10 / 100)
    print(f'Sua compra de R${compra:.2f}, vai ficar no valor de R${av:.2f}.')
elif pag == 2:
    avc = compra - (compra * 5 / 100)
    print(f'Sua compra de R$ {compra:.2f}, vai ficar no valor de R$ {avc:.2f}')
elif pag == 3:
    c2 = compra / 2
    print(f'Sua compra será em 2 parcelas de R${c2:.2f} por mês.')
elif pag == 4:
    parcela = int(input('Em quantas vezes será parcelado? '))
    juros = compra + (compra * 20 / 100)
    totalp = juros / parcela
    print(f'Sua compra será parcelada em {parcela}X de R${totalp:.2f} COM JUROS.')
    print(f'Sua compra de R${compra}, vai custar ao todo R${juros:.2f}.')
else:
    print('Opção inválida, tente novamente.')











