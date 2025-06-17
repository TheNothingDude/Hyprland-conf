import random

lmagas = []
lsuly = []
#magasság
atlag_alatt = 0
atlag_felett = 0
osszeg = 0

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
print(min_val)
print(min_index)
#Suly
for i in range(32):
    lsuly.append(random.randint(38,96))

atlag_alatt = 0
atlag_felett = 0
osszeg = 0
index_min = -1
index_max = -1
j = 0
min_val = lsuly[0] 
max_val = lsuly[0]
for i in lsuly:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
    osszeg += i
while index_min == -1 and j < len(lsuly):
    if lsuly[j] == min_val:
        index_min = j
    j += 1
j = 0
while index_max == -1 and j < len(lsuly):
    if lsuly[j] == max_val:
        index_max = j
    j += 1
atlag = osszeg/ len(lsuly)
for i in lsuly:
    if i > atlag:
        atlag_felett += 1
    if i< atlag:
        atlag_alatt += 1    

    