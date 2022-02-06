import math

n = float(input())
if n % 1 >= 0.5:
    n = math.ceil(n)
else:
    n = math.floor(n)
print(n)
