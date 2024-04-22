#coding: utf-8
count = 0
l = 'бронхи'
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                x = i1+ i2 +i3 +i4
                if x.count('х') == 1:
                    count += 1
print(count)