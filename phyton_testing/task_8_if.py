# Программа проверяет является ли число положительным
# или отрицательным и выводит соответствующее сообщение

num = 3

if num >= 0:
    print("число больше или равно 0")
else:
    print("число отрицательное")

str_1 = "test"
str_2 = "test1"

if str_1 in str_2:
    print("да")
else:
    print("нет")

num_float = 0

if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print("ноль")
else:
    print("число отрицательное")

permit_print = True

if num > 0 and permit_print:
    print('num - положительнгое число')
elif not permit_print:
    print("Печать запрещена")

num = 10
if num >= 1 and num <=4:
    print("бакалавр")
elif num >= 5 and num <=6:
    print("магистр")
elif num >= 7 and num <=8:
    print("аспирант")
else:
    print("Введите корректный год обучения")

num = 101
if num > 100 or num < -100:
    print("-")
else:
    print("+")

