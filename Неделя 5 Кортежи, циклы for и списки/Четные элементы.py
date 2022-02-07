# примененяя enumerate

inputlist = list(map(int, input().split()))
for i, e in enumerate(inputlist):
    if e % 2 == 0:
        print(inputlist[i], end=' ')

# обычный вариант
# inputlist = list(map(int, input().split()))
# for i in range(len(inputlist)):
#     if inputlist[i] % 2 == 0:
#         print(inputlist[i], end=' ')
