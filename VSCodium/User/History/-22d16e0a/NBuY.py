class Konyv:
    def __init__(self, sor):
        data = sor.strip().split(";")
        self.cim = data[0]
        self.mufaj = data[1]
        self.oldalszam = data[2]
        self.ev = data[3]
        self.eldasar = data[4]
    
konyvek = []    
with open("./konyvek-adatok.txt") as s:
    s.readline()
    for i in s:
        konyvek.append(Konyv(i))

def f1(list):
    return len(list)

print(f"1 feladat: {f1(konyvek)} db")
