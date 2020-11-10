# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def figure(point, angle, angle_end, step, color, length=100):
    for ang in range(angle, angle_end, step):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=5)
        v1.draw(color=color)
        point = v1.end_point


def triangle(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure(point=point, angle=angle, angle_end=angle + 241, step=120, color=color, length=length)


def square(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure(point=point, angle=angle, angle_end=angle + 360, step=90, color=color, length=length)


def pentagon(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure(point=point, angle=angle, angle_end=angle + 360, step=72, color=color, length=length)


def hexagon(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure(point=point, angle=angle, angle_end=angle + 360, step=60, color=color, length=length)


colors_dict = {
    '1': ['red', sd.COLOR_RED], '2': ['orange', sd.COLOR_ORANGE],
    '3': ['yellow', sd.COLOR_YELLOW], '4': ['green', sd.COLOR_GREEN],
    '5': ['cyan', sd.COLOR_CYAN], '6': ['blue', sd.COLOR_BLUE],
    '7': ['purple', sd.COLOR_PURPLE]
}
print('Возможные цвета: ')
for key, value in colors_dict.items():
    print(key, ':', colors_dict[key][0])

while True:
    col = input('Введите желаемый цвет(номер): ')
    if col.isdigit():
        if int(col) in range(1, 8):
            figure_color = colors_dict[col][1]
            break
        else:
            print('Неправильный ввод')
    else:
        print('Неправильный ввод')

point_triangle = sd.get_point(50, 50)
triangle(point=point_triangle, color=figure_color)

point_square = sd.get_point(400, 50)
square(point=point_square, color=figure_color)

point_pentagon = sd.get_point(50, 400)
pentagon(point=point_pentagon, color=figure_color)

point_hexagon = sd.get_point(400, 400)
hexagon(point=point_hexagon, color=figure_color)


sd.pause()
