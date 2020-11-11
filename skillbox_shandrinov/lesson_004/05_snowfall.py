# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
sd.resolution = (1200, 800)
N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
snow_dict = {}
for i in range(N):
    snow_dict[i] = {'x': sd.random_number(0, sd.resolution[0]),
                    'y': sd.random_number(750, 800),
                    'length': sd.random_number(5, 40),
                    'color': sd.COLOR_WHITE,
                    'factor_a': random.uniform(0.1, 0.8),
                    'factor_b': random.uniform(0.1, 0.5),
                    'factor_c': sd.random_number(1, 60)
                    }
while True:
    sd.start_drawing()
    for i, snow_param in snow_dict.items():
        point1 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point1, length=snow_param['length'], color=sd.background_color,
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])
        snow_param['y'] -= 40
        snow_param['x'] += sd.random_number(2, 5)

        point2 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point2, length=snow_param['length'], color=snow_param['color'],
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])
        if snow_param['y'] < 70:
            snow_param['y'] = sd.random_number(750, 800)
            snow_param['length'] = sd.random_number(0, 40)
            snow_param['x'] = sd.random_number(0, sd.resolution[0])
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


