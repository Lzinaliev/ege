#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
list = [1,2,3,4,5,6,7,8,9]
index_max = 0
index_min = 0
for i in range(len(list)):
    if list[i] > list[index_max]:
        index_max = i
    if list[i] < list[index_min]:
        index_min = i
list[index_min] , list[index_max] = list[index_max] , list[index_min]
print(list)

#Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
list = [1,2,3,4,5,6,7,8,9]
k = int(input())
for i in range(k,len(list)-1):
    list[i] = list[i+1]
list.pop(len(list)-1)
print(list)