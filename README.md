# Szoftverfejlesztési folyamatok projektmunka

## Hallgató adatai

- Név: Kenese Balázs
- Neptun kód: C4R1AD
- h-s azonosító: h589511 

## Választott alap projekt:

Potyogós Amőba

## Megvalósítandó feature-ök

### I. Egy lépés visszavonása

Biztosítsd a lehetőséget, hogy a játékos visszavonhassa az előző lépést!  
A lépés visszavonástól, egy játékos-ágens lépés páros megtörténése után a következők elvártak:
  - a függvény képes legyen a lépés páros előtti állapotba állítani a játéktáblát úgy, hogy a játék onnan folytatódik
  - egyszerre csak egy lépés párost lehessen visszavonni, tehát kétszer egymás után ne lehessen meghívni a függvényt
  - kezeljük le azt az esetet is, amikor az utolsó lépés páros győzelemmel zárul, akkor azt is helyesen vonjuk vissza

### II. Dinamikus tábla méret és győzelmi feltétel

A játék működjön rugalmasan különböző táblaméretekkel és győzelmi feltételekkel.
A dinamikus tábla és győzelmi feltétel megvalósításától elvárt, hogy a kódban mindenhol, ahol szükséges, a sorokért, oszlopokért és győzelmi feltételekért felelő szám literálok be legyenek helyettesítve a fentebb említett változókkal. Ezen felül a funkciótól elvárt, hogy a felhasználótól beolvas 3 számot, és ha a 3 szám érvényes (pl. 3x3-as pályán nem lehet 5 egymást követő koronggal nyerni, így a 3, 3, 5 bemenet nem érvényes) bemenetet alkot, akkor a megfelelő változókat beállítja, ezután pedig elkezdődik a játék (meghívódik a play_game függvény). Ellenkező esetben a függvény újra kérjen be 3 számot a felhasználótól.


## Követelmények
- venv (opcionális)
- Python 3.10 vagy magasabb
