# Игра "Крестики-нолики" на Python

import random

def display_board(board):
    """Отображает игровое поле"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Проверяет, выиграл ли игрок"""
    # Проверка строк
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    # Проверка столбцов
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    # Проверка диагоналей
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

def is_board_full(board):
    """Проверяет, заполнено ли поле"""
    return " " not in board

def get_player_move(board):
    """Получает ход игрока"""
    while True:
        try:
            move = int(input("Ваш ход (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Неверный ход! Выберите пустую клетку от 1 до 9.")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 9.")

def get_computer_move(board, computer_player, human_player):
    """Получает ход компьютера с простой стратегией"""
    # Проверяем, может ли компьютер выиграть следующим ходом
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = computer_player
            if check_winner(board_copy, computer_player):
                return i
    
    # Проверяем, нужно ли блокировать ход игрока
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = human_player
            if check_winner(board_copy, human_player):
                return i
    
    # Если центр свободен, занимаем его
    if board[4] == " ":
        return 4
    
    # Занимаем углы
    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == " "]
    if available_corners:
        return random.choice(available_corners)
    
    # Занимаем оставшиеся клетки
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

def play_game():
    """Основная функция игры"""
    board = [" "] * 9
    current_player = "X"  # Игрок всегда X
    computer_player = "O"
    
    print("Игра 'Крестики-нолики'")
    print("Вы играете за крестики (X), компьютер - за нолики (O)")
    print("Клетки нумеруются так:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    
    while True:
        display_board(board)
        
        if current_player == "X":  # Ход игрока
            move = get_player_move(board)
            board[move] = "X"
            
            if check_winner(board, "X"):
                display_board(board)
                print("Поздравляю! Вы победили!")
                break
                
            if is_board_full(board):
                display_board(board)
                print("Ничья!")
                break
                
            current_player = "O"
        else:  # Ход компьютера
            print("Ход компьютера...")
            move = get_computer_move(board, "O", "X")
            board[move] = "O"
            print(f"Компьютер выбрал клетку {move + 1}")
            
            if check_winner(board, "O"):
                display_board(board)
                print("Компьютер победил!")
                break
                
            if is_board_full(board):
                display_board(board)
                print("Ничья!")
                break
                
            current_player = "X"

def main():
    """Главная функция программы"""
    while True:
        play_game()
        
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()
