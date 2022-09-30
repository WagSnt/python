import urllib.request
from tkinter import *

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mErro: Site inacessível ou conexão de internet instável.\033[m')
else:
    print('\033[0;32mConexão com o site estabelecida com succeso.\033[m')


janela = Tk()

janela.mainloop()
