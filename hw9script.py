import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Загрузка данных
try:
    with open('events.json', 'r', encoding='utf-8') as f:
        data_dict = json.load(f)

    # Создаем DataFrame (Pandas делает это "из коробки" для списка словарей)
    df = pd.DataFrame(data_dict['events'])

    print("--- Первые 5 строк датафрейма ---")
    print(df.head())

except FileNotFoundError:
    print("Ошибка: Файл events.json не найден. Убедитесь, что он лежит в папке с проектом.")
    exit()

# 2. Анализ данных
# В Pandas самый простой способ посчитать количество уникальных значений — value_counts()
print("\n--- Распределение событий по типам (signature) ---")
# Получаем серию пожсчетов
signature_counts = df['signature'].value_counts()
print(signature_counts)

# 3. Визуализация
plt.figure(figsize=(12, 8))

sns.countplot(
    data=df,
    y="signature",
    hue="signature",
    order=df['signature'].value_counts().index,
    palette="viridis",
    legend=False
)

plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Количество событий")
plt.ylabel("Тип сигнатуры")

# Добавляем сетку
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()