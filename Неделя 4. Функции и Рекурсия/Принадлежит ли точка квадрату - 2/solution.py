def isPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


x, y = float(input()), float(input())
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
