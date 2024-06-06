from fnmatch import *
for s in range(0,10**10,1917):
    if fnmatch(str(s),'3?12?14*5'):
        print(s,s//1917)