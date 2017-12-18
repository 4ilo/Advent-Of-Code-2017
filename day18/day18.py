from Thread import *


def part1(instructions):
    """ Get the first frequency that wants to be recovered """
    registers = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0
    }

    played = []
    pointer = 0

    while True:
        parts = instructions[pointer].split(" ")
        jump_offset = 1

        if parts[0] == "set":
            registers[parts[1]] = get_value(parts[2], registers)

        elif parts[0] == 'add':
            registers[parts[1]] += get_value(parts[2], registers)

        elif parts[0] == 'mul':
            registers[parts[1]] *= get_value(parts[2], registers)

        elif parts[0] == 'mod':
            registers[parts[1]] = registers[parts[1]] % get_value(parts[2], registers)

        elif parts[0] == 'snd':
            played.append(int(registers[parts[1]]))

        elif parts[0] == 'rcv':
            if registers[parts[1]] != 0:
                return played.pop()

        elif parts[0] == 'jgz':
            if get_value(parts[1], registers) > 0:
                jump_offset = get_value(parts[2], registers)

        pointer += jump_offset


def part2(instructions):
    """ Get the amount of times thread1 send a value by the time we reach a deadlock """
    thread0 = Thread(0)
    thread1 = Thread(1)

    while True:
        val1 = thread0.run(instructions)
        if val1 and val1 != 'wait':
            thread1.add_queue(val1)

        val2 = thread1.run(instructions)
        if val2 and val2 != 'wait':
            thread0.add_queue(val2)

        if val1 == val2 == 'wait':
            return len(thread1.send)


if __name__ == '__main__':
    instructions = open("input.txt").read().split("\n")

    print('Recovered freq: %d' % part1(instructions))
    print('Thread1 send %d times.' % part2(instructions))
