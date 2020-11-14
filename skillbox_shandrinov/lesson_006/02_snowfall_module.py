# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
screen_width = 1200
screen_height = 600
sd.set_screen_size(screen_width, screen_height)

# создать_снежинки(N)
snow_count = 20
snow_dict = sf.snow_create(snow_count)

while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sf.snow_color(snow_color=sd.background_color, snow_dict=snow_dict)

    #  сдвинуть_снежинки()
    snow_step = 40
    sf.snow_shift(snow_step, snow_dict)

    #  нарисовать_снежинки_цветом(color)
    sf.snow_color(snow_color=sd.COLOR_YELLOW, snow_dict=snow_dict)

    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    number_to_del_list = sf.snow_list_number(snow_dict)
    if len(number_to_del_list) > 0:
        sf.snow_del_from_list(snow_dict=snow_dict, number_to_del_list=number_to_del_list)
        snow_dict = sf.snow_create(snow_count)

    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()
