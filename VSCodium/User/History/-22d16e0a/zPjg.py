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
def f2(list, mufaj):
    c= 0
    ossz=0
    for i in list:
        if i.mufaj == mufaj:
            c +=1
            ossz += i.oldalszam
    return [c, ossz]

print(f"1 feladat: {f1(konyvek)} db")
print(f"2. feladat: {f2(konyvek,input("Milyen müfaj: ") )}")