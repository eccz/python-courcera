n = int(input())
tuple1 = ()
for i in range(n - 1):
    tuple1 += int(input()),  # ввод прибавляется к кортежу как синглтон (запятая)
for i in range(1, n + 1):
    if i not in tuple1:
        print(i)

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N-1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
