#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для автоматического создания git коммитов
с указанными датами и случайными сообщениями
Создает случайное количество коммитов в день и периодически делает push
"""

import subprocess
import random
import string
from datetime import datetime, timedelta

def generate_random_message(length=10):
    """Генерирует случайное сообщение из букв"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_time():
    """Генерирует случайное время в формате HH:MM:SS"""
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}:{second:02d}"

def create_commit(date_str, time_str, message):
    """Создает git коммит с указанной датой и временем"""
    datetime_str = f"{date_str} {time_str}"
    command = [
        'git', 'commit', '--allow-empty',
        '-m', message,
        '--date', datetime_str
    ]
    
    print(f"Выполняю: git commit --allow-empty -m \"{message}\" --date=\"{datetime_str}\"")
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    
    if result.returncode == 0:
        print(f"✓ Коммит создан: {datetime_str} - {message}")
    else:
        print(f"✗ Ошибка при создании коммита: {result.stderr}")
    return result.returncode == 0

def do_push():
    """Выполняет git push"""
    print("\n" + "="*50)
    print("Выполняю git push...")
    command = ['git', 'push']
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    
    if result.returncode == 0:
        print("✓ Push выполнен успешно")
        print("="*50 + "\n")
    else:
        print(f"✗ Ошибка при push: {result.stderr}")
        print("="*50 + "\n")
    return result.returncode == 0

def main():
    """Основная функция для создания коммитов"""
    # Начальная дата: 31 августа 2025
    start_date = datetime(2025, 8, 31)
    # Конечная дата: 31 октября 2025
    end_date = datetime(2025, 10, 31)
    
    current_date = start_date
    success_count = 0
    error_count = 0
    push_count = 0
    
    # Счетчик коммитов до следующего push
    commits_until_push = random.randint(3, 10)
    commits_since_push = 0
    
    print("Начинаю создание коммитов...")
    print(f"Период: {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}")
    print(f"Коммитов до первого push: {commits_until_push}\n")
    
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        
        # Генерируем случайное количество коммитов для этого дня (0-5)
        commits_today = random.randint(0, 5)
        
        if commits_today > 0:
            print(f"\n[{date_str}] Создаю {commits_today} коммит(ов)")
            
            for _ in range(commits_today):
                time_str = generate_random_time()
                message = generate_random_message()
                
                if create_commit(date_str, time_str, message):
                    success_count += 1
                    commits_since_push += 1
                    
                    # Проверяем, нужно ли делать push
                    if commits_since_push >= commits_until_push:
                        if do_push():
                            push_count += 1
                        # Генерируем новое случайное количество коммитов до следующего push
                        commits_until_push = random.randint(3, 10)
                        commits_since_push = 0
                        print(f"Следующий push через {commits_until_push} коммитов")
                else:
                    error_count += 1
        else:
            print(f"[{date_str}] Нет коммитов")
        
        # Переходим к следующему дню
        current_date += timedelta(days=1)
    
    # Если остались неотправленные коммиты, делаем финальный push
    if commits_since_push > 0:
        print(f"\nОсталось {commits_since_push} коммитов, выполняю финальный push...")
        if do_push():
            push_count += 1
    
    print(f"\n{'='*50}")
    print("Готово!")
    print(f"Успешно создано коммитов: {success_count}")
    print(f"Выполнено push: {push_count}")
    print(f"Ошибок: {error_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

