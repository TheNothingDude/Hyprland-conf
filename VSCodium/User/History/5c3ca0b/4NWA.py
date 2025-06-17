import random

l = []
tizenkilenc = None
osszeg = 0
tizenhet = []
db = 0
l_b = []
for i in range(300):
    rand = random.randint(-500,500)
    if rand % 2 == 0:
        l.append(rand)
min = l[0] 
max = l[0]
for i in l:
    if i % 19 == 0:
        tizenkilenc = True
    if i % 17 == 0:
        tizenhet.append(i)
    if i > max:
        max = i
    if i < min:
        min = i
    if i % 6 == 0:
        db += 1
    if i % 2 == 0 or i % 3 == 0 or i % 5 ==0:
        l_b.append(i)
        
    osszeg += i
if tizenkilenc == True:
    print("Van benne 19-cel oszthato")
print(tizenhet)
print(osszeg)
print(f"Az átlag {osszeg/len(l)}")
print(f"Legkisebb {min} és a legnagyobb {max}")
print(f"{db} 6-tal osztható szám van")