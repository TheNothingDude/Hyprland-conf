import random as r 

def osszegzo(list):
    osszeg = 0
    for  i in list:
        osszeg += i
    return osszeg

list = []

for i in range(10):
    list.append(r.randint(1,50))

osszegzo(list)