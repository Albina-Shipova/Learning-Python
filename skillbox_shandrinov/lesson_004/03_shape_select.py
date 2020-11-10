# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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

point = sd.get_point(100, 100)

colors_dict = {
    '1': ['red', sd.COLOR_RED], '2': ['orange', sd.COLOR_ORANGE],
    '3': ['yellow', sd.COLOR_YELLOW], '4': ['green', sd.COLOR_GREEN],
    '5': ['cyan', sd.COLOR_CYAN], '6': ['blue', sd.COLOR_BLUE],
    '7': ['purple', sd.COLOR_PURPLE]
}

figure_dict = {
    '0': ['треугольник', triangle], '1': ['квадрат', square],
    '2': ['пятиугольник', pentagon], '3': ['шестиугольник', hexagon],
}
print('Возможные фигуры: ')
for key, value in figure_dict.items():
    print(key, ':', figure_dict[key][0])
while True:
    fig = input('Введите желаемую фигуру: ')
    if fig.isdigit():
        if int(fig) in range(4):
            fig = figure_dict[fig][1]
            break
        else:
            print('Неправильный ввод')
    else:
        print('Неправильный ввод')

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


fig(point=point, color=figure_color)


sd.pause()
