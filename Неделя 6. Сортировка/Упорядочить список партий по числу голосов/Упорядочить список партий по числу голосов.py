fin = open('input.txt', 'r', encoding='utf8')
parties = []
votes = []
count = []
for line in fin:
    if line == 'PARTIES:\n':
        continue
    if line == 'VOTES:\n':
        break
    parties.append(line.strip())

for line in fin:
    votes.append(line.strip())

for i, e in enumerate(parties):
    count.append((e, votes.count(e)))

count.sort(key=lambda x: (-x[1], x[0]))
[print(i[0]) for i in count]
# Формат входных данных аналогичен предыдущей задаче (Семипроцентный барьер).
# Выведите список всех партий, участвовавших в выборах,
# отсортировав его в порядке убывания количества голосов избирателей,
# а при равном количестве голосов - в лексикографическом порядке.
