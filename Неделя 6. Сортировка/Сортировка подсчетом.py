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

# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
# Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
# # Использовать встроенные функции сортировки нельзя.
#
# Входные данные:
# 7 3 4 2 5
#
# Вывод программы:
# 2 3 4 5 7
