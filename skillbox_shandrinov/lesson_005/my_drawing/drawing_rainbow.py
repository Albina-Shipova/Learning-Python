import simple_draw as sd


# rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
#                   sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def rainbow(x=250, y=0, radius=350, width=15, rainbow_colors=[sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                   sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]):
    radius_rainbow = radius
    for color in rainbow_colors:
        center = sd.get_point(x, y)
        sd.circle(center_position=center, radius=radius_rainbow, color=color, width=width)
        radius_rainbow += width
    radius_rainbow = radius


def sun(x=1500, y=1500, radius=60, color=sd.COLOR_YELLOW, sun_line=8):
    center = sd.get_point(x, y)
    sd.circle(center_position=center, radius=radius, color=color, width=0)
    sd.circle(center_position=center, radius=radius, color=color, width=1)
    angle = 0
    for i in range(sun_line):
        sd.get_vector(start_point=center, angle=angle, length=radius * 2, width=2).draw()
        angle += 360 / sun_line


if __name__ == '__main__':
    rainbow()
    sd.pause()
