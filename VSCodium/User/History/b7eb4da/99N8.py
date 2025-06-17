import random 

def harommal_oszthatok(list):
    for i in list:
        if i % 3 == 0:
            return True
        return False

list = []
for i in range(10):
    list.append(random.randint(0,10))
print(list)
print(harommal_oszthatok(list))