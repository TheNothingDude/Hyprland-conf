import random

l = []
tizenketto = None
huszomharom_list = []
osszeg = 0
db = 0
l_b = []
for i in range(500):
    rand = random.randint(0,739)
    if rand % 2 != 0:
        l.append(rand)
min = l[0]
max = l[0]
for i in l:
    if i % 12 == 0:
        tizenketto = True
    if i % 23 == 0:
        huszomharom_list.append(i)
    osszeg += i
    if i > max:
        max = i
    if i < min:
        min = i
    if i % 13 == 0:
        db += 1
    if i % 7 == 0 or i % 3 == 0:
        l_b.append(i)
print(f"Az átlag {osszeg/len(l)}")
print(osszeg)
print(f"Legkisebb {min} és a legnagyobb {max}")
print(l_b)
