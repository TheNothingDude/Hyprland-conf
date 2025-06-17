import random 

def harommal_oszthatok(list):
    count = 0
    for i in list:
        if i % 3 == 0:
            count +=1
    return count

list = []
user_imput = 1
while user_imput !=0 or user_imput == None:
    user_imput = int(input("Adj meg egy sztámot: "))
    
    

print(list)
print(harommal_oszthatok(list))