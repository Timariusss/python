# bool - True и False

usl1 = 10 > 5  # число 1 больше числа 2?
print(usl1)
usl2 = 10 < 3  # число 1 меньше числа 2?
print(usl2)
usl3 = 10 <= 6  # число 1 меньше или равно второму числу?
print(usl3)
usl4 = 6 >= 5  # число 1 больше или равно второму числу?
print(usl4)
usl5 = 10 == 10 # равна ли левая сторона правой?
print(usl5)
usl6 = 8 != 9  # НЕ равна ли левая сторона правой?
print(usl6)


# and - И (*) or - ИЛИ (+)

tst1 = int(input('Введите любое число: ')) # 11 


grm1 = tst1 > 10 and tst1 % 2 == 0 # True and True = 1 * 1 = 1 = True 
grm2 = tst1 < 10 and tst1 % 2 == 0 # True and False -> 1 * 0 = 0 = False  
grm3 = tst1 % 3 == 0 or tst1 > 100 # True or False = 1 + 0 = 1 -> True 

print(grm1)
print(grm2) 
print(grm3)


if tst1 > 10 and tst1 % 2 == 0:
     print('Число больше десяти и четное')
elif tst1 % 2 != 0: 
    print('Число нечетное.')
elif tst1 == 8:
    print ('Вы ввели число 8')
else:
    print ('Пока!')

print ('КОНЕЦ!')

