from data import sportolok, szemelyiedzok
from os import system
szemelyiezokfajlnev="szemelyiedzok.txt"

def menu():
    system('cls')
    valasztott=''
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Személyi edzők kiírása')
    print('2 - Új sportoló felvétele')
    print('3 - Sportolók mentése fájlba')
    print('4 - Személyi edzőhöz tartozó sportoló')
    print('5 - Melyik személyi edzőhöz tartozik a legtöbb sportoló')
    print('6 - Sportoló törlése')
    valasztott=input('Válasszon egy menüpontot: ')
    return valasztott

def szemelyiedzokKiirasa():
    print('Személyi edzők listája: ')
    for i in range(0,len(szemelyiedzok)):
        print(f'\t{i+1}. {szemelyiedzok[i]}')
    input('Tovább......') 

def szemelyiedzokfajlBetoltes():   
    file=open(szemelyiezokfajlnev,'r',encoding='utf-8')
    for row in file:
        szemelyiedzok.append(row.strip())  
    file.close()