import random 

def harommal_oszthatok(list):
    count = 0
    for i in list:
        if i % 3 == 0:
            count +=1
    return count

list = []
for i in range(10):
    list.append(random.randint(1,10))
print(list)
print(harommal_oszthatok(list))