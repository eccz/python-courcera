import math

n = int(input())
i = 0
sumn = 0
sum_kv = 0
while n != 0:
    sum_kv += n * n
    sumn += n
    i += 1
    n = int(input())
s = math.sqrt((sum_kv - (sumn * sumn / i)) / (i - 1))
print('{0:.6f}'.format(s))
