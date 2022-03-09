fin = open('input.txt', 'r', encoding='utf8')
countlist = [0] * 100
for line in fin:
    countlist[int(line.split()[2])] += 1
n_max = max(countlist)
print(countlist)
print(*[i for i in range(len(countlist)) if countlist[i] == n_max])
#
# В олимпиаде по информатике принимало участие N человек.
# Определите школы, из которых в олимпиаде принимало участие больше всего участников.
# В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех участниках,
# а только подсчитывая число участников для каждой школы.
#
# Формат ввода
#
# Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
#
# фамилия имя школа балл
#
# Фамилия и имя — текстовые строки, не содержащие пробелов.
# Школа — целое число от 1 до 99. Балл — целое число от 0 до 100.
#
# Формат вывода
#
# Выведите номера этих школ в порядке возрастания.
