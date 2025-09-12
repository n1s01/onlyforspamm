# Простой проверщик погоды на Python

import random
import datetime

def get_weather_data(city):
    """Имитирует получение данных о погоде для города"""
    # В реальном приложении здесь был бы API-запрос к сервису погоды
    weather_conditions = ["Солнечно", "Облачно", "Дождь", "Снег", "Туман", "Ветрено"]
    temperatures = {
        "Москва": random.randint(-10, 25),
        "Санкт-Петербург": random.randint(-5, 20),
        "Новосибирск": random.randint(-15, 20),
        "Екатеринбург": random.randint(-15, 22),
        "Казань": random.randint(-10, 23),
        "Нижний Новгород": random.randint(-8, 22),
        "Челябинск": random.randint(-12, 20),
        "Самара": random.randint(-8, 25),
        "Ростов-на-Дону": random.randint(-2, 30),
        "Уфа": random.randint(-10, 23),
        "Красноярск": random.randint(-15, 20),
        "Воронеж": random.randint(-8, 24),
        "Пермь": random.randint(-12, 20),
        "Волгоград": random.randint(-6, 26)
    }
    
    # Если город не в списке, генерируем случайную температуру
    temperature = temperatures.get(city, random.randint(-15, 30))
    condition = random.choice(weather_conditions)
    humidity = random.randint(30, 90)
    wind_speed = random.randint(0, 20)
    
    return {
        "city": city,
        "temperature": temperature,
        "condition": condition,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    }

def display_weather(weather_data):
    """Отображает информацию о погоде"""
    print(f"\nПогода в городе {weather_data['city']} на {weather_data['date']}:")
    print(f"Температура: {weather_data['temperature']}°C")
    print(f"Состояние: {weather_data['condition']}")
    print(f"Влажность: {weather_data['humidity']}%")
    print(f"Скорость ветра: {weather_data['wind_speed']} м/с")
    
    # Дополнительные рекомендации
    temp = weather_data['temperature']
    if temp < -10:
        print("\nРекомендация: Одевайтесь очень тепло!")
    elif temp < 0:
        print("\nРекомендация: Одевайтесь тепло, не забудьте шапку и перчатки.")
    elif temp < 10:
        print("\nРекомендация: Одевайтесь по погоде, лучше в несколько слоев.")
    elif temp < 20:
        print("\nРекомендация: Лёгкая куртка или свитер будет в самый раз.")
    else:
        print("\nРекомендация: Отличная погода для прогулки! Одевайтесь легко.")
    
    condition = weather_data['condition']
    if condition == "Дождь":
        print("Не забудьте зонт!")
    elif condition == "Снег":
        print("Будьте осторожны на дорогах!")
    elif condition == "Туман":
        print("Водителям стоит быть особенно внимательными!")
    elif condition == "Ветрено":
        print("Крепче держите шляпу!")

def main():
    """Основная функция программы"""
    print("Простой проверщик погоды")
    print("Доступные города: Москва, Санкт-Петербург, Новосибирск, Екатеринбург, Казань,")
    print("Нижний Новгород, Челябинск, Самара, Ростов-на-Дону, Уфа, Красноярск, Воронеж, Пермь, Волгоград")
    
    while True:
        city = input("\nВведите название города (или 'выход' для завершения): ").strip()
        
        if city.lower() == 'выход':
            print("До свидания!")
            break
        
        if not city:
            print("Пожалуйста, введите название города.")
            continue
        
        weather_data = get_weather_data(city)
        display_weather(weather_data)
        
        another = input("\nХотите узнать погоду в другом городе? (да/нет): ").lower()
        if another != 'да':
            print("До свидания!")
            break

if __name__ == "__main__":
    main()
