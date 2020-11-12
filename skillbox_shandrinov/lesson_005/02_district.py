# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as csh1r1, room2 as csh1r2
from district.central_street.house2 import room1 as csh2r1, room2 as csh2r2
from district.soviet_street.house1 import room1 as ssh1r1, room2 as ssh1r2
from district.soviet_street.house2 import room1 as ssh2r1, room2 as ssh2r2
citizen = []
for i in [csh1r1, csh1r2, csh2r1, csh2r2, ssh1r1, ssh1r2, ssh2r1, ssh2r2]:
    citizen.extend(i.folks)
print('На районе живут', ', '.join(citizen))




