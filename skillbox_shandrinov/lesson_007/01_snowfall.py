# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(20, sd.resolution[0]-20)
        self.y = sd.random_number(sd.resolution[1] - 50, sd.resolution[1] - 40)
        self.length = 20
        self.color = sd.COLOR_WHITE
        self.factor_a = 0.5
        self.factor_b = 0.3
        self.factor_c = 60

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color,
                     factor_a=self.factor_a, factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def move(self, step_x=sd.random_number(-5, 5), step_y=20):
        self.x += step_x
        self.y -= step_y

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=self.color,
                     factor_a=self.factor_a, factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def can_fall(self):
        if self.y > 10:
            return True
        else:
            return False


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
def get_flakes(count=1):
    flakes = []
    for i in range(n):
        flake = Snowflake()
        flakes.append(flake)
    return flakes


def get_fallen_flakes(flakes):
    count = 0
    for i, obj in enumerate(flakes):
        if not obj.can_fall():
            count += 1
            del flakes[i]
    return count


def append_flakes(list_flakes, count):
    for i in range(count):
        flake = Snowflake()
        list_flakes.append(flake)
    return list_flakes


n = 10
flakes = get_flakes(count=n)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move(step_y=40)
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flakes = append_flakes(flakes, count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
