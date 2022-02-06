def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


x, y = int(input()), int(input())
print(gcd(x, y))
