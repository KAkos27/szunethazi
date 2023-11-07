#1.	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!

def elso():
    a: int = int(input("Kérek egy számot: "))

    while not (200 <= a <= 920):
        print("200 és 920 közti számot kell megadni!")
        a: int = int(input("Kérek egy számot: "))

    print(str(a)[0])

#2.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // ! 
#pl: 123//10 =12  123%10=3

def masodik(a):
    i:int = 0
    b:int = 0
    c:int = 1

    while i <= a:
        if i % c == 0:
            b += 1
            c *= 10
        i+=1

    print(b)

#3. Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. 
#PL. 324 -> „324 számjegyeinek összege: 9”

def harmadik(a):
    hossz = len(str(a))
    i = 0
    c = 0

    while i < hossz:
        b = str(a)[i]
        i+=1
        c += int(b)

    print(f"{a} számjegyeinek az összege: {c}")

#4.

def negyedik(a):

    if a <= 0:
        print("Be se jövök!")
    elif a == 1:
        print("Még 90 százelékon vagyunk!")
    elif 1 < a < 4:
        print("Még bírjuk (60%)")
    elif 3 < a < 8:
        print("Progit tanulunk, töltődünk! 70%")
    elif 7 < a < 10:
        print("Lassan nem bírjuk tovább! 50%")
    elif 10 <= a:
        print("Ez már tényleg túlzás.")
            
#5.	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:

def otodik(a,b):

    if a == "hétfő":
        print("alszik")
    elif a == "kedd" and b == "hittan":
        print("figyel")
    elif a == "kedd":
        print("alszik")
    elif a =="szerda" and b =="programozás":
        print("dolgozik")
    elif a =="szerda":
        print("nincs info")
    elif a =="csütörtök":
        print("figyel")
    elif a =="péntek":
        print("félig van jelen")
    else:
        print("valamit rosszul adtál meg :(")

#6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

def hatodik():
    a:int = int(input("Kérek egy számot: "))

    while a < 0:
        print("Nem lehet negatív számot megadni")
        a:int = int(input("Kérek egy számot: "))
    
    print(a ** 0.5)

#7.	A program olvasson be a konzolról két valós számot! 

def hetedik():
    a:int = int(input("Kérek egy számot:"))
    b:int = int(input("Kérek még egy számot:"))
    
    while not (a > 0 and b > 0):
        print("0-nál nagyobb számot kell megadni!")
        a:int = int(input("Kérek egy számot: "))
        b:int = int(input("Kérek még egy számot: "))

    print(f"Kerület: {2*(a+b)}") 
    print(f"Terület: {a*b}")   

#1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, hogy egy kihelyezett információs tábla részműködését leprogramozd! 

def terkepes():
    a:str = str(input("Melyik szektort választod?: "))

    if a == "a" or a == "A":
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif a == "b" or a == "B" or a == "e" or a == "E":  
        print("Kereskedelmi Csarnok")
    elif a == "c" or a == "C":
        print("Konferencia-központ Innovációs Showroom")
    elif a == "d" or a =="D":
        print("Hal, Víz és Ember")
    elif a == "f" or a == "F":
        print("Hagyományos Vadászati Módok Csarnoka")
    elif a == "g" or a == "G":
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif a == "h" or a == "H":
        print("Központi Magyar Kiállítás")
    elif a.isnumeric():
        print("HIBA: Adjon meg egy betűt A-H-ig!")
    else:
        print("Forduljon a pénztárhoz.")

#8.	Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!

def nyolcadik():
    a:int = 1
    b:int = 1
    i:int = 0
    
    while a < 11:
        while i != 10:
            if b == 10:
                print(a*b, end="")
            else:
                print(a*b, end=", ")
            b+=1
            i+=1
        print()
        a+=1
        b=1
        i=0


   