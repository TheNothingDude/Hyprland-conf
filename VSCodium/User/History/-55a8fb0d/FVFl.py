
def atvaltas(byte, num):
    if byte == "MB":
        return num / 1024
    elif byte =="GB":
        return num * 1024

byte = input("Milyen mértékegységben adod meg(MB/GB): ")
num = int(input("írd be az átváldandó számot: "))


atvaltas
