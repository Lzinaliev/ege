k = 0
for n in range(128, 256):
    for m in range(256):
        if m % 4 == 0:
            k += 1
print(k)
