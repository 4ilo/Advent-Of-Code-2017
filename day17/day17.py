

def part1(step):
    """ Calculate the value next to 2017 after 2017 cycles """
    buffer = [0]
    pos = 0

    for i in range(2017):
        pos = (step + pos) % len(buffer) + 1
        buffer.insert(pos, i+1)

    return buffer[buffer.index(2017) + 1]


def part2(step):
    """ Calculate the value next to 0 after 50000000 cycles"""
    pos = 0
    value = 0

    for i in range(1, 50000000 + 1):
        pos = ((step + pos) % i) + 1
        if pos == 1:
            value = i

    return value


if __name__ == "__main__":
    input = 343

    print("Value after 2017: %d" % part1(input))
    print("Value after 0 with 50000000 cycles: %d" % part2(input))
