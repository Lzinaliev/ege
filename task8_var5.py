l = '01234567'
count = 0
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    x = i1+i2+i3+i4+i5
                    if x.count('4') == 2:
                        if (x[0] != '0') and ('41' not in x) and ('43' not in x) and ('45' not in x) and ('47' not in x):
                            if ('14' not in x) and ('34' not in x) and ('54' not in x) and ('74' not in x):
                                count += 1
print(count)