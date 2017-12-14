

def wrap_around(list, position, length):
    """ Calculate the list if the sublist wraps around """
    pos1 = position
    pos2 = position + length - 1
    pos2 = pos2 % len(list)

    temp_list = []

    if pos2 < pos1:
        for i in range(pos1, len(list)):
            temp_list.append(list[i])

        for i in range(0, pos2 + 1):
            temp_list.append(list[i])

        temp_list.reverse()

        for i in range(pos1, len(list)):
            list[i] = temp_list.pop(0)

        for i in range(0, pos2 + 1):
            list[i] = temp_list.pop(0)

    return list


def knot_hash(list, position, skip_size, input_lengths):
    """ Generate 1 round of the knot hash """
    for length in input_lengths:
        if length > len(list):
            print("Invalid length!")
            exit(0)

        if position + length > len(list):
            list = wrap_around(list, position, length)
        else:
            list[position:position + length] = list[position:position + length][::-1]

        position = (position + length + skip_size) % len(list)
        skip_size += 1

    return list, position, skip_size


def dense_hash(spare_hash):
    """ Generate the dens hash from the given spare hash """
    dense_hash = []
    for x in range(16):
        xor = 0
        for i in range(16):
            xor = xor ^ spare_hash[i]
        dense_hash.append(xor)
        spare_hash = spare_hash[16:]

    return dense_hash


def part1(input_lengths):
    """ Use the input as lengths and generate a multiplication of the first 2 numbers """
    list = [x for x in range(256)]
    position = 0
    skip_size = 0
    input_lengths = [int(x) for x in input_lengths]

    list = knot_hash(list, position, skip_size, input_lengths)[0]

    return list[0] * list[1]


def day10(input_lengths):
    """ Calculate the hash for the given input string """
    input_lengths = [ord(c) for c in input_lengths]
    input_lengths += [17, 31, 73, 47, 23]

    list = [x for x in range(256)]
    position = 0
    skip_pos = 0

    for x in range(64):
        (list, position, skip_pos) = knot_hash(list, position, skip_pos, input_lengths)

    hash = dense_hash(list)
    hash = [format(i, 'x').zfill(2) for i in hash]
    hash_string = "".join(hash)

    return hash_string


# input_lengths = open("input.txt").read()
# print("Multiplication: %d" % part1(input_lengths.split(",")))
# print("Hash: %s" % part2(input_lengths))
