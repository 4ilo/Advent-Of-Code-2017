
def get_steps(instructions, part2=False):
    """ Count the steps needed to exite the instruction list """
    index = 0
    stop = False
    steps = 0

    while not stop:
        jump = instructions[index]

        # For part 2 we need to subtract 1 if the value is larger then 3
        if part2:
            if jump >= 3:
                instructions[index] -= 1
            else:
                instructions[index] += 1
        else:
            instructions[index] += 1

        if index + jump >= len(instructions):
            stop = True
        else:
            index += jump

        steps += 1

    return steps


instructions = open("input.txt").read().split("\n")
instructions = [int(value) for value in instructions]

print("Steps part1: %d" % get_steps(instructions[:]))
print("Steps part2: %d" % get_steps(instructions, part2=True))
