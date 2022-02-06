n = int(input())
sumSeq = 0
i = 0
while n != 0:
    sumSeq += n
    i += 1
    n = int(input())
print(sumSeq / i)
