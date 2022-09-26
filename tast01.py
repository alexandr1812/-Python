# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


while True:
    number_day = int(input('Введите день недели: '))
    if number_day == 6 or number_day == 7:
        print('Выходной день')
    elif number_day > 0 and number_day < 6:
        print('Рабочий день')
        break
    elif number_day < 0 or number_day > 7:
        print('Такого дня недели не cуществует')