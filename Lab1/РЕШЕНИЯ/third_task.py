# Открываем и читаем файл
with open('./75/third_task.txt', 'r', encoding='utf-8') as file:
    rows = file.readlines()

# Создаем список для суммы строк
row_sums = []

for row in rows:

    # Проходимся по строкам и разбиваем числа на int/None
    nums = [
        int(num) if num != 'N/A' else None for num in row.strip().split(' ')]

    # Заменяем None на среднее значение соседей
    nums = [
        (nums[i - 1] + nums[i + 1]) / 2 if nums[i] is None else nums[i]
        for i in range(len(nums))
    ]
    
    # Оставляем числа, кратные трем
    multiple_nums = [num for num in nums if num % 3 == 0]

    #Считаем суммы в каждой строке
    row_sums.append(int(round(sum(multiple_nums), 0)))

# Записываем результат в файл
with open('./75/third_task_solve.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(map(str, row_sums)))