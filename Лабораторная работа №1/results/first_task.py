from collections import Counter

# Открываем и читаем файл
with open('./75/first_task.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Общее задание
# Удаляем лишние символы из текста
text = (
    text.replace(',', '')
        .replace('!', '')
        .replace('.', '')
        .replace('?', '')
        .replace('\n', ' ')
        .lower()
)

# Получаем массив слов
words = text.split()

# Создаем словарь для подсчета частоты слов
word_dict = {}

# Используем Counter для подсчёта частот
word_dict = Counter(words)

# Сортируем полученный словарь по убыванию значения ключа
word_dict = sorted(word_dict.items(), key = lambda x: x[1], reverse=True)

# Сохраняем полученный словарь в отдельный txt файл
with open('./75/first_task_solve_1.txt', 'w', encoding='utf-8') as file:
    for key, value in word_dict:
        file.write(f'{key}: {value}\n')

# Вариант №5
# Записываем в переменную гласные буквы
chars = 'aeiouy'

# Подсчет всех гласных букв
chars_count = sum(1 for letters in text if letters in chars)

# Подсчет всех букв в тексте
letters_count = sum(1 for letters in text if letters.isalpha())

# Подсчет доли гласных букв
chars_ratio = chars_count / letters_count * 100

with open('./75/first_task_solve_2.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество гласных: {chars_count}\nДоля гласных: {chars_ratio}")