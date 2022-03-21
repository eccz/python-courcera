import copy
import sys


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    @staticmethod
    def transposed(obj):
        return Matrix([[obj.copy[j][i] for j in range(len(obj.copy))]
                       for i in range(len(obj.copy[0]))])

    def __init__(self, mlist):
        self.copy = copy.deepcopy(mlist)

    def __str__(self):  # также влияет на print, так как он использует str внутри
        all_str = ''
        for elem in self.copy:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str.strip()

    def size(self):
        return len(self.copy), len(self.copy[0])

    def __add__(self, other):
        all_str = ''
        if len(self.copy) == len(other.copy):
            for i, e in enumerate(self.copy):
                for j, k in enumerate(e):
                    all_str += f'{k + other.copy[i][j]}\t'
                all_str += '\n'
        else:
            error = MatrixError(self, other)
            raise error
        return all_str.strip()

    def __mul__(self, other):
        all_str = ''
        for i, e in enumerate(self.copy):
            for j, k in enumerate(e):
                all_str += f'{k * other}\t'
            all_str += '\n'
        return all_str.strip()

    __rmul__ = __mul__

    def transpose(self):
        transposed = [[0 for i in range(len(self.copy))]
                      for j in range(len(self.copy[0]))]
        for i in range(len(self.copy)):
            for j in range(len(self.copy[0])):
                transposed[j][i] = self.copy[i][j]
        self.copy = transposed
        return Matrix(self.copy)


exec(sys.stdin.read())

# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
#
# В класс Matrix внесите следующие изменения:
#
#  Добавьте в метод __add__ проверку на ошибки в размере входных данных,
#  чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом,
#  чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self),
#  а matrix2  —  вторым (второй операнд для сложения).
#
#  Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
#  (данный метод модифицирует экземпляр класса Matrix)
#
#  Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.
#
# Формат ввода
#
# Как в предыдущей задаче.
#
# Формат вывода
#
# Как в предыдущей задаче.
#
# Тест 1
# Входные данные:
# # Task 3 check 1
# # Check exception to add method
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# try:
#     m = m1 + m2
#     print('WA\n' + str(m))
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
#
# Вывод программы:
# 1	1	0
# 20	1	-1
# -1	-2	1
# 1	0	0
# 0	1	0
# 0	0	1
# 0	1	0
# 20	0	-1
#
#
#
# Тест 2
# Входные данные:
# # Task 3 check 2
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m)
# m1 = m.transpose()
# print(m)
# print(m1)
#
# Вывод программы:
# 10	10
# 0	0
# 1	1
# 10	0	1
# 10	0	1
# 10	0	1
# 10	0	1
#
#
#
# Тест 3
# Входные данные:
# # Task 3 check 3
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m)
# print(Matrix.transposed(m))
# print(m)
#
# Вывод программы:
# 10	10
# 0	0
# 1	1
# 10	0	1
# 10	0	1
# 10	10
# 0	0
# 1	1
