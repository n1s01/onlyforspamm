# Простой менеджер задач (To-Do List) на Python

tasks = []

def show_menu():
    print("\nМЕНЮ:")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу")
    print("4. Выход")

def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена!")

def show_tasks():
    if not tasks:
        print("Список задач пуст!")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Введите номер задачи для удаления: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Задача '{removed_task}' удалена!")
            else:
                print("Неверный номер задачи!")
        except ValueError:
            print("Пожалуйста, введите число!")

# Основной цикл программы
while True:
    show_menu()
    choice = input("Выберите пункт меню: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")
