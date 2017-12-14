from day10 import *


def get_hashes(input):
    """ Calculate 128 hashes for the given input """
    hashes = []
    for x in range(128):
        hashes.append(day10(input + "-" + str(x)))

    return hashes


def part1(hashes):
    """ Calculate the used spaces """
    used = 0

    for i, hash in enumerate(hashes):
        hashes[i] = format(int(hash, 16), "b").zfill(128)
        used += hashes[i].count('1')

    return used, hashes


def part2(hashes):
    """ Count the number of regions """
    count = 0
    ungrouped = []

    for i, hash in enumerate(hashes):
        ungrouped += [(i, j) for j, bit in enumerate(hashes[i]) if bit == "1"]

    while ungrouped:
        current = [ungrouped[0]]
        while current:
            (x, y) = current.pop()
            if (x, y) in ungrouped:
                ungrouped.remove((x, y))
                current += [(x - 1, y), (x+1, y), (x, y+1), (x, y-1)]
        count += 1

    return count


if __name__ == "__main__":
    input = "hwlqcszp"

    hashes = get_hashes(input)

    used, hashes = part1(hashes)
    print("Places used: %d" % used)
    print("Region count: %d" % part2(hashes))
