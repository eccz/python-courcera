def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


x, y = float(input()), int(input())
print(power(x, y))
