import simple_draw as sd


def draw_branches(start_point, angle=90, length=100):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    color = sd.COLOR_DARK_ORANGE
    if length < 20:
        color = sd.COLOR_GREEN
    v1.draw(color=color)
    start_point = v1.end_point
    length = length * 0.75
    draw_branches(start_point, angle=angle + 30, length=length)
    draw_branches(start_point, angle=angle - 30, length=length)

if __name__ == '__main__':
    root_point = sd.get_point(300, 30)
    draw_branches(start_point=root_point, angle=90, length=100)
    sd.pause()

