# этот вариант я сдал:

# inputlist = list(input().split())
# for i in range(len(inputlist)):
#     if i % 2 == 0:
#         print(inputlist[i], end=' ')

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# Программа должна быть эффективной и не выполнять лишних действий
# Вводится список чисел. Все числа списка находятся на одной строке.

# тут то же самое с применением enumerate, из видоса про ошибки с применением range(len(list)):

inputlist = list(input().split())
for i, e in enumerate(inputlist):
    if i % 2 == 0:
        print(inputlist[i], end=' ')

print(*input().split()[::2])  # а это в одну строку
