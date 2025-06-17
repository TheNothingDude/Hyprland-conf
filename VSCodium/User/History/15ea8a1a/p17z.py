import datetime
import random as r

class Diak:
    minor = 0 
    adult = 0
    vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
    keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
    osztalyok = ["10.C", "10.B", "10.A"]
    def __init__(self):
        self.nev = type(self).keresztnevek[r.randint(0,4)] + " " + type(self).vezeteknevek[r.randint(0,5)]
        self.osztaly = type(self).osztalyok[r.randint(0,2)] 
        self.szEv = r.randint(10,16) 
        if self.kor() >= 18:
            type(self).adult +=1
        else:
            type(self).minor += 1
    def kor(self) -> int:
        return datetime.datetime.now().year - self.szEv
    def __str__(self) -> str:
        return f"A diak életkora {self.kor()}, A neve {self.nev}, és a {self.osztaly}-ba jár."
    
    @classmethod
    def diak_db(cls) -> int:
        return cls.minor + cls.adult 
    @staticmethod
    def diak_info() -> str:
        return "Csak a legjobbak"

diakok = []
for i in range(5):
    diakok.append(Diak())
        
        
for i in diakok:
    print(i)

diakok[0].diak_db()
