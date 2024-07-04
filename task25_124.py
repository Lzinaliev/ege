from fnmatch import *

for n in range(0,10**10,3023):
    if fnmatch(str(n),'1?954*21'):
        print(n)