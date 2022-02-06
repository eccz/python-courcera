def isPointInArea(x, y):
    x1, y1, x2, y2 = -1, 0, 0, 2
    x3, y3, x4, y4 = -1, 1, 0, 0
    xc, yc, r = -1, 1, 2
    xy1 = (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)
    xy2 = (x4 - x3) * (y - y3) - (x - x3) * (y4 - y3)
    c = ((xc - x) ** 2 + (yc - y) ** 2) ** 0.5
    return xy1 >= 0 and xy2 >= 0 and c <= r or \
        xy1 <= 0 and xy2 <= 0 and c >= r


x, y = float(input()), float(input())
if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
