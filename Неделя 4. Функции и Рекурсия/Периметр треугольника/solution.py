import math


def distance(X1, Y1, X2, Y2):
    X = X2 - X1
    Y = Y1 - Y2
    SUM_TOT = math.sqrt(X*X + Y*Y)
    return SUM_TOT


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
o1 = distance(x1, y1, x2, y2)
o2 = distance(x1, y1, x3, y3)
o3 = distance(x2, y2, x3, y3)
print('{0:.5f}'.format(o1 + o2 + o3))
