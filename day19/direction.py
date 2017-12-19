from enum import Enum


class Direction(Enum):
    """ Enum to save the curent direction """
    up = 1
    down = 2
    left = 3
    right = 4


class Position:
    """ Class to save the current position """
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def __str__(self):
        return str(self.x) + '-' + str(self.y)


def printNetwork(network, pos):
    """ Print the network for debugging """
    for y, row in enumerate(network):
        for x, char in enumerate(row):
            if y == pos.y and x == pos.x:
                print('#', end='')
            else:
                print(char, end='')
        print('')
    print('')