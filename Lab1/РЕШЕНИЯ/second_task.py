import math

# Открываем и читаем файл
with open('./75/second_task.txt', 'r', encoding='utf-8') as file:
    raws = file.readlines()

# Создаем таблицу с числами
table = []

for raw in raws:
    nums = raw.strip().split(' ')
    table.append(list(map(int, nums)))

# Считаем список сумм каждой строчки
row_sums = [
    int(round(sum(math.sqrt(num) for num in raw if num > 0), 0))
    for raw in table
]

# Находим минимальную и максимальную сумму
minmax_sum = [max(row_sums), min(row_sums)]

# Сохраняем файл
with open('./75/second_task_solve.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(map(str, row_sums)) + '\n')
    file.write('\n'.join(map(str, minmax_sum)))   