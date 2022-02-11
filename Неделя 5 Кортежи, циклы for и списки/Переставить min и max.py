# вот это сдал:
# inputlist = list(map(int, input().split()))
# maxelement = max(inputlist)
# minelement = min(inputlist)
# k, j = 0, 0
# for i, e in enumerate(inputlist):
#     if e == maxelement:
#         j = i
#     if e == minelement:
#         k = i
# inputlist[j], inputlist[k] = inputlist[k], inputlist[j]
# print(*inputlist)

# В списке все элементы попарно различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Вводится список целых чисел. Все числа списка находятся на одной строке.
# Выведите ответ на задачу.

# а это с index()
inputlist = list(map(int, input().split()))
indexmax = inputlist.index(max(inputlist))
indexmin = inputlist.index(min(inputlist))
inputlist[indexmin], inputlist[indexmax] = inputlist[indexmax], inputlist[indexmin]
print(*inputlist)
