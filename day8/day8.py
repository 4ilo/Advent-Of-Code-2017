import re


def get_reg(name, registers):
    """ Get the value for the register or create the register """
    if name not in registers:
        registers.update({
            name: 0
        })

    return registers[name]


def compare(reg1, reg2, comp):
    """ Compare the 2 values with the comparator """
    if comp == '>':
        return reg1 > reg2
    elif comp == '<':
        return reg1 < reg2
    elif comp == '>=':
        return reg1 >= reg2
    elif comp == '<=':
        return reg1 <= reg2
    elif comp == '==':
        return reg1 == reg2
    elif comp == '!=':
        return reg1 != reg2


def largest_register(data):
    """ Get the largest register, and the higest value """
    registers = {}
    highest = 0

    for line in data:
        m = re.search("(\w+) (inc|dec) (-?\d+) if (\w+) ((?:>|<|!|=)(?:>|<|!|=)?) (-?\d+)", line)

        if m:
            statement = m.groups()

            cmp1 = get_reg(statement[3], registers)
            cmp2 = int(statement[5])
            operator = statement[4]
            if compare(cmp1, cmp2, operator):
                get_reg(statement[0], registers)  # Make sure the reg exists

                if statement[1] == 'inc':
                    registers[statement[0]] += int(statement[2])
                else:
                    registers[statement[0]] -= int(statement[2])

                # Save the higest possible value
                if registers[statement[0]] > highest:
                    highest = registers[statement[0]]

    registers = sorted(registers.items(), key=lambda x: x[1])
    return (registers[len(registers) -1], highest)


data = open("input.txt").read().split("\n")
values = largest_register(data)

print("Highest value in register: %s" % (values[0],))
print("Highest possible value: %d" % values[1])
