x = 4**14+2**32-4
s = str(bin(x)[2:]).count('1')
print(s)