import re


def part1(programs, instructions):
    """ Calculate 1 dance """
    for instruction in instructions:
        m = re.search("s(\d+)", instruction)
        if m:
            num = int(m.groups()[0])
            programs = programs[len(programs) - num:] + programs[:len(programs) - num]
            continue

        m = re.search("x(\d+)\/(\d+)", instruction)
        if m:
            pos1 = int(m.groups()[0])
            pos2 = int(m.groups()[1])

            tmp = programs[pos1]
            programs[pos1] = programs[pos2]
            programs[pos2] = tmp
            continue

        m = re.search("p(\w)\/(\w)", instruction)
        if m:
            pos1 = programs.index(m.groups()[0])
            pos2 = programs.index(m.groups()[1])

            tmp = programs[pos1]
            programs[pos1] = programs[pos2]
            programs[pos2] = tmp
            continue

    return programs


def part2(programs, instructions):
    """ Calculate 1000000000 dances """
    cache = []
    iterations = 1000000000 - 1

    for x in range(iterations):
        s = ''.join(programs)
        if s not in cache:
            cache.append(s)
        else:
            # It is not needed to run 1000000 times, after x try's, the sequence repeats itself
            return cache[iterations % x]

        programs = part1(programs, instructions)

    return programs


if __name__ == "__main__":

    programs = [chr(i) for i in range(ord('a'), ord('p')+1)]
    instructions = open("input.txt").read().split(",")

    programs = part1(programs, instructions)
    print("Programs part1: %s" % "".join(programs))

    programs = part2(programs, instructions)
    print("Programs part2: %s" % "".join(programs))
