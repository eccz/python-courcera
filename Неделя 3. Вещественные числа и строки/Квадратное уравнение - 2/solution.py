import math

a, b, c = float(input()), float(input()), float(input())
if a == b == c == 0:
    print(3)
elif a == b == 0:
    print('0')
elif a == 0:
    x1 = (-1 * c / b)
    print(1, x1)
d = b * b - 4 * a * c
if d < 0 and a != 0:
    print(0)
elif d == 0 and a != 0:
    x1 = (-1 * b + math.sqrt(d)) / (2 * a)
    print(1, '{0:.6f}'.format(x1))
elif d > 0 and a != 0:
    x1 = (-1 * b - math.sqrt(d)) / (2 * a)
    x2 = (-1 * b + math.sqrt(d)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    print(2, '{:.6f}'.format(x1), '{:.6f}'.format(x2))
