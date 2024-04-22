l = 'дкмо'
x = 0
c = 0
i = 0
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    l2 = i1 + i2 + i3 +i4 + i5
                    x += 1
                    if l2 == 'домок':
                        c = x
                    elif l2 == 'комод':
                        i = x
print(i-c+1)

