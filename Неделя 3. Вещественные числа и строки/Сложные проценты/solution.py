import math

p, rub, kop, year = int(input()), int(input()), int(input()), int(input())
i = 1
all_kop = rub * 100 + kop
while i <= year:
    plus = all_kop * p / 100
    all_kop = math.trunc(all_kop + plus)
    i += 1
vivod_rub = all_kop // 100
vivod_kop = all_kop % 100
print("{0:.0f}".format(vivod_rub), end=' ')
print('{0:.0f}'.format(vivod_kop))
