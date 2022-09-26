# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

number_quasters = int(input('введите номер четверти: '))


while number_quasters < 0 or number_quasters > 4:
    print('Такого не может быть. Попробуйте еще раз')
    number_quasters = int(input('введите номер четверти: '))


if number_quasters == 1:
    print('x > 0 and y > 0')
elif number_quasters == 2:
    print('x < 0 and y > 0')
elif number_quasters == 3:
    print('x < 0 and y < 0')
elif number_quasters == 4:
    print('x > 0 and y < 0')
