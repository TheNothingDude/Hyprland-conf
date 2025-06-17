pez = int(input("Mennyi pénzed van: "))

while pez >0:
    pez -= int(input("Mennyit szeretnél elkölteni: "))
    print(pez)
if pez <0:
    print("")