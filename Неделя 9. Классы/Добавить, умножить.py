import copy
import sys


class Matrix:
    def __init__(self, mlist):
        self.copy = copy.deepcopy(mlist)

    def __str__(self):
        all_str = ''
        for elem in self.copy:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str.strip()

    def size(self):
        return len(self.copy), len(self.copy[0])

    def __add__(self, other):
        all_str = ''
        for i, e in enumerate(self.copy):
            for j, k in enumerate(e):
                all_str += f'{k + other.copy[i][j]}\t'
            all_str += '\n'
        return all_str.strip()

    def __mul__(self, other):
        all_str = ''
        for i, e in enumerate(self.copy):
            for j, k in enumerate(e):
                all_str += f'{k * other}\t'
            all_str += '\n'
        return all_str.strip()

    __rmul__ = __mul__


exec(sys.stdin.read())

# Добавьте в предыдущий класс следующие методы: см задачу Класс
#
#  __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#
#  __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#
#  __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
#  Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
#
# Иллюстрация:
#
#  В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.
#
#  В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа):
#  10 * Matrix([[0, 1], [1, 0]).
#
# Разумеется, данные методы не должны менять содержимое матрицы.
#
# Формат ввода
#
# Как в предыдущей задаче.
#
# Формат вывода
#
# Как в предыдущей задаче.
# Тест 1
# Входные данные:
# # Task 2 check 1
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m.size())
#
# Вывод программы:
# (3, 2)
#
#
#
# Тест 2
# Входные данные:
# # Task 2 check 2
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# Вывод программы:
# 1	1	0
# 20	1	-1
# -1	-2	1
#
#
#
# Тест 3
# Входные данные:
# # Task 2 check 3
# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
# alpha = 15
# print(m * alpha)
# print(alpha * m)
#
# Вывод программы:
# 15	15	0
# 0	30	150
# 150	225	450
# 15	15	0
# 0	30	150
# 150	225	450
