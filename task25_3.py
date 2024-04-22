from fnmatch import *

for n in range(0,10**10,2023):
    if fnmatch(str(n),'1?493*41'):
        print(n)