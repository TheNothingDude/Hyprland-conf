with open("/home/thenothingdude/Code/pa/pilotak.csv", encoding="utf-8") as s:
    line_c = 0
    c = 0
    smallest = 9999
    s.readline()
    for i in s:
        line_c +=1
    print(f"Hármas feladat: {line_c}")
    s.seek(0)
    s.readline()
    for i in s:
        c +=1
        if c == line_c:
            l_line = i.strip().split(";")
            l_name = l_line[0]
    print(f"Négyes feladat: {l_name}")  
    s.seek(0)
    s.readline()
    print("Ötös feladat: ")
    for i in s: 
        line = i.strip().split(";")
        if len(line) ==4:
            rajtszam = line[3]
            if rajtszam:
                if rajtszam < smallest:
                    smallest = rajtszam
        if len(line) == 4:
            if int(line[3]) == smallest:
                s_nas = line[2]
        date = line[1].split(".")
        if int(date[0]) < 1901:
            print(f" \t{line[0]} ({date[0]}.{date[1]}.{date[2]})")
    print(f"Hatodik feladat: {s_nas}")

    

  