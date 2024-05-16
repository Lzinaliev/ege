def delit(h):
    a = [1]
    for d in range(2,int(h**0.5)+1):
        if h % d == 0:
            a.append(d)
            if h//d != d:
                a.append(h//d)
    a.sort()
    return a
