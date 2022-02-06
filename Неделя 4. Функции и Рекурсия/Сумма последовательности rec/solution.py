def sumseq():
    a = int(input())
    if a != 0:
        a = a + sumseq()
    return a


print(sumseq())
