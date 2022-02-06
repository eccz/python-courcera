import math

p, rub, kop = int(input()), int(input()), int(input())
all_kop = rub * 100 + kop
plus = all_kop * p / 100
itog_kop = math.trunc(all_kop + plus)
vivod_rub = itog_kop // 100
vivod_kop = itog_kop % 100
print("{0:.0f}".format(vivod_rub), end=' ')
print('{0:.0f}'.format(vivod_kop))
