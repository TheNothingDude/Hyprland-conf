import random

lmagas = []
lsuly = []
#magasság
atlag_alatt = 0
atlag_felett = 0

def minmax(list, melyik):
    max_val = list[0]
    min_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    if melyik == "max":
        return max_val
    else:
        return min_val
def indexfind(val, list):
    j = 0
    index = -1
    while index == -1 and j < len(list):
        if list[j] == val:
            index = j
        j += 1
    return index


for i in range(32):
    lmagas.append(random.randint(130,190))
min_val =  minmax(lmagas, "min")
max_val = minmax(lmagas, "max")
osszeg = 0
for i in lmagas:
    osszeg += i
min_index = indexfind(min_val, lmagas)
max_index = indexfind(max_val, lmagas)
atlag = osszeg/ len(lmagas)
for i in lmagas:
    if i > atlag:
        atlag_felett += 1
    if i< atlag:
        atlag_alatt += 1
print(f"A magasságok összege {osszeg}")
print(f"A magasságok átlaga {osszeg/len(lmagas)}")
#Suly
for i in range(32):
    lsuly.append(random.randint(38,96))

atlag_alatt = 0
atlag_felett = 0
osszeg = 0
for i in lsuly:
    osszeg += i
min_val_suly = minmax(lsuly, "min")
max_val_suly = minmax(lsuly, "max")
max_index_suly = indexfind(max_val, lsuly)
min_index_suly = indexfind(min_val, lsuly)
atlag = osszeg/ len(lsuly)
for i in lsuly:
    if i > atlag:
        atlag_felett += 1
    if i< atlag:
        atlag_alatt += 1 
l_bmi = []
for i in range(32):
    l_bmi.append((lsuly[i]/(lmagas[i]*lmagas[i]))*10000)
min_bmi = minmax(l_bmi, "min")
max_bmi = minmax(l_bmi, "max")
min_index_bmi = indexfind(min_bmi, l_bmi)
max_index_bmi = indexfind(max_bmi, l_bmi)
osszeg_bmi =0
for i in l_bmi:
    osszeg += i
atlag_bmi = (osszeg/len(l_bmi))
print(l_bmi)
print(atlag)
