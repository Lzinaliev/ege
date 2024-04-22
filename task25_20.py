from fnmatch import *

for n in range(0,10**10,2024):
    if fnmatch(str(n),'1?2157*4'):
        print(n,n//2024)