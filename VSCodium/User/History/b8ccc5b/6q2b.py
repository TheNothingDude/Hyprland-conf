def paros(list):
    paros_list = []
    for i in list:
        if i % 2 == 0:
            paros_list.append(i)
    return paros_list

user_input = int(input("Adj meg egy negatív számot: "))
while user_input < 0:
    