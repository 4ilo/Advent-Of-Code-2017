import re
from program import *


def get_prog(id, programs):
    """ Get the program linked to the id, or create one """
    for program in programs:
        if program.id == int(id):
            return program

    prog = Program(id)
    programs.append(prog)
    return prog


def link_programs(data):
    """ Link programs to each other accoring to the given data """
    programs = []

    for line in data:
        m = re.search("(\d+) <-> (?:(\d+), )?(?:(\d+), )?(?:(\d+), )?(?:(\d+), )?(?:(\d+), )?(?:(\d+), )?(?:(\d+), )?(\d+)", line)

        if m:
            for id in m.groups()[1:]:
                program =get_prog(m.groups()[0], programs)
                if id is not None:
                    prog = get_prog(id, programs)
                    program.add_link(prog)

    return programs


def part1(programs):
    """ Calculate the amount of programs in group 0 """
    count = 0
    for program in programs:
        if program.connected(0)[0]:
            count += 1

    return count


def part2(programs):
    ignore = []
    groups = []
    for index in range(len(programs)):
        groups.append([])
        if index not in ignore:
            for program in programs:
                if program.connected(index)[0]:
                    groups[index].append(program.id)
                    ignore.append(program.id)

    groups = [x for x in groups if x != []]
    return len(groups)


if __name__ == '__main__':
    data = open("input.txt").read().split("\n")
    programs = link_programs(data)

    print("Connected to 0: %d" % part1(programs[:]))
    print("Groups: %d" % part2(programs[:]))
