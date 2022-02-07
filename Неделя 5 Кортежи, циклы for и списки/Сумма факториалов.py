from math import factorial

n = int(input())
sumfactorial = 0
for i in range(1, n + 1):
    sumfactorial += factorial(i)
print(sumfactorial)

# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
