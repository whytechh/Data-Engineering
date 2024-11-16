import pandas as pd

# Чтение файла
data = pd.read_csv('./75/fourth_task.txt')

# Удаление колонки
data_dropped = data.drop('status', axis=1)

# Среднее арифметическое
mean_value = data['quantity'].mean()

# Максимум
max_value = data['price'].max()

# Минимум
min_value = data['rating'].min()

# Фильтрация
data_filtered = data[data['status'] == 'Refunded']

# Сохранение модифицированного csv-файла
data_filtered.to_csv('./75/fourth_task_solve.csv', index=False, header=True)

# Сохранение результатов вычислений
with open("./75/fourth_task_solve.txt", "w") as file:
            file.write(f"Среднее арифметическое по столбцу quantity: {mean_value}\n \
Максимальное значение по столбцу price: {max_value}\n \
Минимальное значение по стобцу rating: {min_value}")