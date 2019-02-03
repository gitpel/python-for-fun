#!/usr/bin/python

#    ______     __     ______     __  __     ______
#   /\  ___\   /\ \   /\  ___\   /\ \_\ \   /\__  _\
#   \ \  __\   \ \ \  \ \ \__ \  \ \  __ \  \/_/\ \/
#    \ \_____\  \ \_\  \ \_____\  \ \_\ \_\    \ \_\
#     \/_____/   \/_/   \/_____/   \/_/\/_/     \/_/
#
#    ______     __  __     ______     ______     __   __     ______
#   /\  __ \   /\ \/\ \   /\  ___\   /\  ___\   /\ "-.\ \   /\  ___\
#   \ \ \/\_\  \ \ \_\ \  \ \  __\   \ \  __\   \ \ \-.  \  \ \___  \
#    \ \___\_\  \ \_____\  \ \_____\  \ \_____\  \ \_\\"\_\  \/\_____\
#     \/___/_/   \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_____/
#

# Puzzle "Eight Queens" in one line solution
# https://en.wikipedia.org/wiki/Eight_queens_puzzle
#
# My solution\idea based on straight board and rotated on 45
# and -45 degrees and infinity of queens direction - Konstantin Gimpel
# https://github.com/gitpel/

desk_size = 8
queen_location = []
# Uncomment the right puzzle quiz
# queen_location = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 3], [6, 1], [7, 7], [8, 5]]


# ------------------ start of unnecessary code ------------


def place_queen(x, y):
    if 1 <= x <= desk_size and 1 <= y <= desk_size:
        if not [x, y] in queen_location:
            queen_location.append([x, y])
            print('Queens placed:', len(queen_location), 'from:', desk_size, '\nQueens coordinates:', queen_location)


while len(queen_location) != desk_size:
    place_queen(*[int(x) for x in (input('\nPlace the queen at location X and Y\nUse space between X and Y\nlike 1 5:\n').split())])


# ------------------ end of unnecessary code --------------


# One line solution is:
print('No') if sum([len(x) for x in (list(map(set, zip(*[(x, y, y + x, y - x) for x, y in queen_location]))))]) != desk_size * 4 else print('Yes')

