def isPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


x, y = float(input()), float(input())
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
