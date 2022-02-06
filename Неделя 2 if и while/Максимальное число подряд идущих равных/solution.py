n = int(input())
i1, i2 = 0, 0
dif1 = n
while n != 0:
    if dif1 == n:
        i1 += 1
    else:
        dif1 = n
        if i1 > i2:
            i2 = i1
        i1 = 1
    n = int(input())
print(max(i1, i2))
