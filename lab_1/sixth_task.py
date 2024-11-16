import requests
import pandas as pd

# Запрос данных
response = requests.get('https://randomuser.me/api/')
data = response.json()

# Преобразование в датафрейм
df = pd.json_normalize(data)  # Преобразуем JSON в табличный вид

# Генерация html
html_content = df.to_html(index=False, border=1, justify="center", classes="table")

# Сохранение файла
with open('lab_1/results/sixth_task_solve.html', "w", encoding="utf-8") as file:
    file.write(html_content)
