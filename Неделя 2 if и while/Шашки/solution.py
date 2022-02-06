x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1 + x2 + y2) % 2 == 0 and y2 > y1 and (y2 - y1) >= abs(x2 - x1):
    print('YES')
else:
    print('NO')
