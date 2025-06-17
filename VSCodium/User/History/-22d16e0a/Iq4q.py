class Konyv:
    def __init__(self, sor):
        data = sor.strip().split(";")
        self.cim = data[0]
        self.mufaj = data[1]
        self.oldalszam = data[2]
        self.ev = data[3]
        self.