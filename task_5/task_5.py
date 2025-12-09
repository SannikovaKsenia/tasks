"""
Конвертация данных из JSON в CSV формат
"""

import json
import csv
import os

def convert_json_to_csv(json_file, csv_file):
    """
    Конвертирует JSON файл в CSV
    
    Args:
        json_file: путь к JSON файлу
        csv_file: путь для сохранения CSV файла
    """
    
    try:
        # Проверяем существование JSON файла
        if not os.path.exists(json_file):
            print(f"Файл {json_file} не найден")
            return False
        
        # Читаем JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Проверяем тип данных
        if not isinstance(data, list):
            print("Ошибка: JSON должен содержать список объектов")
            return False
        
        if len(data) == 0:
            print("Ошибка: список данных пуст")
            return False
        
        # Определяем все возможные ключи (заголовки столбцов)
        all_keys = set()
        for item in data:
            if isinstance(item, dict):
                all_keys.update(item.keys())
        
        # Сортируем ключи для единообразия
        fieldnames = sorted(all_keys)
        
        # Записываем в CSV
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            # Записываем заголовок
            writer.writeheader()
            
            # Записываем данные
            for item in data:
                # Создаем строку со всеми ключами
                row = {key: item.get(key, '') for key in fieldnames}
                writer.writerow(row)
        
        # Статистика
        file_size = os.path.getsize(csv_file)
        print(f"Конвертация завершена успешно")
        print(f"Файл: {csv_file}")
        print(f"Размер: {file_size} байт")
        print(f"Строк: {len(data)}")
        print(f"Столбцов: {len(fieldnames)}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return False
    except Exception as e:
        print(f"Ошибка при конвертации: {type(e).__name__}: {e}")
        return False

def preview_csv(csv_file, lines=5):
    """Выводит первые строки CSV файла"""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            print(f"\nПервые {lines} строк файла {csv_file}:")
            print("-" * 50)
            
            for i, line in enumerate(f):
                if i >= lines:
                    break
                print(line.strip())
            
            print("-" * 50)
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")

# Основной блок
if __name__ == "__main__":
    print("=" * 50)
    print("Конвертер JSON в CSV")
    print("=" * 50)
    
    # Конвертируем файл из задания 4
    json_file = "acmp_tasks.json"
    csv_file = "acmp_tasks.csv"
    
    # Если JSON файла нет, создаем пример
    if not os.path.exists(json_file):
        print(f"Файл {json_file} не найден")
        print("Создаю пример данных...")
        
        example_data = [
            {"id": "1", "title": "A+B", "difficulty": "easy", "solved": "10000"},
            {"id": "2", "title": "Сумма", "difficulty": "easy", "solved": "8500"},
            {"id": "3", "title": "Максимум", "difficulty": "easy", "solved": "9200"}
        ]
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(example_data, f, ensure_ascii=False, indent=2)
        print(f"Создан пример файла: {json_file}")
    
    # Выполняем конвертацию
    if convert_json_to_csv(json_file, csv_file):
        # Показываем результат
        preview_csv(csv_file)
        
        print("\nКонвертация acmp_tasks.json -> acmp_tasks.csv выполнена")
    else:
        print("\nОшибка при конвертации")
