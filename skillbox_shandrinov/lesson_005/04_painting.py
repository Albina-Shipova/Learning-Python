# -*- coding: utf-8 -*-
import simple_draw as sd
import random
from my_drawing import drawing_house, drawing_tree, drawing_rainbow, drawing_snowfall
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# параметры экрана
screen_width = 1200
screen_height = 600
# sd.set_screen_size(width=screen_width, height=screen_height)

# параметры дома с крышей и расположение дома на экране
house_height = 175
house_weight = 275
lines_color = sd.COLOR_ORANGE
ground_color = sd.COLOR_DARK_ORANGE
x_screen_shift = 300
y_screen_shift = 50
roof_color = sd.COLOR_RED

# рисуем дом, окно и землю
drawing_house.house(house_height, house_weight, x_screen_shift, y_screen_shift, roof_color, lines_color)
drawing_house.ground(screen_width=screen_width, y_screen_shift=y_screen_shift, color=ground_color)
drawing_house.window(house_height, house_weight, x_screen_shift, y_screen_shift)
drawing_house.smile(x=x_screen_shift+house_weight/2, y=y_screen_shift+house_height/2)

# рисуем дерево
shift_from_house = 300
root_point = sd.get_point(house_weight + x_screen_shift + shift_from_house, y_screen_shift)
drawing_tree.draw_branches(start_point=root_point, angle=90, length=90)

# рисуем радугу и солнце

drawing_rainbow.sun(x=400, y=450, radius=50)
rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
snow_number = 20
snow_dict = {}
for i in range(snow_number):
    snow_dict[i] = {'x': sd.random_number(0, x_screen_shift),
                    'y': sd.random_number(750, 800),
                    'length': sd.random_number(5, 10),
                    'color': sd.COLOR_WHITE,
                    'factor_a': random.uniform(0.1, 0.8),
                    'factor_b': random.uniform(0.1, 0.4),
                    'factor_c': sd.random_number(1, 60)
                    }
while True:
    drawing_rainbow.rainbow(x=350, y=-150, radius=900, width=10, rainbow_colors=rainbow_colors)
    rainbow_colors.insert(0, rainbow_colors[-1])
    rainbow_colors.pop()

    drawing_snowfall.snow(snow_dict=snow_dict, stop_snow_x=x_screen_shift-40, stop_snow_y=y_screen_shift+10)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break
sd.pause()




# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
