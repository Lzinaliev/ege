#max Дана последовательность из N элементов. Элементы вводятся с клавиатуры. Числа в диапазоне от -100 до 100 включительно. Найти максимум.
n = int(input())
max = -101
for i in range(n):
    n1 = int(input())
    if n1>max:
        max = n1
print(max)
print("----------------------------")
#max while
n = int(input())
i = 1
max = -101
while i<=n:
    n1 = int(input())
    i += 1
    if n1>max:
        max = n1
print(max)
print("----------------------------")


