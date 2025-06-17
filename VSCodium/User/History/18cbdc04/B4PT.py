class GokartPalya:
    def __init__(self, data):
        self.nev = data[0]
        self.telepules = data[1]
        self.hossz = int(data[2])
        self.jegyar = data[3]
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

print(f"{fel1(palyak)} méter")