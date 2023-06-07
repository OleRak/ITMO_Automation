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
