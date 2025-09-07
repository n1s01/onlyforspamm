# Генератор паролей на Python

import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль указанной длины"""
    # Определяем наборы символов
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Объединяем все символы
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Генерируем пароль
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Генератор паролей")
    
    try:
        length = int(input("Введите длину пароля (рекомендуется 12+): "))
        if length < 4:
            print("Слишком короткая длина! Минимум 4 символа.")
            return
    except ValueError:
        print("Пожалуйста, введите число!")
        return
    
    password = generate_password(length)
    print(f"Ваш сгенерированный пароль: {password}")
    
    # Оценка надёжности
    strength = "Слабый"
    if length >= 8:
        strength = "Средний"
    if length >= 12:
        strength = "Надёжный"
    if length >= 16:
        strength = "Очень надёжный"
    
    print(f"Уровень надёжности: {strength}")

if __name__ == "__main__":
    main()
