from genericpath import exists
from data import sportolok, szemelyiedzok
from os import system
szemelyiezokfajlnev="szemelyiedzok.txt"
sportolokfajlNev="sportolok.txt"

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
    system('cls')
    print('Személyi edzők listája: ')
    for i in range(0,len(szemelyiedzok)):
        print(f'\t{i+1}. {szemelyiedzok[i]}')
    input('Tovább......') 

def szemelyiedzokfajlBetoltes():   
    file=open(szemelyiezokfajlnev,'r',encoding='utf-8')
    for row in file:
        szemelyiedzok.append(row.strip())  
    file.close()
    
def sportolokFajlbetoltes():
    file=open(sportolokfajlNev, 'r',encoding='utf-8')
    darabolt=[]
    for row in file:
        darabolt=row.strip().split(';')
        sportolok[darabolt[0]]=darabolt[1]
    file.close()
    
def sportolokKiirasa():
    system('cls')
    print('Sportolók edzőkkel: ')
    sorszam=1
    for key,value in sportolok.items():
        print(f'\t{sorszam}. {key} - {value}')
        sorszam+=1

def ujSportoloFelvetele():
    system('cls')    
    print('Új sportoló felvétele')
    nev=input('Kérem a spotoló nevét: ')
    szemelyiedzo=input('Kérem a személyi edző nevét: ')
    while szemelyiedzo not in szemelyiedzok:
        szemelyiedzo=input('A bekért név nincs benn a listában kirem adjon meg egy másikat: ')
    sportolok[nev]=szemelyiedzo
    input('A sportoló sikeresen felvételre került...')

def mentesFajlba():
    file=open('sportolok.txt','w',encoding='utf-8')
    for key,value in sportolok.items():
        file.write(f'{key};{value}\n')  
    file.close()
    input('Sikeres mentés...')

def SzemelyiEdzohozSportolo():
    szemelyiedzoklista=list(sportolok.values())
    legtobbszemelyedzo=max(set(szemelyiedzoklista), key=szemelyiedzoklista.count)
    print(f'A legtöbb sportolóhoz tartozó személyi edző: {legtobbszemelyedzo}')
    input('Tovább......')

def SportoloTorlese():
    sportolokKiirasa()
    torlendo=int(input('Kit szeretne törölni? Adja meg a sorszámát: '))-1
    sportoloklista=list(sportolok.keys())
    sportolok.pop(sportoloklista[torlendo])
    input('A sportoló törlése sikeres...')
