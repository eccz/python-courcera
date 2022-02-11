# сдал, но только для упорядоченной последовательности:
inputlist = list(map(int, input().split()))
count = 1
for i, e in enumerate(inputlist[1::]):
    if e != inputlist[i]:
        count += 1
print(count)

# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# Вводится список чисел. Все числа списка находятся на одной строке.
# Выведите ответ на задачу.
#
# Входные данные:
# 1 2 2 3 3 3
#
# Вывод программы:
# 3

# для неупорядоченной:
# int_list = list(map(int, input().split()))
# x = []
# for i in int_list:
#     if i not in x:
#         x.append(i)
# print(len(x))
