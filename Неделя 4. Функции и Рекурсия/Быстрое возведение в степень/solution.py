def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a * a, b / 2)
    return a * power(a, b - 1)


x, y = float(input()), int(input())
print(power(x, y))
