from fnmatch import *

for n in range(0,10**10,1991):
    if fnmatch(str(n), '1*4182?7'):
        print(n)