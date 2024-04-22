#48
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((x and not(y)) == (z or not(w))) <= (x and z)):
                    print(x, y, z, w)
print("ответ: y z w x")

print("----------------------------")

#56
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((y <= x) and (z or w)) <= ((x and not(w)) or (y == z))):
                    print(x, y, z, w)

print("ответ: z w y x")

print("----------------------------")
#56.1

import itertools

print("x y z w")
for x, y, z, w in itertools.product(range(2), repeat=4): #Конструкция itertools.product(range(2), repeat=4) создает итератор,
    if not(((y <= x) and (z or w)) <= ((x and not(w)) or (y == z))): # который генерирует все возможные комбинации из значений, взятых из диапазона range(2), повторяя каждое значение 4 раза.
        print(x, y, z, w)

print("----------------------------")

#19
print("функция равна 1")
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((y <= w)== (x <= (not z))) and (x or w):
                    print(x, y, z, w)
print("функция равна 0")
print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if not(((y <= w)==(x <= (not z))) and (x or w)):
                    print(x, y, z, w)



