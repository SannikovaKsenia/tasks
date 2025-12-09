"""
Парсер задач с сайта acmp.ru
Сохраняет данные в JSON формате
"""

import requests
from bs4 import BeautifulSoup
import json
import time

def parse_acmp_tasks():
    """Парсит задачи с главной страницы acmp.ru"""
    
    url = "https://acmp.ru/index.asp?main=tasks"
    tasks_data = []
    
    try:
        print("Получаем данные с acmp.ru...")
        
        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Отправляем запрос
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'windows-1251'  # Кодировка acmp.ru
        
        if response.status_code != 200:
            print(f"Ошибка HTTP: {response.status_code}")
            return []
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем таблицы с задачами (основной контент)
        main_table = None
        for table in soup.find_all('table'):
            if table.get('class') and 'main' in str(table.get('class')):
                main_table = table
                break
        
        if main_table:
            # Ищем все строки в таблице
            rows = main_table.find_all('tr')
            for row in rows:
                # Ищем ссылки на задачи
                task_link = row.find('a', href=True)
                if task_link and 'index.asp?main=task' in task_link['href']:
                    
                    # Извлекаем ID задачи из URL
                    href = task_link['href']
                    task_id = ''
                    if 'id=' in href:
                        task_id = href.split('id=')[1].split('&')[0]
                    
                    # Извлекаем текст задачи
                    task_text = task_link.get_text(strip=True)
                    
                    if task_id and task_text:
                        tasks_data.append({
                            'id': task_id,
                            'title': task_text,
                            'url': f"https://acmp.ru/{href}",
                            'parsed_date': time.strftime("%Y-%m-%d"),
                            'difficulty': 'unknown'  
                        })
        
        # Если не нашли через таблицу, ищем просто по ссылкам
        if not tasks_data:
            print("Попытка альтернативного поиска...")
            for link in soup.find_all('a', href=True):
                href = link['href']
                if 'index.asp?main=task' in href and 'id=' in href:
                    task_id = href.split('id=')[1].split('&')[0]
                    task_text = link.get_text(strip=True)
                    
                    if task_text and task_id:
                        tasks_data.append({
                            'id': task_id,
                            'title': task_text,
                            'url': f"https://acmp.ru/{href}",
                            'parsed_date': time.strftime("%Y-%m-%d")
                        })
        
        # Ограничиваем 20 задачами для демонстрации
        tasks_data = tasks_data[:20]
        
        # Сохраняем в JSON
        with open('acmp_tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=2)
        
        print(f"Парсинг завершен. Найдено задач: {len(tasks_data)}")
        print("Данные сохранены в acmp_tasks.json")
        
        return tasks_data
        
    except requests.exceptions.Timeout:
        print("Ошибка: таймаут запроса")
        return []
    except Exception as e:
        print(f"Ошибка при парсинге: {type(e).__name__}: {e}")
        return []

def create_sample_data():
    """Создает пример данных если парсинг не работает"""
    sample_tasks = [
        {
            "id": "1",
            "title": "A+B",
            "url": "https://acmp.ru/index.asp?main=task&id_task=1",
            "parsed_date": time.strftime("%Y-%m-%d"),
            "difficulty": "easy"
        },
        {
            "id": "2",
            "title": "Сумма",
            "url": "https://acmp.ru/index.asp?main=task&id_task=2",
            "parsed_date": time.strftime("%Y-%m-%d"),
            "difficulty": "easy"
        },
        {
            "id": "3",
            "title": "Максимум",
            "url": "https://acmp.ru/index.asp?main=task&id_task=3",
            "parsed_date": time.strftime("%Y-%m-%d"),
            "difficulty": "easy"
        }
    ]
    
    with open('acmp_tasks.json', 'w', encoding='utf-8') as f:
        json.dump(sample_tasks, f, ensure_ascii=False, indent=2)
    
    print("Создан пример данных (acmp_tasks.json)")
    return sample_tasks

# Основной блок
if __name__ == "__main__":
    print("=" * 50)
    print("Парсер задач acmp.ru")
    print("=" * 50)
    
    # Пытаемся спарсить реальные данные
    tasks = parse_acmp_tasks()
    
    # Если не получилось, создаем пример
    if not tasks:
        print("\nИспользуем пример данных...")
        tasks = create_sample_data()
    
    # Выводим результат
    if tasks:
        print("\nПервые 5 найденных задач:")
        for i, task in enumerate(tasks[:5], 1):
            print(f"{i}. [{task['id']}] {task['title']}")
