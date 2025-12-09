"""
Задание 3: Конвертация JSON -> CSV
"""

import json
import csv
import os

print("=" * 50)
print("ЗАДАНИЕ 3: Конвертация JSON -> CSV")
print("=" * 50)

# 1. Загрузка JSON
print("\n1. Загрузка данных из classrooms.json")

with open("classrooms.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"   Загружено аудиторий: {len(data['classrooms'])}")

# 2. Создание CSV
print("\n2. Создание CSV файла")

with open("classrooms.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Заголовки
    writer.writerow(["ID", "Аудитория", "Вместимость", "Кол-во компьютеров", "Компьютеры"])
    
    # Данные
    for classroom in data['classrooms']:
        computers = classroom['computers']
        writer.writerow([
            classroom['id'],
            classroom['name'],
            classroom['capacity'],
            len(computers),
            "; ".join(computers)  # Все компьютеры в одной ячейке
        ])

print("   Файл classrooms.csv создан")

# 3. Создание YAML-подобного файла (без библиотеки)
print("\n3. Создание YAML-like файла (ручная генерация)")

with open("classrooms.yml", 'w', encoding='utf-8') as f:
    f.write("# Данные об аудиториях\n")
    f.write("university: \"Технический Университет\"\n")
    f.write("classrooms:\n")
    
    for classroom in data['classrooms']:
        f.write(f"  - id: {classroom['id']}\n")
        f.write(f"    name: \"{classroom['name']}\"\n")
        f.write(f"    capacity: {classroom['capacity']}\n")
        f.write(f"    computers:\n")
        
        for computer in classroom['computers']:
            f.write(f"      - \"{computer}\"\n")

print("   Файл classrooms.yml создан")

# 4. Результаты
print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ")
print("=" * 50)

files = ["classrooms.csv", "classrooms.yml"]
for file in files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"{file}: {size} байт")

print("\n" + "=" * 50)
print("=" * 50)
