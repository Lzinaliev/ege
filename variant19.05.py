#print('x y z w')
#for x in range(0,2):
 #   for y in range(0, 2):
 #       for z in range(0, 2):
 #           for w in range(0, 2):
 #               if y and (x <= w) and ((not(x)) <= ((not(w)) == z)):
 #                   print(x,y,z,w)
 #

 #5
#for n in range(0,100):
    #s = bin(n)[2:]
   # s = str(s)
 #   if n % 2 == 0:
  #      s = s + '0'
  #  else:
  #      s = s + '1'
 #   s1 = s[2:]
  #  if s.count('1') % 3 == 0:
 #      s = '11' + s1
  #  else:
  #     s = '10' + s1
 #   r = int(s,2)
#    if r <= 37:
 #     print(n)

from turtle import *

speed(100)
k = 5
left(90)
#penup()
#forward(100*k)
right(90)
#forward(100*k)
right(45)
#pendown()
for i in range(10):
    forward(30*k)
    right(90)
penup()
for x in range(-21,10):
    for y in range(-50,10):
        goto(x*k,y*k)
        dot(3)


done()

#8
#count = 0
#l = '0123'
#for i1 in l:
#    for i2 in l:
#        for i3 in l:
#            for i4 in l:
#                for i5 in l:
#                    x = i1+i2+i3+i4+i5
#                    if (x[0] != '0') and (x.count('3') == 1) and (('30' not in x) and ('03' not in x)):
#                        count += 1
#                        print(x)
#print(count)

#12

#x = '22' + '1'*2050 + '22'
#while ('211' in x) or ('112' in x):
#    x = x.replace('11','1',1)
#    if '21' in x:
#        x = x.replace('21','12',1)
#    else:
#        x = x.replace('12','1',1)
#print(x)

#13

#from ipaddress import *
#count = 0
#network = ip_network('249.0.33.87/255.252.0.0',strict=0)
#for ip in network:
#    s = bin(int(ip))[2:]
#    s1 = s[16:]
#    s2 = s[:16]
#    if s2.count('1') * 2 < s1.count('1'):
#        count += 1
#print(count)

#14
#x = 4**2022 - 6*4**522 + 5 * 64**510-3*2**330-100
#s = ''
#
#while x != 0:
#    s += str(x%8)
#    x = x//8
#x
#print(s.count('7'))

#15
#for a in range(1,301):
 #   k = 0
  #  for x in range(1,301):
    #    if ( (x%20==0) <= (not(x%11==0)) ) or ((x+a) >= 300):
   #         k += 1
   # if k == 300:
   #     print(a)
   #     break

#16

#def f(n):
#    if n < 3:
#        return n
#    if (n > 2) and (n%2 == 0):
#$        return 3*(n-1) + f(n-1) + 5
 #   if (n > 2) and (n%2 != 0):
 #       return 3*(n+1) + f(n-2) -2
#print(f(35))

#17
#f = open('17var06.txt')
#l = []
#max1 = 0
#count = 0
#max2 = 0
#for i in f:
#    i = int(i)
#    l.append(i)
#    if i % 2 == 0:
#        max1 = max(max1,i)
#for j in range(len(l)-1):
#    if l[j] + l[j+1] == max1:
#        count += 1
#        max2 = max(max2,l[j]**2 + l[j+1]**2)

#print(count,max2)



#19
#def f(n,p):
#    if n >= 301 and p == 2:
#        return 1
#    if n < 301 and p==2:
#        return 0
#    if n >= 301 and p < 2:
#        return 0
#    if p % 2 == 0:
#        return f(n+1,p+1) and f(n*2,p+1)
#    else:
#        return f(n + 1, p + 1) or f(n * 2, p + 1)



#for n in range(1,301):
#    if f(n,0) ==1:
#        print(n)
#print('---------------------')
#def f(n,p):
#    if n >= 301 and p == 3:
#        return 1
#    if n < 301 and p==3:
#        return 0
#    if n >= 301 and p < 3:
#        return 0
#    if p % 2 == 0:
#        return f(n+1,p+1) or f(n*2,p+1)
#    else:
#        return f(n + 1, p + 1) and f(n * 2, p + 1)


#for n in range(1,301):
#    if f(n,0) ==1:
#        print(n)

#print('---------------------')

#def f(n,p):
   # if n >= 301 and (p == 2 or p==4):
   #     return 1
   # if n < 301 and p==4:
   #     return 0
   # if n >= 301 and p < 4:
   #     return 0
  #  if p % 2 == 0:
  #      return f(n+1,p+1) and f(n*2,p+1)
  #  else:
  #      return f(n + 1, p + 1) or f(n * 2, p + 1)

#def f1(n,p):
#    if n >= 301 and p == 2:
#        return 1
#    if n < 301 and p==2:
#        return 0
#    if n >= 301 and p < 2:
#        return 0
#    if p % 2 == 0:
#        return f1(n+1,p+1) and f1(n*2,p+1)
#    else:
#        return f1(n + 1, p + 1) or f1(n * 2, p + 1)

#for n in range(1,301):
#$    if f(n,0) ==1:
 #       print(n)


#print('==========')

#for n in range(1,301):
#    if f1(n,0) ==1:
#        print(n)

#23
#def f(x,y):
#    if x < y:
#        return 0
#    if x == y:
#        return 1
#    else:
#        return f(x-1,y) + f(x//2,y)
#print(f(60,10)*f(10,2))


#25

#from fnmatch import *

#for n in range(0,10**8,123):
  # if fnmatch(str(n),'32*823'):
   #     print(n,n//123)



