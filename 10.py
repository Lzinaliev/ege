#1. Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
n = int(input())
max1 = 0
max2 = 0
while n != 0:
    if n > max1:
        max2 = max1
        max1 = n
    elif n>max2:
        max2 = n
    n = int(input())
print(max2)


print("----------------------------")

#2. Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение  двух наибольших элементов в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
n = int(input())
max1 = 0
max2 = 0
while n != 0:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
    n = int(input())
print(max1, max2)






