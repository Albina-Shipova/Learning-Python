# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.element = 'Water'

    def __add__(self, other):
        if other.element == 'Fire':
            return Steam()
        elif other.element == 'Earth':
            return Dirt()
        elif other.element == 'Air':
            return Storm()
        elif other.element == 'Water':
            return Water()
        else:
            return None

    def __str__(self):
        return 'Вода'


class Fire:
    def __init__(self):
        self.element = 'Fire'

    def __add__(self, other):
        if other.element == 'Water':
            return Steam()
        elif other.element == 'Earth':
            return Lava()
        elif other.element == 'Air':
            return Lightning()
        elif other.element == 'Fire':
            return Fire()
        else:
            return None

    def __str__(self):
        return 'Огонь'


class Earth:
    def __init__(self):
        self.element = 'Earth'

    def __add__(self, other):
        if other.element == 'Water':
            return Steam()
        elif other.element == 'Fire':
            return Lava()
        elif other.element == 'Air':
            return Dust()
        elif other.element == 'Earth':
            return Earth()
        else:
            return None

    def __str__(self):
        return 'Земля'


class Air:
    def __init__(self):
        self.element = 'Air'

    def __add__(self, other):
        if other.element == 'Water':
            return Storm()
        elif other.element == 'Fire':
            return Lightning()
        elif other.element == 'Earth':
            return Dust()
        elif other.element == 'Air':
            return Air()
        else:
            return None

    def __str__(self):
        return 'Воздух'


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt():
    def __str__(self):
        return 'Грязь'


class Lightning():
    def __str__(self):
        return 'Молния'


class Dust():
    def __str__(self):
        return 'Пыль'


class Lava():
    def __str__(self):
        return 'Лава'


print(Water(), '+', Water(), '=', Water() + Water())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Earth(), '+', Fire(), '=', Earth() + Fire())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
