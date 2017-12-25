from input import *


def part1(states, check_after, start_state='a'):
    """ Calculate the checksum after x times """
    tape = [0 for x in range(100000)]
    cursor = len(tape) // 2
    current_state = start_state

    for x in range(check_after):
        actions = states[current_state]
        value = tape[cursor]

        tape[cursor] = actions['write'][value]
        cursor += actions['move'][value]
        current_state = actions['next'][value]

    return tape.count(1)


if __name__ == '__main__':
    print('Checksum(example) after 6: %d' % part1(states_example, 6))
    print('Checksum after 12964419: %d' % part1(states, 12964419))
