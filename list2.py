#Условие Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
list = []
count = 0
n1 = int(input())
while n1 != 0:
    list.append(n1)
    n1 = int(input())
for i in range(1,len(list)-1):
    if list[i-1]<list[i]>list[i+1]:
        count += 1
print(count)

print("-------------------")

list = []
count = 0
n1 = int(input())
while n1 != 0:
    list.append(n1)
    n1 = int(input()) #создание списка

x = int(input())
for i in list: #проходим по всем эл-там списка
    if x>i: #сравниваем с x и если x больше то индекс i
        ind = list.index(i)
print(ind+1) #выводим i