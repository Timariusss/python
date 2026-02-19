import colorama
import inspect
from colorama import Fore, Back, Style


colorama.init()


print("1. Информация о модуле colorama")


print("Тип объекта colorama:", type(colorama))
print("\nСписок атрибутов модуля (dir):")
print(dir(colorama))



print("2. Интроспекция классов Fore, Back, Style")


print("\nТип Fore:", type(Fore))
print("Тип Back:", type(Back))
print("Тип Style:", type(Style))


print("\nАтрибуты Fore:")
for name in dir(Fore):
    if not name.startswith("_"):
        print(name)

print("\nАтрибуты Back:")
for name in dir(Back):
    if not name.startswith("_"):
        print(name)

print("\nАтрибуты Style:")
for name in dir(Style):
    if not name.startswith("_"):
        print(name)



print("3. Использование основных атрибутов")


print(Fore.RED + "Красный текст")
print(Fore.GREEN + "Зеленый текст")
print(Back.YELLOW + "Текст на желтом фоне")
print(Style.BRIGHT + "Яркий текст")
print(Style.RESET_ALL)



print("4 Интроспекция через inspect")


print("\nЧлены класса Fore:")
for name, value in inspect.getmembers(Fore):
    if not name.startswith("_"):
        print(f"{name} -> {value}")

print("\nДокументация Fore:")
print(Fore.__doc__)



print("Программа завершена")
