n = int(input())
maxSeq = 0
i = 0
while n != 0:
    if n > maxSeq:
        maxSeq = n
        i = 1
    elif n == maxSeq:
        i += 1
    n = int(input())
print(i)
