from fnmatch import *
for n in range(0,10**8,273):
    if fnmatch(str(n),'12??36*1'):
        print(n,n//273)