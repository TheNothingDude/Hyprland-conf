import random 

def harommal_oszthatok(list):
    count = 0
    for i in list:
        if i % 3 == 0:
            count +=1
    return count

list = []
user_imput = int(imput("Adj meg egy számot: "))
while user_imput != "":
    
print(list)
print(harommal_oszthatok(list))