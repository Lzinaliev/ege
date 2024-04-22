for N in range(11):
    s = bin(N)[2:]
    if len(s) < 8:
        while len(s) != 8:
            s = "0" + s
    s = s.replace("1","2")
    s = s.replace("0","1")
    s =  s.replace("2","0")
print(s)

