class GokartPalya:
    def __init__(self, data):
        self.nev = data[0]
        self.telepules = data[1]
        self.hossz = int(data[2])
        self.jegyar = int(data[3])
palyak = []

with open("./gokart-adatok.txt") as s:
    s.readline()
    for i in s:
        palyak.append(GokartPalya(i.strip().split(";")))


def fel1(list):
    osszeg =0
    for i in list:
        osszeg += i.hossz
    return osszeg

def fel2(list):
    minim = list[0].jegyar
    for i in list:
        if i.jegyar < minim:
            minim = i.jegyar
    for i in list:
        if i.jegyar == minim:
            return [minim, i.nev]

print(f"{fel1(palyak)} méter")
print(f"{fel2(palyak)[0]}")