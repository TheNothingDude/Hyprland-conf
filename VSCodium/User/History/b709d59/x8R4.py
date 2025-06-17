import random 

def paros_e(list):
    for i in list:
        if i % 2 == 0:
            return True
    return False

list = []
for i in range(10):
    list.append(random.randint(0,1))
print(list)
print(paros_e(list))