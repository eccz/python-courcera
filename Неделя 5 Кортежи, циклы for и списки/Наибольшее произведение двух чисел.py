# Долгий алгоритм:
# inputlist = list(map(int, input().split()))
# indexi, indexj, mult = int, int, 0
# for i, e in enumerate(inputlist):
#     for j, k in enumerate(inputlist):
#         if e * k > mult and i != j:
#             mult = e * k
#             indexi = i
#             indexj = j
# if inputlist[indexi] > inputlist[indexj]:
#     print(inputlist[indexj], inputlist[indexi])
# else:
#     print(inputlist[indexi], inputlist[indexj])

#  А этот быстрый
inputlist = list(map(int, input().split()))
max1 = max(inputlist)
min1 = min(inputlist)
inputlist.remove(max1)
inputlist.remove(min1)
max2 = max(inputlist)
min2 = min(inputlist)
if max1 * max2 > min1 * min2:
    print(min(max1, max2), max(max1, max2))
else:
    print(min(min1, min2), max(min1, min2))

# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.
# Выведите эти числа в порядке неубывания.
#
# Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку использовать нельзя.
