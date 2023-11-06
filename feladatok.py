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
