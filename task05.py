# 5) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Введите координаты первой точки: ')
x1 = float(input('x: '))
y1 = float(input('y: '))
print("Введите координаты второй точки:")
x2 = float(input('x: '))
y2 = float(input('y: '))

from math import sqrt
print('Расстояние между точками: ',round(sqrt((x1 - x2)**2 + (y1 - y2)**2), 2))