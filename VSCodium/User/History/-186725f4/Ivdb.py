list = []
talalat = False
user_input = input("Adj meg egy betüt: ")
while user_input != "":
    for i in list:
        if i == user_input:
            talalat = True
    if talalat == True:
        print("Már található a listába")
    else:
        list.append(user_input)
    user_input = input("Adj meg egy betüt: ")
    talat = False
print(list)