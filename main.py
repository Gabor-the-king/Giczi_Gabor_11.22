from functions import * 
from os import system
from data import szemelyiedzok, sportolok
szemelyiedzokfajlBetoltes()
sportolokFajlbetoltes()

valasztott=''
while valasztott!='0':
    valasztott=menu()
    if valasztott=='1':
        system('cls')
        szemelyiedzokKiirasa()
    elif valasztott=='2':
        system('cls')
        pass
    elif valasztott=='3':    
        system('cls')
        pass
    elif valasztott=='4':
        system('cls')
        sportolokKiirasa()
    elif valasztott=='5':
        system('cls')
        pass
    elif valasztott=='6':
        system('cls')
        pass
