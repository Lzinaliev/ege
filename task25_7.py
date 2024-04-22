from fnmatch import *

for n in range(0,10**10,3013):
    if fnmatch(str(n),'1?3948*5'):
        print(n)