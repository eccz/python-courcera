import copy
import sys


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    @staticmethod
    def transposed(obj):
        """Транспонирует марицу не изменяя ее, аля sorted(list)"""
        return Matrix([[obj.copy[j][i] for j in range(len(obj.copy))]
                       for i in range(len(obj.copy[0]))])

    def __init__(self, mlist):
        """Тут можно и без deepcopy"""
        self.copy = copy.deepcopy(mlist)

    def __str__(self):
        """также влияет на print, так как он использует str внутри"""
        all_str = ''
        for elem in self.copy:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str.strip()

    def size(self):
        return len(self.copy), len(self.copy[0])

    def __add__(self, other):
        """Складывает две матрицы между собой, если возможно -
        иначе вываливается с Matrixerror"""
        result = [i for i in self.copy]
        if len(self.copy) == len(other.copy):
            for i, e in enumerate(self.copy):
                for j, k in enumerate(e):
                    result[i][j] += other.copy[i][j]
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(result)

    def __mul__(self, other):
        """Умножает матрицы на все что можно,
        если невозможно вываливается с Matrixerror"""
        temp_list, result = [], []
        if type(other) == int or type(other) == float:
            for i, e in enumerate(self.copy):
                for j, k in enumerate(e):
                    temp_list.append(k * other)
                result.append(temp_list)
                temp_list = []
        elif len(self.copy[0]) == len(other.copy):
            temp = 0
            for z in range(len(self.copy)):
                for j in range(len(other.copy[0])):
                    for i in range(len(self.copy[0])):
                        temp += self.copy[z][i] * other.copy[i][j]
                    temp_list.append(temp)
                    temp = 0
                result.append(temp_list)
                temp_list = []
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        """Транспонирует матрицу изменяя ее, как list.sort()"""
        transposed = [[0 for i in range(len(self.copy))]
                      for j in range(len(self.copy[0]))]
        for i in range(len(self.copy)):
            for j in range(len(self.copy[0])):
                transposed[j][i] = self.copy[i][j]
        self.copy = transposed
        return Matrix(self.copy)


exec(sys.stdin.read())

# Внесите следующие изменение в предыдущую программу:
#
# Измените метод __mul__ таким образом, чтобы матрицы можно было умножать как на скаляры, так и на другие матрицы.
# В случае, если две матрицы перемножить невозможно, то тогда выбросьте ошибку MatrixError.
# Первая матрице в ошибке  —  это self, вторая  —  это второй операнд умножения.
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
# # Task 4 check 1
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(mid * m1)
# print(mid * m2)
# print(m2 * m1)
# try:
#     m = m1 * m2
#     print("WA It should be error")
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
#
# Вывод программы:
# 3	2
# -10	0
# 14	5
# 5.0	2.0	10.0
# -0.5	-0.25	18.0
# -22.0	-2.5	-0.125
# 135	60
# 253.0	89.0
# -42.75	-44.625
# 3	2
# -10	0
# 14	5
# 5	2	10
# -0.5	-0.25	18
# -22	-2.5	-0.125
#
#
#
# Тест 2
# Входные данные:
# # Task 4 check 2
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(0.5 * m2)
# print(m2 * (0.5 * mid * m1))
#
# Вывод программы:
# 2.5	1.0	5.0
# -0.25	-0.125	9.0
# -11.0	-1.25	-0.0625
# 67.5	30.0
# 126.5	44.5
# -21.375	-22.3125
#
#
#
# Тест 3
# Входные данные:
# # Task 4 check 3
# mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
# m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
# m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
# print(5 * m2)
# print(m2 * (120 * mid * m1))
#
# Вывод программы:
# 25	10	50
# -2.5	-1.25	90
# -110	-12.5	-0.625
# 16200	7200
# 30360.0	10680.0
# -5130.0	-5355.0
