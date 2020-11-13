# Создать модуль my_burger. В нем определить функции добавления инградиентов:

# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

food = ['булочка', 'котлета', 'огурчик', 'помидор', 'майонез', 'сыр']


def bread(lst):
    lst.append('булочка')
    print('Добавим булочку')


def meat(lst):
    lst.append('котлета')
    print('A теперь добавим котлету')


def mayonnaise(lst):
    lst.append('майонез')
    print('A теперь добавим майонез')


def cucumber(lst):
    lst.append('огурчик')
    print('A теперь добавим огурчик')


def tomato(lst):
    lst.append('помидор')
    print('A теперь добавим помидор')


def cheese(lst):
    lst.append('сыр')
    print('A теперь добавим сыр')