from fnmatch import *

for n in range(0,10**9,9517):
    if fnmatch(str(n), '2*41*6?9'):
        print(n)