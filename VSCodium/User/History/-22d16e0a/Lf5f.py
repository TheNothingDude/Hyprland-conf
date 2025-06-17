class Konyv:
    def __init__(self, sor):
        data = sor.strip().split(";")
        self.cim = data[0]
        self.mufaj = data[1]
        self.oldalszam = int(data[2])
        self.ev = int(data[3])
        self.eldasar = int(data[4])
    def hossz(self):
        
    
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
def f3(list) -> str:
    for i in list:
        c=0
        if i.ev >= 1600 and i.ev <=1699:
            if i.mufaj == "színmű":
                c+=1
    if c>0:
        return "1600 és 1699 között van színmű"
    else:
        return "1600 és 1699 között nincs színmű"
f2_ans = f2(konyvek,input("Milyen müfaj: "))
print(f"1 feladat: {f1(konyvek)} db")
print(f"2. feladat: {f2_ans[0]} db könyv tartozik ebbe a müfajba \n összoldalszáma: {f2_ans[1]}")