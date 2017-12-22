from direction import *

CLEAN = '.'
WEAKENED = 'W'
INFECTED = '#'
FLAGGED = 'F'


def burst(cluster, pos):
    """ Perform 1 burst for the standard virus (part1) """
    infected = False

    if cluster[pos.y][pos.x] == '#':
        pos.turn_right()
        cluster[pos.y][pos.x] = '.'

    else:
        pos.turn_left()
        cluster[pos.y][pos.x] = '#'
        infected = True

    pos.move()
    return pos, infected


def burst2(cluster, pos):
    """ Perform 1 burst for the mutated virus (part2) """
    infected = False

    if cluster[pos.y][pos.x] == CLEAN:
        pos.turn_left()
        cluster[pos.y][pos.x] = WEAKENED

    elif cluster[pos.y][pos.x] == INFECTED:
        pos.turn_right()
        cluster[pos.y][pos.x] = FLAGGED

    elif cluster[pos.y][pos.x] == FLAGGED:
        pos.reverse()
        cluster[pos.y][pos.x] = CLEAN

    else:
        cluster[pos.y][pos.x] = INFECTED
        infected = True

    pos.move()
    return pos, infected


def infect(small_cluster, bursts, fieldsize, part2=False):
    """ Let the virus run thrue the cluster and infect """
    cluster = [['.' for x in range(fieldsize)] for y in range(fieldsize)]

    for y, row in enumerate(small_cluster):
        for x, field in enumerate(row):
            offset = int(fieldsize / 2)
            cluster[offset + y][offset + x] = field

    start_pos = int(fieldsize/2) + int(len(small_cluster)/2)
    pos = Position(start_pos, start_pos, Direction.up)

    ingected_count = 0

    for i in range(bursts):
        if part2:
            pos, infected = burst2(cluster, pos)
        else:
            pos, infected = burst(cluster, pos)

        if infected:
            ingected_count += 1

    return ingected_count


if __name__ == '__main__':
    input = open('input.txt').read().splitlines()
    input = [list(x) for x in input]

    print("Bursts caused infection1: %d" % infect(input, 10000, fieldsize=999))
    print("Bursts caused infection2: %d" % infect(input, 10000000, fieldsize=999, part2=True))
