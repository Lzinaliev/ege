# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
list = []
count = 0
n1 = int(input())
while n1 != 0:
    list.append(n1)
    n1 = int(input())

count = 1
for i in range(1, len(list)):
    #если элементы не равны добавляем в переменную 1
    if list[i] != list[i-1]:
        count += 1
print(count)

print("-------------------")

#2
list = []
count = 0
n1 = int(input())
while n1 != 0:
    list.append(n1)
    n1 = int(input())
count = len(set(list))
print(count)

print("-------------------")

#Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(list)-1, 2):  # цикл для прохода по индексам элементов с шагом 2
    list[i], list[i+1] = list[i+1], list[i]  # меняем местами соседние элементы
print(list)



