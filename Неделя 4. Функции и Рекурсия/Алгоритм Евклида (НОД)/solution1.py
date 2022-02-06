def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    elif a % b != 0:
        return gcd(a - b, b)
    return b


x, y = int(input()), int(input())
print(gcd(x, y))
