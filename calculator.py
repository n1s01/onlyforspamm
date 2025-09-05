# Простой калькулятор на Python

print("Простой калькулятор")
print("Доступные операции: +, -, *, /")

# Получаем первое число
num1 = float(input("Введите первое число: "))

# Получаем операцию
op = input("Введите операцию (+, -, *, /): ")

# Получаем второе число
num2 = float(input("Введите второе число: "))

# Выполняем операцию
if op == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Ошибка: неизвестная операция!")
