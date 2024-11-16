import pandas as pd

# Чтение фрагмента, поиск таблиц
chunk = pd.read_html('./75/fifth_task.html', attrs={'id': 'product-table'}, encoding='utf-8')

# Выбор первой таблицы
table = chunk[0]

# Сохранение в csv-файл
table.to_csv('./75/fifth_task_solve.csv', index=False, header=True)