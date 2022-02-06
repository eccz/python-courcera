def xor(x, y):
    return (x == 1 and y == 0) or (x == 0 and y == 1)


x, y = int(input()), int(input())
if xor(x, y):
    print('1')
else:
    print('0')
