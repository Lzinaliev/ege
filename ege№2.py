#1
print("x y z")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if not((x or y) <=(z == x)):
                print(x, y ,z )

print("---------------------------№2-")
#2
print("x y z")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if not((x==z) or (x <=(y and z))):
                print(x, y, z)

print("----------------------------")
#3
print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
               if (((x and not(y)) or (w<=z))==(z==x)):
                   print(x, y, z, w)

print("----------------------------")
#4


