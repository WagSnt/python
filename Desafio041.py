from datetime import date
print('='*40)
print('\033[1;97;44mCONFEDERAÇÃO NACIONAL DE NATAÇÃO (CNN)\033[m')
print ('='*40)
ano = int(input('Digite o ano de nascimento do atleta: '))
cat = date.today().year - ano
if cat <= 9:
    print('O atleta é da categoria \033[1;34mMIRIM\033[m')
elif cat <= 14:
    print('O atleta é da categoria \033[1;34mINFANTIL\033[m')
elif cat <= 19:
    print('O alteta é da categoria \033[1;34mJUNIOR\033[m')
elif cat <= 20:
    print('O atleta é da categoria \033[1;34mSÊNIOR\033[m')
else:
    print('O atleta é da categira \033[1;34mMASTER\033[m')
