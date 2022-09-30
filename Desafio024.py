cid = str(input('Digite a cidade em que você nasceu: ')).upper().replace('-', ' ').split()
print(cid[0] == 'SANTA')
#replace com ('-', ' ') é para evitar "false" incorreto em caso da pessoa utilizar o - como separação. Ex: Santa-Cruz
#sendo assim, primeiro ira colocar tudo em maiúsculo, depois caso precise, trocar o '-' por 'espaço' e aí separar as palavras


