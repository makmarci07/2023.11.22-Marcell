#1.feladat Írj programot, ami kiírja a képernyőre, hogy ”Hello world!”!
szovegKiir = f"Hello World!"
print(szovegKiir)

#2.feladat Írj programot, beolvassa a felhasználó nevét, majd köszön neki!
nev, szovegKiir = "", ""

nev = input("Hogy hívnak: ")


szovegKiir = f"Hello {nev}!"
print(szovegKiir)

#3.feladat Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!

alapSzam, ketszeres,  szovegKiir = 0, 0, ""
alapSzam = int(input("kérem a számot: "))
ketszeres = 2 *alapSzam
szovegKiir = f"A szám: {alapSzam} \
ketszerese: {ketszeres}"

print(szovegKiir)

"""

#4.feladat Írj programot, ami beolvas két számot, majd kiírja:
#a. az összegüket;
#b. különbségüket;
#c. szorzatukat;
#d. hányadosukat, ha lehet!

"""
elso, masodik, osszeg, kulonbseg, szorzat, hanyados, szovegKiir = 0, 0, 0, 0, 0,0.0 

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
kulonbseg = elso / masodik

szovegKiir = f"A számok:  {elso}, {masodik}"
szovegKiir += f"összege:  {osszeg}"
szovegKiir += f"különbsége:  {kulonbseg}"
szovegKiir += f"Szorzat:  {szorzat}"
szovegKiir += f"Hányadosa:  {hanyados:.4f}"

print(szovegKiir)

#5. Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat.!

elso, masodik, nagyobb, szovegKiir = 0, 0, 0,

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

if elso <= masodik:
    nagyobb = masodik
else:
    nagyobb = elso 

szovegKiir = f"A nagyobb szám: {nagyobb}"  

print(szovegKiir)

#6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

elso, masodik, harmadik, legkisebb, szovegKiir = 0, 0, 0, 0, ""

#segédváltozó
kisebb = 0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
harmadik = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    kisebb =  elso
else:
    kisebb = masodik

if kisebb <= harmadik:
        legkisebb = kisebb
else: 
    legkisebb = harmadik

szovegKiir = f"A legkisebb szám: {legkisebb}"
print(szovegKiir)
