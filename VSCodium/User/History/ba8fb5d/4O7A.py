def pozitivok(l):
    bekeres = int(input("írj be egy számot: "))
    while bekeres >=0:
        l.append (int(bekeres))
        bekeres = int(input("írj be egy számot: "))
    minimum = 9999
    for i in range (len(l)):
        if l[i]<minimum:
            minimum = l[i]
    return minimum
list = []

print(pozitivok(list))