print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x == (w or y)) or ((w <= z) and (y <= w))):
                    print(x, y, z, w)
print("yxzw")