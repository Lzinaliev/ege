from fnmatch import *

for n in range(0,10**8,2622):
    if fnmatch(str(n), "1?4*6?8"):
        print(n,n//2622)