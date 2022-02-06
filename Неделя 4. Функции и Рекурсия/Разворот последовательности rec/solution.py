def revseq(a):
    n = int(input())
    if n == 0:
        print(0)
    else:
        revseq(n)
        print(n)


revseq(1337)
