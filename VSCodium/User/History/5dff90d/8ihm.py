import random

l = []
nyolcvanegy = None
huszonegy_list = []
osszeg = 0
min = 0
max = 0
db = 0
l_b = []
for i in range(346):
    rand = random.randint(-84,322)
    if rand % 7 == 0:
        l.append(rand)
for i in l:
    if i % 81 == 0:
        nyolcvanegy = True
    if i % 21 == 0:
        huszonegy_list.append(i)
    if i > max:
        max = i
    if i < min:
        min = i
    if i % 49 == 0:
        db += 1
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        l_b.append(i)
    osszeg += i
print(f"Az átlag {osszeg/len(l)}")
print(f"A számok összege {osszeg}")
print(f"Legkisebb {min} és a legnagyobb {max}")
print(huszonegy_list)
