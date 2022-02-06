a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
if (a == a1 and b == b1 and c == c1) \
        or (a == a1 and c == b1 and b == c1) \
        or (b == a1 and a == b1 and c == c1) \
        or (b == a1 and c == b1 and a == c1) \
        or (c == a1 and a == b1 and b == c1) \
        or (c == a1 and b == b1 and a == c1):
    print('Boxes are equal')
elif (a >= a1 and b >= b1 and c >= c1) \
        or (a >= a1 and c >= b1 and b >= c1) \
        or (b >= a1 and a >= b1 and c >= c1) \
        or (b >= a1 and c >= b1 and a >= c1) \
        or (c >= a1 and a >= b1 and b >= c1) \
        or (c >= a1 and b >= b1 and a >= c1):
    print('The first box is larger than the second one')
elif (a <= a1 and b <= b1 and c <= c1) \
        or (a <= a1 and c <= b1 and b <= c1) \
        or (b <= a1 and a <= b1 and c <= c1) \
        or (b <= a1 and c <= b1 and a <= c1) \
        or (c <= a1 and a <= b1 and b <= c1) \
        or (c <= a1 and b <= b1 and a <= c1):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
