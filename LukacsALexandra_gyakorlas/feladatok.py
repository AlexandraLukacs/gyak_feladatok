'''1. Írjuk ki 0-tól 150-ig a páros számokat!'''
def feladat1():
    print("1. Feladat")
    i: int= 0
    while i <= 150:
        if i < 150:
            print(i, end=", ")
        else:
            print(i, end=" ")
        i += 2


'''2. Számold meg 10 bekért szám esetében a 3-mal osztható számokat!'''
def feladat2():
    print("2. Feladat")
    szamok: int = 0
    oszthato3mal: int = 0
    while szamok < 10:
        szam_bekeres: int = int(input("Adjon meg egy számot: "))
        szamok += 1
        if szam_bekeres % 3 == 0:
            oszthato3mal += 1
    print(f"A 3-mal osztható számok: {oszthato3mal}")

'''3. Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!'''
def feladat3():
    print("3. Feladat")
    szam_bekeres: int= int(input("Adjon meg egy 10-el osztható számot: "))
    while not(szam_bekeres % 10 == 0):
        szam_bekeres: int= int(input("Adjon meg egy 10-el osztható számot: "))
    print(f"A {szam_bekeres} osztható 10-el!")


'''4. Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!'''
def feladat4():
    print("4. Feladat")
    szam_bekeres: int= int(input("Adjon meg egy kétjegyű páros számot: "))
    while not(((100 > szam_bekeres >= 10) or (szam_bekeres <=-10 and szam_bekeres > -100)) and szam_bekeres % 2 == 0):
        szam_bekeres: int=int(input("Kétjegyű páros szám kell: "))
    print(f"A {szam_bekeres} kétjegyű és páros!")

'''5. Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.'''
def feladat5():
    print("5. Feladat")
    szam_bekeres: int= int(input("Adjon meg egy pozitív páratlan számot: "))
    while not(szam_bekeres >= 0 and szam_bekeres % 2 == 1):
        szam_bekeres: int=int(input("Pozitív páratlan szám kell: "))
    print(f"A {szam_bekeres} pozitív páratlan szám!")

'''6. Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.'''
def feladat6():
    print("6. Feladat")
    szam_bekeres: int= int(input("Adjon meg egy 3-mal osztható vagy négyzetszámot: "))
    while not((szam_bekeres ** 0.5) % 1 == 0 or szam_bekeres % 3 == 0):
        szam_bekeres: int=int(input("3-mal osztható vagy négyzetszám kell: "))
    print(f"A {szam_bekeres} 3-mal osztható vagy négyzetszám szám!")

'''7. Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!'''
def feladat7():
    print("7. Feladat")
    a: int= int(input("Adjon meg egy számot: "))
    b: int= int(input("Adjon meg egy számot: "))
    c: int= int(input("Adjon meg egy számot: "))
    while not(a + b > c and b + c > a and a + c > b):
