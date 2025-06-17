import random 

def harommal_oszthatok(list):
    count = 0
    for i in list:
        if i % 3 == 0:
            count +=1
    return count

list = []
user_imput = 0
while user_imput != \n:
    user_imput = int(input("Adj meg egy sztámot: "))
    list.append(user_imput)
    

print(list)
print(harommal_oszthatok(list))