import math


def distance(X1, Y1, X2, Y2):
    X = X2 - X1
    Y = Y1 - Y2
    SUM_TOT = math.sqrt(X*X + Y*Y)
    return SUM_TOT


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
