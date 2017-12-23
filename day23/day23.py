
def get_value(key, registers):
    """ Get the value for the given key if in the registers. """
    if key in registers:
        return registers[key]

    return int(key)


def part1(instructions):
    """ Calculate the amount of mul instructions executed """
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}

    pointer = 0
    mul_count = 0

    while True:
        parts = instructions[pointer].split(" ")
        jump_offset = 1

        if parts[0] == "set":
            registers[parts[1]] = get_value(parts[2], registers)

        elif parts[0] == 'sub':
            registers[parts[1]] -= get_value(parts[2], registers)

        elif parts[0] == 'mul':
            registers[parts[1]] *= get_value(parts[2], registers)
            mul_count += 1

        elif parts[0] == 'jnz':
            if get_value(parts[1], registers) != 0:
                jump_offset = get_value(parts[2], registers)

        pointer += jump_offset

        if pointer >= len(instructions):
            return mul_count


def is_prime(d):
    """ Perform the test expression extraced of the asm logic """
    i = 2
    while i*i <= d:
        if d % i == 0:
            return False

        i += 1
    return True


def part2(instructions):
    """ Calculate the amount of mul instructions executed """
    start = int(instructions[0].split(' ')[2])      # Initial value of b
    mul = int(instructions[4].split(' ')[2])        # Multyply b with
    subb = int(instructions[5].split(' ')[2])       # Substract from b
    subc = int(instructions[7].split(' ')[2])       # Substract from c

    b = start * mul - subb
    c = b - subc
    g = 0

    stop = False

    while not stop:
        if not is_prime(b):
            g += 1

        if b == c:
            stop = True
        b += 17

    return g


if __name__ == '__main__':
    instructions = open('input.txt').read().splitlines()
    print("Mul instruction count: %d" % part1(instructions[:]))
    print("Value of h: %d" % part2(instructions[:]))
