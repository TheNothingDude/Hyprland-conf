class Kolcsonzes:
    def __init__(self, sor):
        data = sor.strip().split(";")
        self.nev = data[0]
        self.jAzon = data[1]
        self.EOra = int(data[2])
        self.EPerc = int(data[3])
        self.VOra = int(data[4])
        self.Vperc = int(data[5])

with open("./pa/kolcsonzesek/kolcsonzesek.txt", "r", encoding="utf-8") as s:
    vizbickiklik = []
    s.readline()
    for i in s:
        vizbickiklik.append(Kolcsonzes(i))

def f5(list):
    return len(list)

def f6(list):
    c=0
    nev = input("Kérek egy nevet: ")
    print(f"{nev} kölcsönzései: ")
    for i in list:
        if i.nev == nev:
           print(f"\t{i.EOra}:{i.EPerc}-{i.VOra}:{i.Vperc}")
           c +=1
    if c == 0:
        print("Nem volt ilyen nevü kölcsönző!")

def f7(list):
    oraperc = input("Add meg ora:percben: ").strip().split(":")
    perc = int(oraperc[0]) *60 + int(oraperc[1])
    for i in list:
        if i.EOra*60 + i.EPerc < perc and i.VOra * 60 + i.Vperc > perc:
            print(f"\t{i.EOra}:{i.EPerc}-{i.VOra}:{i.Vperc} - {i.nev} ") 
def f8(list):
    penz = 0
    for i in list:
        perc = (i.VOra *60 + i.Vperc) - (i.EOra * 60 + i.EPerc)
        penz += (perc//30)*2400
    return penz

print(f"5. feladat: {f5(vizbickiklik)}")
print(f"6. feladat: ", end=" ")
f6(vizbickiklik)
print(f"7. feladat: ", end=" " )
f7(vizbickiklik)
print(f"{f8(vizbickiklik)} Ft")
