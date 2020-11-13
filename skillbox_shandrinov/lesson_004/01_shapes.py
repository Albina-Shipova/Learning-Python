# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(point, angle=0, length=100, width=2):
    for ang in range(angle, 241, 120):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=width)
        v1.draw()
        point = v1.end_point


def square(point, angle=0, length=100):
    for ang in range(angle, 360, 90):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=2)
        v1.draw()
        point = v1.end_point


def pentagon(point, angle=0, length=100):
    for ang in range(angle, 360, 72):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=5)
        v1.draw()
        point = v1.end_point


def hexagon(point, angle=0, length=100):
    for ang in range(angle, 360, 60):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=5)
        v1.draw()
        point = v1.end_point


point_triangle = sd.get_point(50, 50)
triangle(point=point_triangle)

point_square = sd.get_point(400, 50)
square(point=point_square)

point_pentagon = sd.get_point(50, 400)
pentagon(point=point_pentagon)

point_hexagon = sd.get_point(400, 400)
hexagon(point=point_hexagon)

sd.pause()
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def figure(point, angle, angle_end, step, length=100):
    for ang in range(angle, angle_end, step):
        v1 = sd.get_vector(start_point=point, angle=ang, length=length, width=5)
        v1.draw()
        point = v1.end_point


def triangle(point, angle=0, length=100):
    figure(point=point, angle=angle, angle_end=angle + 241, step=120, length=length)


def square(point, angle=0, length=100):
    figure(point=point, angle=angle, angle_end=angle + 360, step=90, length=length)


def pentagon(point, angle=0, length=100):
    figure(point=point, angle=angle, angle_end=angle + 360, step=72, length=length)


def hexagon(point, angle=0, length=100):
    figure(point=point, angle=angle, angle_end=angle + 360, step=60, length=length)


point_triangle = sd.get_point(50, 50)
triangle(point=point_triangle)

point_square = sd.get_point(400, 50)
square(point=point_square)

point_pentagon = sd.get_point(50, 400)
pentagon(point=point_pentagon)

point_hexagon = sd.get_point(400, 400)
hexagon(point=point_hexagon)

sd.pause()
