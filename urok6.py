'''
# 1 
try: 
    x = int(input("Введите число: "))
    result = 10 / x
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно.")
except ValueError:
    print("Ошибка: введите корректное число.")
else:
    print(result)
finally:
    print("Программа завершена.")
'''
'''
# 2 
try: 
    x = int("abc")
except (ValueError, TypeError):
    print("Ошибка типа или значения.")
'''
'''
# 3
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Текст ошибки: {e}")
'''
'''
# 4  
def func(balance, amount):
    if amount > balance:
        raise ValueError("Недостаточно средств на счете.")
    return balance - amount 

try: 
    func(int(input("Введите баланс: ")), int(input("Введите сумму для снятия: ")))
except ValueError as e:
    print(e)
finally:
    print("Программа завершена.")
'''
'''
# 5 
data = ["10", "20", "abc", "30"]
for item in data:
    try:
        print(10 / int(item))
    except Exception as e:
        print(f"Ошибка: {e}")
'''
'''
# 6
try:
    with open("urok6dop.txt") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Ошибка: файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally: 
    print("Программа завершена.")
'''