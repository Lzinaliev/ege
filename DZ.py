#min Дана последовательность, оканчивающаяся 0. Элементы вводятся с клавиатуры. Числа в диапазоне от -100 до 100 включительно. Найти минимум.
n = int(input())
min = 101
while n != 0:
    if n<min:
        min = n
    n = int(input())
print(min)

print("----------------------------")

# Определите кол-во элементов , оканчивающихся на 6 и не кратынх 3. Последовательность завершается числом 0.
a=int(input())
k=0
while a!=0:
    if a%10==6 and a%3 !=0:
        k+=1
    a = int(input())
print(k)