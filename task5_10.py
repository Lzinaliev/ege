for N in range(102,0,-1):
    s = bin(N)[2:]
    if N % 2 == 0:
        s += "10"
    else:
        s += "01"
    R = int(s,2)
    if R <= 102:
        print(R)
        break


