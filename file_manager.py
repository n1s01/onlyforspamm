# Простой файловый менеджер на Python

import os
import shutil

def show_menu():
    """Показывает меню файлового менеджера"""
    print("\nФайловый менеджер")
    print("1. Показать файлы в текущей директории")
    print("2. Создать папку")
    print("3. Создать текстовый файл")
    print("4. Удалить файл")
    print("5. Удалить папку")
    print("6. Копировать файл")
    print("7. Переместить файл")
    print("8. Показать текущую директорию")
    print("9. Сменить директорию")
    print("10. Выход")

def list_files():
    """Показывает файлы и папки в текущей директории"""
    print(f"\nФайлы в директории: {os.getcwd()}")
    items = os.listdir()
    
    if not items:
        print("Директория пуста!")
        return
    
    print("\nПапки:")
    for item in items:
        if os.path.isdir(item):
            print(f"  [ПАПКА] {item}")
    
    print("\nФайлы:")
    for item in items:
        if os.path.isfile(item):
            size = os.path.getsize(item)
            print(f"  [ФАЙЛ] {item} ({size} байт)")

def create_folder():
    """Создаёт новую папку"""
    folder_name = input("Введите имя новой папки: ")
    try:
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' успешно создана!")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует!")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}")

def create_file():
    """Создаёт новый текстовый файл"""
    file_name = input("Введите имя файла (с расширением .txt): ")
    content = input("Введите содержимое файла: ")
    
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Файл '{file_name}' успешно создан!")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

def delete_file():
    """Удаляет файл"""
    file_name = input("Введите имя файла для удаления: ")
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' успешно удалён!")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден!")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

def delete_folder():
    """Удаляет папку"""
    folder_name = input("Введите имя папки для удаления: ")
    try:
        os.rmdir(folder_name)
        print(f"Папка '{folder_name}' успешно удалена!")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не найдена!")
    except OSError:
        print(f"Папка '{folder_name}' не пуста! Удалите сначала файлы внутри.")
    except Exception as e:
        print(f"Ошибка при удалении папки: {e}")

def copy_file():
    """Копирует файл"""
    source = input("Введите имя исходного файла: ")
    destination = input("Введите имя файла назначения: ")
    
    try:
        shutil.copy(source, destination)
        print(f"Файл '{source}' успешно скопирован в '{destination}'!")
    except FileNotFoundError:
        print(f"Файл '{source}' не найден!")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

def move_file():
    """Перемещает файл"""
    source = input("Введите имя исходного файла: ")
    destination = input("Введите новое имя файла или путь: ")
    
    try:
        shutil.move(source, destination)
        print(f"Файл '{source}' успешно перемещён в '{destination}'!")
    except FileNotFoundError:
        print(f"Файл '{source}' не найден!")
    except Exception as e:
        print(f"Ошибка при перемещении файла: {e}")

def show_current_directory():
    """Показывает текущую директорию"""
    print(f"Текущая директория: {os.getcwd()}")

def change_directory():
    """Меняет текущую директорию"""
    path = input("Введите путь к новой директории: ")
    try:
        os.chdir(path)
        print(f"Текущая директория изменена на: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Директория '{path}' не найдена!")
    except Exception as e:
        print(f"Ошибка при смене директории: {e}")

def main():
    """Основная функция файлового менеджера"""
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            list_files()
        elif choice == '2':
            create_folder()
        elif choice == '3':
            create_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            delete_folder()
        elif choice == '6':
            copy_file()
        elif choice == '7':
            move_file()
        elif choice == '8':
            show_current_directory()
        elif choice == '9':
            change_directory()
        elif choice == '10':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 10.")

if __name__ == "__main__":
    main()
