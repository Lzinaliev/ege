for x in range(0,2031):
    l = x**150-x**100 - x
    s = ''
    while l != 0:
        s = str(l%5) + s
        l = l// 5
    if s.count('0') == 50:
        print(x)
