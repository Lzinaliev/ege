#Напишите программу, которая в последовательности натуральных чисел определяет сумму чисел, кратных 6. Программа получает на вход количество чисел в последовательности, а затем сами числа.

n = int(input())
sum = 0
for i in range(n):
    n1 = int(input())
    if(n1 % 6 == 0):
         sum += n1
print(sum)


print("--------------------")

#Напишите программу, которая в последовательности натуральных чисел определяет сумму чисел, кратных 6 и оканчивающихся на 4. Программа получает на вход количество чисел в последовательности, а затем сами числа.
n = int(input())
sum = 0
for i in range(n):
    n1 = int(input())
    if n1 % 6 == 0 and n1 % 10 == 4:
         sum += n1
print(sum)

print("--------------------")

#Напишите программу, которая в последовательности натуральных чисел определяет количество чисел, четных чисел и оканчивающихся на 6. Программа получает на вход количество чисел в последовательности, а затем сами
n = int(input())
sum = 0
for i in range(n):
    n1 = int(input())
    if n1 % 10 == 6 and n1 % 2 == 0:
        sum += n1
print(sum)

print("--------------------")

