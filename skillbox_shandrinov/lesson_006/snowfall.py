# создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
import simple_draw as sd
import random


def snow_create(snow_count):
    snow_dict = {}
    for i in range(snow_count):
        snow_dict[i] = {'x': sd.random_number(0, sd.resolution[0]),
                        'y': sd.random_number(sd.resolution[1] - 50, sd.resolution[1]-40),
                        'length': sd.random_number(5, 40),
                        # 'color': sd.COLOR_WHITE,
                        'factor_a': random.uniform(0.1, 0.8),
                        'factor_b': random.uniform(0.1, 0.5),
                        'factor_c': sd.random_number(1, 60)
                        }
    return snow_dict


def snow_color(snow_color, snow_dict):
    for i, snow_param in snow_dict.items():
        snow_dict[i]['color'] = snow_color
        point2 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point2, length=snow_param['length'], color=snow_color,
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])


def snow_shift(snow_step, snow_dict):
    for _, snow_param in snow_dict.items():
        point1 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point1, length=snow_param['length'], color=sd.background_color,
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])
        snow_param['y'] -= snow_step
        snow_param['x'] += sd.random_number(-5, 5)

        point2 = sd.get_point(snow_param['x'], snow_param['y'])
        sd.snowflake(center=point2, length=snow_param['length'], color=snow_param['color'],
                     factor_a=snow_param['factor_a'], factor_b=snow_param['factor_b'],
                     factor_c=snow_param['factor_c'])


def snow_list_number(snow_dict):
    snow_list = []
    for i, snow_param in snow_dict.items():
        if snow_param['y'] < -40:
            snow_list.append(i)
    return snow_list


def snow_del_from_list(snow_dict, number_to_del_list):
    for i in number_to_del_list:
        del snow_dict[i]
    return snow_dict

if __name__ == '__main__':
    screen_weight = 1200
    screen_height = 600
    sd.set_screen_size(screen_weight, screen_height)
    sd.start_drawing()
    snow_create(10)
    sd.finish_drawing()
    sd.pause()
