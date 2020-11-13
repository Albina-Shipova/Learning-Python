# -*- coding: utf-8 -*-

import simple_draw as sd
import random


def snow(snow_dict, stop_snow_x=sd.resolution[0], stop_snow_y=70, delta=0):
    # snow_dict = {}
    # for i in range(n):
    #     snow_dict[i] = {'x': sd.random_number(0, stop_snow_x),
    #                     'y': sd.random_number(750, 800),
    #                     'length': sd.random_number(5, 10),
    #                     'color': sd.COLOR_WHITE,
    #                     'factor_a': random.uniform(0.1, 0.8),
    #                     'factor_b': random.uniform(0.1, 0.4),
    #                     'factor_c': sd.random_number(1, 60)
    #                     }

    for _, snow_param in snow_dict.items():
        point1 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point1, length=snow_param['length'], color=sd.background_color,
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])
        snow_param['y'] -= 20
        snow_param['x'] += sd.random_number(-3, 3)

        point2 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point2, length=snow_param['length'], color=snow_param['color'],
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])
        if snow_param['y'] < stop_snow_y + delta:
            snow_param['x'] = sd.random_number(0, stop_snow_x)
            snow_param['y'] = sd.random_number(750, 800)
            snow_param['length'] = sd.random_number(5, 10)
            delta += 5


if __name__ == '__main__':
    snow_number = 20
    snow_dict = {}
    for i in range(snow_number):
        snow_dict[i] = {'x': sd.random_number(0, sd.resolution[0]),
                        'y': sd.random_number(750, 800),
                        'length': sd.random_number(5, 10),
                        'color': sd.COLOR_WHITE,
                        'factor_a': random.uniform(0.1, 0.8),
                        'factor_b': random.uniform(0.1, 0.4),
                        'factor_c': sd.random_number(1, 60)
                        }
    while True:
        snow(snow_dict=snow_dict)
        if sd.user_want_exit():
            break
    sd.pause()