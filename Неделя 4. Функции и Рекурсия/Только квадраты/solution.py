def onlysq(i):
    n = int(input())
    if n == 0:
        if i == 0:
            print(0)
        return
    elif (n**0.5) % 1 == 0:
        onlysq(i + 1)
        print(n, end=' ')
    else:
        onlysq(i)


onlysq(0)
