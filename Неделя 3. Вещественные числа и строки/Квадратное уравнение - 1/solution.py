import math

a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d == 0:
    x1 = (-1 * b + math.sqrt(d)) / (2 * a)
    print('{0:.5f}'.format(x1))
elif d > 0:
    x1 = (-1 * b - math.sqrt(d)) / (2 * a)
    x2 = (-1 * b + math.sqrt(d)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    print('{:.6f}'.format(x1), '{:.6f}'.format(x2))
