
def f(n):
    flag = 0
    for j in range(2,n):
        if n % j == 0:
            flag = 1
            break
    if flag == 0:
        return 1
    else:
        return 0

s = '10 2 4 6 1 58 52 123 5 32 51 63 7 11 17 18'
l = s.split()
for i in l:
    if (f(int(i)) == 1) and (int(i) != 1):
        print(i)