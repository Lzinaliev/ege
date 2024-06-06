#coding: utf-8

#2
#print('x y z w')
#for x in range(0,2):
 #   for y in range(0, 2):
  #      for z in range(0, 2):
   #         for w in range(0, 2):
    #            if not(not(w <= x) or (not(z) <= (not(y))) or (z)):
     #               print(x,y,z,w)

#5
#def f4(n):
 #   s = ''
  #  while n != 0:
   #     s += str(n % 4)
    #    n = n // 4
    #return s[::-1]
#
#
#for n in range(1,1000):
 #   n4 = f4(n)
  #  if n % 4 == 0:
   #     n4 += n4[-2:]
    #else:
     #   ost = n % 4
    #    ost4 = f4(ost*2)
     #   n4 += ost4
   # r = int(n4, 4)
   # if r >= 1088:
    #    print(n)
     #   break


#8
#from itertools import *

#a = 'агеилнрт'
#l = product(a,repeat=5)
#for x in l:
#    s = ''.join(x)




#12

#for n in range(4,10001):
 #   x = '4' + '1'*n
  #  while ('31' in x) or ('411' in x) or ('1111' in x):
   #     if '31' in x:
    #        x = x.replace('31','1',1)
     #   if '411' in x:
      #      x = x.replace('411','13',1)
#        if '1111' in x:
 #           x = x.replace('1111','4',1)
#
 #   sum1 = 0
  #  for i in range(len(x)):
   #     sum1 += int(x[i])
    #if sum1 == 34:
     #   print(n)
      #  break
#13
#count = 0
#from ipaddress import *
#
#network = ip_network('253.112.169.12/255.255.254.0', strict=0)
#
#for ip in network:
#    ip = bin(int(ip))[2:]
#    s1 = ip[:16]
#    s2 = ip[16:]
#    if s1.count('1') <= s2.count('1'):
#        count += 1
#print(count)

#14
#for x in '0123456789ABCDEFGH':
 #   s = int('3' + str(x) + '2' + str(x) + '1' + str(x) + '0' + str(x) + '1',19) + int(str(x) + '2024', 19) + int('1' + str(x) + '077', 19)
  #  if s % 18 == 0:
   #     print(s//18)

#15
#for a in range(1,301):
 #   k = 0
 #   for x in range(1,301):
 #       for y in range(1,301):
 #           if (x >= 20) or (y >= 40) or (y <= x + a) or (y >= 3*x - a):
 #               k += 1
 #   if k == 300*300:
 #       print(a)
  #      break

#16
#from sys import *

#setrecursionlimit(2500)

#def f(n):
#   if n == 1:
#       return 1
#   if n == 2:
#       return 2
#   if n > 2:
#       return n * (n-1) + f(n-1) - f(n-2)

#sum1 = f(2024) + f(2020)
#print(sum1)

#19
#012
#$pv

#def f(n,p):
 #   if n >= 105 and p == 2:
  #      return 1
   # if n < 105 and p == 2:
    #    return 0
 #   if n >= 105 and p < 2:
 #       return 0
 #   if p % 2 == 0:
 #       return f(n+1,p+1) and f(n+5,p+1) and f(n*4,p+1)
 #   else:
 #       return f(n + 1, p + 1) or f(n + 5, p + 1) or f(n * 4, p + 1)
#
#for n in range(1,105):
#    if f(n,0) == 1:
#        print(n)
#        break
#
#print('----------------')
#
#def f(n,p):
#    if n >= 105 and p == 3:
#        return 1
#    if n < 105 and p == 3:
#        return 0
#    if n >= 105 and p < 3:
#        return 0
#    if p % 2 == 0:
#        return f(n+1,p+1) or f(n+5,p+1) or f(n*4,p+1)
#    else:
#        return f(n + 1, p + 1) and f(n + 5, p + 1) and f(n * 4, p + 1)
#
#for n in range(1,105):
 #   if f(n,0) == 1:
  #      print(n)
#
#print('----------------')
#
#def f(n,p):
 #   if n >= 105 and (p == 2 or p==4):
  #      return 1
   # if n < 105 and p == 4:
    #    return 0
    #if n >= 105 and p < 4:
     #   return 0
    #if p % 2 == 0:
    #    return f(n+1,p+1) and f(n+5,p+1) and f(n*4,p+1)
    #else:
    #    return f(n + 1, p + 1) or f(n + 5, p + 1) or f(n * 4, p + 1)

#for n in range(1,105):
#    if f(n,0) == 1:
#        print(n)

#print('===================')
#
#def f1(n,p):
#    if n >= 105 and p == 2:
#        return 1
#    if n < 105 and p == 2:
#        return 0
#    if n >= 105 and p < 2:
#        return 0
#    if p % 2 == 0:
#        return f1(n+1,p+1) and f1(n+5,p+1) and f1(n*4,p+1)
#    else:
#        return f1(n + 1, p + 1) or f1(n + 5, p + 1) or f1(n * 4, p + 1)

#for n in range(1,105):
#    if f1(n,0) == 1:
#        print(n)

#25

#from fnmatch import *

#for s in range(0,10**8,3377):
#    if fnmatch(str(s),'?79?8*3'):
#        print(s,s//3377)

#23

def f(x,y):
   if x > y or x == 21:
     return 0
   elif x == y:
     return 1
   else:
       return f(x+2,y) + f(x+3,y) + f(x*5,y)

x = f(1,6)* f(6,35)
print(x)
