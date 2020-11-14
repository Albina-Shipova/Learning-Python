# -*- coding: utf-8 -*-

import simple_draw as sd

screen_width = 1200
screen_height = 600
sd.set_screen_size(width=screen_width, height=screen_height)


def house(house_height=175, house_width=275,
          x_screen_shift=400, y_screen_shift=50,
          roof_color=sd.COLOR_RED, lines_color=sd.COLOR_ORANGE):
    house_start_point = sd.get_point(x_screen_shift, y_screen_shift)
    house_end_point = sd.get_point(x_screen_shift + house_width, y_screen_shift + house_height)

    # рисуем крышу дома
    roof_pointlist = [
        sd.get_point(x_screen_shift, y_screen_shift + house_height),
        sd.get_point(x_screen_shift + house_width / 2, y_screen_shift + house_height + house_height / 3),
        house_end_point,
    ]
    sd.polygon(point_list=roof_pointlist, color=roof_color, width=0)
    sd.polygon(point_list=roof_pointlist, color=roof_color, )

    # рисуем стены дома
    sd.rectangle(house_start_point, house_end_point, color=lines_color, width=1)
    # число кирпичей по горизонтали и вертикали:
    brick_quantity_x = 8
    brick_quantity_y = 8
    brick_length = house_width / brick_quantity_x
    brick_height = house_height / brick_quantity_y
    for shift_brick_y in range(0, int(house_height / brick_height)):
        y = shift_brick_y * brick_height
        for shift_brick_x in range(brick_quantity_x):
            if shift_brick_y % 2 == 0:
                x = shift_brick_x * brick_length
            else:
                if shift_brick_x == brick_quantity_x - 1:
                    break
                x = shift_brick_x * brick_length + brick_length / 2
            left_b = sd.get_point(x + x_screen_shift, y + y_screen_shift)
            right_t = sd.get_point(x + x_screen_shift + brick_length, y + y_screen_shift + brick_height)
            sd.rectangle(left_bottom=left_b, right_top=right_t, color=lines_color, width=1)


def window(house_height=175, house_width=275,
           x_screen_shift=400, y_screen_shift=50, color=sd.COLOR_DARK_PURPLE):
    window_left_bottom = sd.get_point(x_screen_shift + house_width / 3, y_screen_shift + house_height / 3)
    window_right_top = sd.get_point(x_screen_shift + house_width / 3 * 2, y_screen_shift + house_height / 3 * 2)
    sd.rectangle(window_left_bottom, window_right_top, color=color, width=0)
    sd.rectangle(window_left_bottom, window_right_top, color=color, width=1)


def smile(x=540, y=140, radius=20, color=sd.COLOR_YELLOW):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, color=color, radius=radius)
    # рисуем глаза смайла
    radius_eye = 3
    eye_left = sd.get_point(x - radius / 3, y + radius / 3)
    sd.circle(center_position=eye_left, color=color, radius=radius_eye)
    eye_right = sd.get_point(x + radius / 3, y + radius / 3)
    sd.circle(center_position=eye_right, color=color, radius=radius_eye)
    # рисуем улыбку из трех линий. вначале прямая, потом наклонные
    line_start = sd.get_point(x - radius / 4, y - radius / 3)
    line_end = sd.get_point(x + radius / 4, y - radius / 3)
    sd.line(start_point=line_start, end_point=line_end, color=color, width=1)
    line1_start = sd.get_point(x - radius / 1.5, y)
    line2_end = sd.get_point(x + radius / 1.5, y)
    sd.line(start_point=line1_start, end_point=line_start, color=color, width=1)
    sd.line(start_point=line_end, end_point=line2_end, color=color, width=1)


def ground(screen_width=1200, y_screen_shift=50, color=sd.COLOR_DARK_ORANGE):
    ground_left_bottom = sd.get_point(0, 0)
    ground_right_top = sd.get_point(screen_width, y_screen_shift)
    sd.rectangle(ground_left_bottom, ground_right_top, color)


if __name__ == '__main__':
    house()
    ground()
    window()
    smile()
    sd.pause()
