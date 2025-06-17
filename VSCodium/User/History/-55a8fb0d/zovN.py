
def atvaltas(byte, num):
    if byte == "MB":
        return f"{round(num / 1024,1)} GB"
    elif byte =="GB":
        return f"{num * 1024} MB"

byte = input("Milyen mértékegységben adod meg(MB/GB): ")
num = int(input("írd be az átváldandó számot: "))

print(atvaltas(byte, num))
