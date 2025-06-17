list = []

def valtozo(list):
    user_input= input("Adj meg egy számot: ")
    while user_input != "":
        list.append(int(user_input))
        user_input= input("Adj meg egy számot: ")
    return list
print(valtozo(list))