#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для автоматического создания git коммитов
с указанными датами и случайными сообщениями
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
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Коммит создан: {datetime_str} - {message}")
    else:
        print(f"✗ Ошибка при создании коммита: {result.stderr}")
    return result.returncode == 0

def main():
    """Основная функция для создания коммитов"""
    # Начальная дата: 16 сентября 2025
    start_date = datetime(2025, 9, 16)
    # Конечная дата: 31 октября 2025
    end_date = datetime(2025, 10, 31)
    
    current_date = start_date
    success_count = 0
    error_count = 0
    
    print("Начинаю создание коммитов...")
    print(f"Период: {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}\n")
    
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        time_str = generate_random_time()
        message = generate_random_message()
        
        if create_commit(date_str, time_str, message):
            success_count += 1
        else:
            error_count += 1
        
        # Переходим к следующему дню
        current_date += timedelta(days=1)
    
    print(f"\n{'='*50}")
    print(f"Готово!")
    print(f"Успешно создано коммитов: {success_count}")
    print(f"Ошибок: {error_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

