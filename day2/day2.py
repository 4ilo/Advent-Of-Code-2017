
def part1(data):
    sum = 0

    for i in range(len(data)):
        row = data[i].split(' ')
        row = sorted(row, key=lambda x: int(x))

        lowest = int(row[0])
        highest = int(row[-1])

        dif = highest - lowest
        sum = sum + highest-lowest

    return sum


def find(row):
    for x in range(len(row)):
        for y in range(x + 1, len(row)):
            if int(row[x]) % int(row[y]) == 0:
                return int(row[x]) / int(row[y])

    return False


def part2(data):
    sum = 0

    for i in range(len(data)):
        row = data[i].split(' ')

        value = find(row)
        if not value:
            value = find(row[::-1])

        sum = sum + value

    return sum


data = open('input.txt').read().split('\n')

print("Part1: %d" % part1(data))
print("Part2: %d" % part2(data))
