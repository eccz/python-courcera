a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
root_count = 0
for i in range(0, 1001):
    if i != e and (a * i**3 + b * i**2 + c * i + d) / (i - e) == 0:
        root_count += 1
print(root_count)

# Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел от 0 до 1000 (включительно),
# которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.
