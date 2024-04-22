a = input()
b = input()
for i in range(len(a)):
    if a[i] != b[i]:
        print(b[i])
        break
else:
    print(b[-1])