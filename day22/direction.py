from enum import IntEnum
from termcolor import colored


class Direction(IntEnum):
    """ Enum to save the curent direction """
    up = 1
    right = 2
    down = 3
    left = 4


class Position:
    """ Class to save the current position and direction """
    def __init__(self, xpos, ypos, dir):
        self.x = xpos
        self.y = ypos
        self.dir = dir

    def turn_right(self):
        """ Turn right """
        if (self.dir + 1) <= 4:
            self.dir += 1
        else:
            self.dir = 1

    def turn_left(self):
        """ Turn left """
        if (self.dir - 1) >= 1:
            self.dir -= 1
        else:
            self.dir = 4

    def reverse(self):
        """ Reverse the direction """
        if self.dir == Direction.up:
            self.dir = Direction.down

        elif self.dir == Direction.down:
            self.dir = Direction.up

        elif self.dir == Direction.left:
            self.dir = Direction.right

        elif self.dir == Direction.right:
            self.dir = Direction.left

    def move(self):
        """ Move 1 step in the given direction """
        if self.dir == Direction.down:
            self.y += 1
        if self.dir == Direction.up:
            self.y -= 1
        if self.dir == Direction.left:
            self.x -= 1
        if self.dir == Direction.right:
            self.x += 1

    def __str__(self):
        return str(self.x) + '-' + str(self.y)


def print_cluster(cluster, pos):
    """ Print the network for debugging """
    for y, row in enumerate(cluster):
        for x, char in enumerate(row):
            if y == pos.y and x == pos.x:
                print(colored(char, 'red'), end='')
            else:
                print(char, end='')
        print('')
    print('')
