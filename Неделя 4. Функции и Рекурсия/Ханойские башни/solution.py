def hanoi(n, i, k):  # n - высота пирамиды на 1 столбце, i - столбец с которого перекладываем, k - на который
    if n == 1:
        print('Move Disk 1 from pin', i, 'to', k)
    else:
        tmp = 6 - i - k
        hanoi(n - 1, i, tmp)
        print('Move Disk', n, 'from pin', i, 'to', k)
        hanoi(n-1, tmp, k)


x = int(input())
hanoi(x, 1, 3)
