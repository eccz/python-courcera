dist = list(map(int, input().split()))
tax = list(map(int, input().split()))
dist.sort()
tax.sort(reverse=True)
total = 0
for i, e in enumerate(dist):
    total += e * tax[i]
print(total)

# После затянувшегося совещания директор фирмы решил заказать такси, чтобы развезти сотрудников по домам.
# Он заказал N машин — ровно столько, сколько у него сотрудников. Однако когда они подъехали, оказалось,
# что у каждого водителя такси свой тариф за 1 километр.
#
# Директор знает, какому сотруднику сколько километров от работы до дома
# (к сожалению, все сотрудники живут в разных направлениях, поэтому нельзя отправить двух сотрудников на одной машине).
# Теперь директор хочет определить, сколько придется заплатить за перевозку всех сотрудников.
# Естественно, директор хочет заплатить как можно меньшую сумму.
#
# Формат ввода
#
# В первой строке записаны N чисел через пробел, задающих расстояния в километрах
# от работы до домов сотрудников компании.
# Во второй строке записаны N чисел — тарифы за проезд одного километра в такси.
#
# Формат вывода
#
# Выведите одно целое число — наименьшую сумму, которую придется заплатить за доставку всех сотрудников.
# Входные данные:
# 10 20 1 30 30
# 3 3 3 2 3
#
# Вывод программы:
# 243
