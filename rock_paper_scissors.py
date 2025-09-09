# Игра "Камень, ножницы, бумага" на Python

import random

def get_user_choice():
    """Получает выбор пользователя"""
    while True:
        choice = input("Ваш выбор (камень, ножницы, бумага): ").lower()
        if choice in ["камень", "ножницы", "бумага"]:
            return choice
        print("Неверный ввод! Пожалуйста, выберите: камень, ножницы или бумага.")

def get_computer_choice():
    """Генерирует выбор компьютера"""
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Определяет победителя"""
    if user_choice == computer_choice:
        return "ничья"
    
    # Камень побеждает ножницы
    if user_choice == "камень" and computer_choice == "ножницы":
        return "пользователь"
    
    # Ножницы побеждают бумагу
    if user_choice == "ножницы" and computer_choice == "бумага":
        return "пользователь"
    
    # Бумага побеждает камень
    if user_choice == "бумага" and computer_choice == "камень":
        return "пользователь"
    
    # В остальных случаях побеждает компьютер
    return "компьютер"

def main():
    print("Игра 'Камень, ножницы, бумага'")
    print("Правила: камень побеждает ножницы, ножницы побеждают бумагу, бумага побеждает камень.")
    
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nСчёт: Вы {user_score} - {computer_score} Компьютер")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "ничья":
            print("Ничья!")
        elif winner == "пользователь":
            print("Вы победили!")
            user_score += 1
        else:
            print("Компьютер победил!")
            computer_score += 1
        
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != "да":
            break
    
    print(f"\nИтоговый счёт: Вы {user_score} - {computer_score} Компьютер")
    print("Спасибо за игру!")

if __name__ == "__main__":
    main()
