# Игра "Угадай число" на Python

import random

# Генерируем случайное число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0

print("Игра 'Угадай число'")
print("Я загадал число от 1 до 100. Попробуйте угадать его!")

while True:
    # Получаем предположение пользователя
    guess = int(input("Ваше предположение: "))
    attempts += 1
    
    # Проверяем предположение
    if guess < secret_number:
        print("Слишком маленькое число! Попробуйте ещё раз.")
    elif guess > secret_number:
        print("Слишком большое число! Попробуйте ещё раз.")
    else:
        print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
        break
