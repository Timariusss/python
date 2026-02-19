result = []

def divider(a, b):
    if a < b:
        raise ValueError("a меньше чем b")
    if b > 100:
        raise IndexError("b больше 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 15: 8, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)

    except ZeroDivisionError as e:
        print("Вы получили ошибку деления на ноль:", e)

    except ValueError as e:
        print("ValueError:", e)

    except IndexError as e:
        print("IndexError:", e)

    except TypeError as e:
        print("TypeError:", "Нельзя использовать строку в качестве делителя")

    except Exception as e:
        print("Другая ошибка:", e)

print("\nРезультат работы:")
print(result)
