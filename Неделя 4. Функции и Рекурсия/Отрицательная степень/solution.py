def power(a, n):
    i = n
    c = 1
    if n == 0:
        return c
    elif n > 0:
        c = a
        while i != 1:
            c = c * a
            i -= 1
        return c
    elif n < 0:
        c = 1 / a
        while i != -1:
            c = c * (1 / a)
            i += 1
        return c


x, y = float(input()), int(input())
print(power(x, y))
