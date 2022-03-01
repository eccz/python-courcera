def count_sort(a):
    countlist = [0] * 101
    output = []
    for now in a:
        countlist[now] += 1
    for i, e in enumerate(countlist):
        for j in range(e):
            output.append(i)
    return output


inputlist = list(map(int, input().split()))
print(*count_sort(inputlist))
