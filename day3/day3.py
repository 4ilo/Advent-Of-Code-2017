import math


def highest_root(data):
    """ Calculate the highest sqrt for the given number """
    stop = False
    while not stop:
        root = math.sqrt(data)
        if root.is_integer() and (root % 2 != 0):
            return int(root)

        data = data - 1


def next_corner(spiral, number):
    """ Calculate the distance to the next corner of the squire """
    higest = math.pow(spiral, 2)
    diference = spiral - 1
    corners = [higest, higest - diference, higest - 2*diference, higest - 3*diference, 0]

    for i in range(len(corners)):
        if corners[i] >= number > corners[i+1]:
            return int(corners[i])


def calculate_steps(puzzle_input):
    """ Calculate the amount of steps for part1 """
    spiral = highest_root(puzzle_input) + 2

    l1 = math.floor(spiral / 2)
    l_to_corner = next_corner(spiral, puzzle_input) - puzzle_input

    l2 = abs(l1 - l_to_corner)

    return l1 + l2


puzzle_input = 265149
print('part1: %d' % calculate_steps(puzzle_input))
