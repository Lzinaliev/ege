print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((y <= x) == (x <= w)) and (z or x):
                    print(x, y, z, w)
print('ywxz')