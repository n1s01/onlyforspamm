# Конвертер валют на Python

def get_exchange_rates():
    """Возвращает словарь с курсами валют относительно рубля"""
    # В реальном приложении здесь был бы API-запрос к сервису курсов валют
    return {
        "RUB": 1.0,        # Рубль
        "USD": 0.011,      # Доллар США
        "EUR": 0.010,      # Евро
        "GBP": 0.009,      # Британский фунт
        "CNY": 0.078,      # Китайский юань
        "JPY": 1.59,       # Японская иена
        "KZT": 5.02,       # Казахстанский тенге
        "BYN": 0.036,      # Белорусский рубль
        "UAH": 0.40,       # Украинская гривна
        "GEL": 0.029       # Грузинский лари
    }

def display_currencies():
    """Отображает список доступных валют"""
    print("\nДоступные валюты:")
    currencies = get_exchange_rates()
    for code in currencies:
        if code == "RUB":
            print(f"{code} - Российский рубль (базовая валюта)")
        elif code == "USD":
            print(f"{code} - Доллар США")
        elif code == "EUR":
            print(f"{code} - Евро")
        elif code == "GBP":
            print(f"{code} - Британский фунт")
        elif code == "CNY":
            print(f"{code} - Китайский юань")
        elif code == "JPY":
            print(f"{code} - Японская иена")
        elif code == "KZT":
            print(f"{code} - Казахстанский тенге")
        elif code == "BYN":
            print(f"{code} - Белорусский рубль")
        elif code == "UAH":
            print(f"{code} - Украинская гривна")
        elif code == "GEL":
            print(f"{code} - Грузинский лари")

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """Конвертирует сумму из одной валюты в другую"""
    # Сначала конвертируем в рубли, если это не рубль
    if from_currency != "RUB":
        amount_in_rub = amount / exchange_rates[from_currency]
    else:
        amount_in_rub = amount
    
    # Затем конвертируем из рублей в целевую валюту
    if to_currency != "RUB":
        converted_amount = amount_in_rub * exchange_rates[to_currency]
    else:
        converted_amount = amount_in_rub
    
    return converted_amount

def main():
    """Основная функция программы"""
    print("Конвертер валют")
    exchange_rates = get_exchange_rates()
    
    while True:
        display_currencies()
        
        # Получаем исходную валюту
        from_currency = input("\nВведите код исходной валюты (например, USD): ").upper()
        if from_currency not in exchange_rates:
            print("Ошибка: неизвестная валюта!")
            continue
        
        # Получаем целевую валюту
        to_currency = input("Введите код целевой валюты (например, EUR): ").upper()
        if to_currency not in exchange_rates:
            print("Ошибка: неизвестная валюта!")
            continue
        
        # Получаем сумму для конвертации
        try:
            amount = float(input(f"Введите сумму в {from_currency}: "))
            if amount <= 0:
                print("Ошибка: сумма должна быть положительным числом!")
                continue
        except ValueError:
            print("Ошибка: введите корректное число!")
            continue
        
        # Выполняем конвертацию
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        
        # Отображаем результат
        print(f"\nРезультат конвертации:")
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        
        # Дополнительная информация
        if from_currency != "RUB" and to_currency != "RUB":
            # Показываем курс через рубль
            amount_in_rub = amount / exchange_rates[from_currency]
            print(f"Курс: 1 {from_currency} = {exchange_rates[from_currency]:.4f} RUB")
            print(f"Курс: 1 {to_currency} = {exchange_rates[to_currency]:.4f} RUB")
        
        # Спрашиваем, хочет ли пользователь выполнить ещё одну конвертацию
        another = input("\nХотите выполнить ещё одну конвертацию? (да/нет): ").lower()
        if another != 'да':
            print("До свидания!")
            break

if __name__ == "__main__":
    main()
