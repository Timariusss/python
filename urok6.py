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
# 3
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Текст ошибки: {e}")

