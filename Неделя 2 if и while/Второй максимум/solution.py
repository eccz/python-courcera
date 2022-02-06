n = int(input())
maxSeq1 = 0
maxSeq2 = 0
while n != 0:
    if n >= maxSeq2:
        maxSeq1 = maxSeq2
        maxSeq2 = n
    elif n >= maxSeq1 and n < maxSeq2:
            maxSeq1 = n
    n = int(input())
print(maxSeq1)
