# Анализатор текста на Python

def analyze_text(text):
    """Анализирует текст и возвращает статистику"""
    # Базовая статистика
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Подсчёт гласных и согласных
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    # Подсчёт цифр
    digit_count = sum(1 for char in text if char.isdigit())
    
    # Подсчёт знаков препинания
    punctuation_count = sum(1 for char in text if char in ".,!?;:-\"'()[]{}")
    
    # Самые частые слова
    words = text.lower().split()
    # Удаляем знаки препинания из слов
    cleaned_words = [word.strip(".,!?;:-\"'()[]{}") for word in words if word.strip(".,!?;:-\"'(){}")]
    
    word_frequency = {}
    for word in cleaned_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    # Сортируем слова по частоте
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:5]  # Топ-5 самых частых слов
    
    return {
        "char_count": char_count,
        "char_count_no_spaces": char_count_no_spaces,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
        "digit_count": digit_count,
        "punctuation_count": punctuation_count,
        "top_words": top_words
    }

def display_results(stats):
    """Отображает результаты анализа"""
    print("\n=== РЕЗУЛЬТАТЫ АНАЛИЗА ТЕКСТА ===")
    print(f"Количество символов (с пробелами): {stats['char_count']}")
    print(f"Количество символов (без пробелов): {stats['char_count_no_spaces']}")
    print(f"Количество слов: {stats['word_count']}")
    print(f"Количество предложений: {stats['sentence_count']}")
    print(f"Количество гласных: {stats['vowel_count']}")
    print(f"Количество согласных: {stats['consonant_count']}")
    print(f"Количество цифр: {stats['digit_count']}")
    print(f"Количество знаков препинания: {stats['punctuation_count']}")
    
    if stats['top_words']:
        print("\nСамые частые слова:")
        for i, (word, count) in enumerate(stats['top_words'], 1):
            print(f"{i}. '{word}' - {count} раз(а)")
    else:
        print("\nВ тексте нет слов для анализа.")

def get_text_from_file():
    """Получает текст из файла"""
    file_path = input("Введите путь к файлу: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def main():
    """Основная функция программы"""
    print("Анализатор текста")
    print("Эта программа анализирует текст и предоставляет статистику о нём.")
    
    while True:
        print("\nВыберите источник текста:")
        print("1. Ввести текст вручную")
        print("2. Прочитать текст из файла")
        print("3. Выход")
        
        choice = input("Ваш выбор (1-3): ")
        
        if choice == '1':
            print("\nВведите текст для анализа (для завершения введите пустую строку):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            
            text = "\n".join(lines)
            if not text:
                print("Вы не ввели текст!")
                continue
                
            stats = analyze_text(text)
            display_results(stats)
            
        elif choice == '2':
            text = get_text_from_file()
            if text:
                stats = analyze_text(text)
                display_results(stats)
                
        elif choice == '3':
            print("До свидания!")
            break
            
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 3.")
        
        if choice in ['1', '2'] and text:
            another = input("\nХотите проанализировать ещё один текст? (да/нет): ").lower()
            if another != 'да':
                print("До свидания!")
                break

if __name__ == "__main__":
    main()
