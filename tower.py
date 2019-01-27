#!/usr/bin/python

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

d_room = int(input('Elevator: Enter the room number:'))

tower = []  # Create tower
i = 0  # Rooms counter
x = 0  # Stages counter
f = 0  # Floors counter
d = 0  # Doors from left counter

while i < d_room:

    # Counting stages
    x += 1

    # Creating block
    block = []
    for _ in range(x):

        # Creating floor
        f += 1
        floor = []
        for d in range(x):

            # Counting rooms
            i += 1
            floor.append(i)
            if i == d_room:
                print('location of room:', d_room, '\nfloor:', f, '\ndoor from left:', d + 1)

        block.append(floor)

    tower.append(block)

# Draw the tower in a fun way
print('\nThe upended tower will looks like:')
print(str(tower).replace('],', ']\n').replace(']', '').replace('[', '\r').replace(',', ''))
