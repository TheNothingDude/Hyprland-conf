pez = int(input("Mennyi pénzed van: "))

while pez >0:
    koltes = int(input("Mennyit szeretnél elkölteni: "))
    pez -= koltes
    if pez >=0:
        print(f"ennyi pénzed maradt:{pez}")
    else:
        print("Nincs ennyi pénzed")
        pez += koltes
        print(f"ennyi pénzed maradt:{pez}")
