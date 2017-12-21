import numpy as np


def serialize(array):
    """ Convert numpy array to string """
    tmp = array.tolist()
    return '/'.join([''.join(x) for x in tmp])


def deserialize(string):
    """ Convert string to numpy array """
    grid = [list(x) for x in string.split('/')]
    return np.array(grid)


def parse_rules(input):
    """ Parse the input rules """
    rules = {}

    for line in input:
        parts = line.split(" => ")
        grid = deserialize(parts[0])

        for r in range(4):
            rotated = np.rot90(grid, r)
            rules.update({
                serialize(rotated): parts[1],
                serialize(np.fliplr(rotated)): parts[1],
                serialize(np.flipud(rotated)): parts[1]
            })

    return rules


def enhance(grid, rules):
    """ Perfom one enhancement cycle """
    size = len(grid[0])

    if size % 2 == 0:
        """ Dividable by 2 """
        block = int(size / 2)
        new_grid = np.empty((3*block, 3*block), dtype=str)
        for y in range(block):
            for x in range(block):
                part = serialize(grid[2*y: 2*y +2, 2*x: 2*x +2].copy())
                new_grid[3*y: 3*y +3, 3*x: 3*x +3] = deserialize(rules[part])

    elif size % 3 == 0:
        """ Dividable by 3 """
        block = int(size / 3)
        new_grid = np.empty((4*block, 4*block), dtype=str)
        for y in range(block):
            for x in range(block):
                part = serialize(grid[3*y: 3*y +3, 3*x: 3*x +3].copy())
                new_grid[4*y: 4*y +4, 4*x: 4*x +4] = deserialize(rules[part])

    return new_grid


def count_pixels(array):
    """ Count the active pixels in the grid """
    return serialize(array).count('#')


def run(i, rules):
    """ Run the enhancement i times """
    grid = deserialize(".#./..#/###")

    for x in range(i):
        grid = enhance(grid, rules)

    return grid


if __name__ == '__main__':
    input = open("input.txt").read().splitlines()

    rules = parse_rules(input)

    print("Count pixels after 5: %d" % count_pixels(run(5, rules)))
    print("Count pixels after 18: %d" % count_pixels(run(18, rules)))
