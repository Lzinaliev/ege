#В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

x = int(input())
y = int(input())
i = 1

while x<y:
    x *= 1.1
    i += 1
print(i)

#ДЗ 2: По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
n = int(input())
i = 0
d = 1
while d*2 <=n:
    d *= 2
    i+=1
print(i,d)
#Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
n = int(input())
sum = 0
while n != 0:
    sum += n
    n = int(input())
print(sum)