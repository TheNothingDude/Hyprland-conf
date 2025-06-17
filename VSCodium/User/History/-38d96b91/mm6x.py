class Rendeles:
    def __init__(self, sor) -> None:
        data = sor.strip().split()
        self.nap = int(data[0])
        self.varos = data[1]
        self.elad = int(data[2])


rendelesek = []
with open("./rendel.txt", "r" ,encoding="utf-8") as s:
    for i in s:
        rendelesek.append(Rendeles(i))


def f4(list):
    return len(list)

def f5(list):
    nem = 0
    c = 0
    nap = 1 
    for j in list:
        if j.nap == nap:
            if j.varos == "NR":
                c += 1
        nap +=1
        if c == 0:
            nem += 1
    
    if nem == 0:
        return "Minden nap volt rendelés a reklámban nem érintett városból"
    else:
        return nem

def f6(list):
    max_db =0
    for i in list:  
        if i.elad > max_db:
            max_db = i.elad
    for i in list:
        if i.elad == max_db:
            return [max_db, i.nap]

def f7(list):
    eTiz = {"PL": 0, "TV": 0, "NR": 0}
    mTiz = {"PL": 0, "TV": 0, "NR": 0}
    hTiz = {"PL": 0, "TV": 0, "NR": 0}

    for i in list:
        if i.nap <= 10:
            if i.varos == "PL":
                eTiz["PL"] +=1
            elif i.varos == "TV":
                eTiz["TV"] +=1
            elif i.varos =="NR":
                eTiz["NR"] +=1
        elif i.nap >= 11 and i.nap <= 20:
            if i.varos == "PL":
                mTiz["PL"] +=1
            elif i.varos == "TV":
                mTiz["TV"] +=1
            elif i.varos =="NR":
                mTiz["NR"] +=1
        elif i.nap >= 21 and i.nap <= 30:
            if i.varos == "PL":
                hTiz["PL"] +=1
            elif i.varos == "TV":
                hTiz["TV"] +=1
            elif i.varos =="NR":
                hTiz["NR"] +=1

    with open("./kampany.txt", "w", encoding="utf-8") as out:
        out.write("Napok;1..10;11..20;21..30\n")
        for i in ["PL", "TV", "NR"]:
            out.write(f"{i};{eTiz[i]};{mTiz[i]};{hTiz[i]}\n") 



print(f"4. Feladat: A rendelések száma: {f4(rendelesek)}")
print(f"5. Feladat: {f5(rendelesek)} nap nem volt a reklámban nem érintett városból rendelés")
max_db = f6(rendelesek)
print(f"5.Feladat: A legnagyobb {max_db[0]}, A rendelés napja: {max_db[1]} ")
f7(rendelesek)