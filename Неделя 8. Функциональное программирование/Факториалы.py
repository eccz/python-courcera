import math

print(
    *map(
        math.factorial,
        range(int(input()) + 1)
    )
)
# from itertools import accumulate
#
# print(
#     *accumulate(
#         map(
#             lambda x: max(x, 1),
#             map(
#                 int,
#                 range(int(input()) + 1))
#         ),
#         lambda x, y: x * y
#     )
# )
# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов:
# 0!,1!,2!,…,n!
#
# Формат ввода
# Вводится число n.
#
# Формат вывода
# Выведите последовательность факториалов, разделяя числа пробелами
#
# Тест 1
# Входные данные:
# 4
#
# Вывод программы:
# 1 1 2 6 24
