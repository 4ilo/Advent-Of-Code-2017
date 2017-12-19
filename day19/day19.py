from direction import *


def move(direction, pos):
    """ Move 1 step in the given direction """
    if direction == Direction.down:
        pos.y += 1
    if direction == Direction.up:
        pos.y -= 1
    if direction == Direction.left:
        pos.x -= 1
    if direction == Direction.right:
        pos.x += 1

    return pos


def search_network(network):
    """ Search the network for letters, and calculate the steps needed """
    direction = Direction.down
    pos = Position(network[0].index('|'), 0)

    word = ""
    steps = 0

    stop = False

    while not stop:
        char = network[pos.y][pos.x]

        if char in ["|", "-"]:
            pos = move(direction, pos)

        elif char in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            word += char
            pos = move(direction, pos)

        elif char == '+':
            if direction == direction.down or direction == direction.up:
                if network[pos.y][pos.x-1] != ' ':
                    direction = direction.left
                else:
                    direction = direction.right

            else:
                if network[pos.y - 1][pos.x] != ' ':
                    direction = direction.up
                else:
                    direction = direction.down
            pos = move(direction, pos)

        else:
            # Nothing useful detected in front of us
            stop = True
            continue

        steps += 1
        # printNetwork(network, pos)

    return word, steps


if __name__ == '__main__':
    network = open("input.txt").read().splitlines()

    for x, line in enumerate(network):
        network[x] = line.ljust(len(max(network, key=len)))

    print("Letters: %s, steps: %d" % search_network(network))
