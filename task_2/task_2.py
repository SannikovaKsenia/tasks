"""
Задание 2: JSON с 2 аудиториями
Реализация методов load, loads, dump, dumps для работы с JSON
"""

import json
import os

print("=" * 50)
print("ЗАДАНИЕ 2: JSON с аудиториями и компьютерами")
print("=" * 50)

# 1. СОЗДАНИЕ ДАННЫХ
print("\n1. Создание данных об аудиториях")

data = {
    "university": "Технический Университет",
    "classrooms": [
        {
            "id": 101,
            "name": "Аудитория 101",
            "capacity": 30,
            "computers": ["PC-101-01", "PC-101-02", "PC-101-03"]
        },
        {
            "id": 102,
            "name": "Аудитория 102", 
            "capacity": 20,
            "computers": ["PC-102-01", "PC-102-02"]
        }
    ]
}

print(f"   Создано аудиторий: {len(data['classrooms'])}")

# 2. ФУНКЦИЯ dump() - сохранение в файл
def dump(data_dict, filename):
    print(f"\n2. Сохранение в файл '{filename}'")
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)
        print(f"   Файл создан успешно")
        return True
    except Exception as e:
        print(f"   Ошибка: {e}")
        return False

dump(data, "classrooms.json")

# 3. ФУНКЦИЯ load() - загрузка из файла
def load(filename):
    print(f"\n3. Загрузка из файла '{filename}'")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
        print(f"   Файл загружен успешно")
        return loaded_data
    except FileNotFoundError:
        print(f"   Ошибка: файл не найден")
        return None
    except json.JSONDecodeError:
        print(f"   Ошибка: некорректный JSON формат")
        return None

loaded_data = load("classrooms.json")

# 4. ФУНКЦИЯ dumps() - преобразование в строку
def dumps(data_dict):
    print("\n4. Преобразование данных в JSON строку")
    
    json_string = json.dumps(data_dict, ensure_ascii=False, indent=2)
    
    print(f"   Длина строки: {len(json_string)} символов")
    
    return json_string

json_string = dumps(data)

# 5. ФУНКЦИЯ loads() - из строки в данные
def loads(json_str):
    print("\n5. Преобразование JSON строки обратно в данные")
    
    try:
        data_from_string = json.loads(json_str)
        print(f"   Преобразование выполнено успешно")
        return data_from_string
    except json.JSONDecodeError as e:
        print(f"   Ошибка преобразования: {e}")
        return None

data_from_string = loads(json_string)

# 6. ПРОВЕРКА РЕЗУЛЬТАТОВ
print("\n" + "=" * 50)
print("ПРОВЕРКА РЕЗУЛЬТАТОВ")
print("=" * 50)

if loaded_data is not None:
    if data == loaded_data:
        print("Тест 1: Данные из файла совпадают с исходными")
    else:
        print("Тест 1: Данные из файла не совпадают с исходными")

if data_from_string is not None:
    if data == data_from_string:
        print("Тест 2: Данные из строки совпадают с исходными")
    else:
        print("Тест 2: Данные из строки не совпадают с исходными")

# 7. ИНФОРМАЦИЯ О ФАЙЛАХ
print("\n" + "=" * 50)
print("СОЗДАННЫЕ ФАЙЛЫ")
print("=" * 50)

if os.path.exists("classrooms.json"):
    file_size = os.path.getsize("classrooms.json")
    print(f"1. classrooms.json - {file_size} байт")

print(f"2. task2.py - {os.path.getsize(__file__)} байт")

print("\n" + "=" * 50)
print("=" * 50)