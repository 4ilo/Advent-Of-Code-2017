

def spread(banks, highest):
    """ Spread the higest memory bank over the others """
    orig_val = banks[highest]
    banks[highest] = 0
    index = highest + 1

    for i in range(orig_val):
        if index >= len(banks):
            index = 0

        banks[index] += 1
        index += 1

    return banks


# banks = [0, 2, 7, 0]
banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

found = [banks[:]]
counter = 1

stop = False

while not stop:
    highest = banks.index(max(banks))
    banks = spread(banks, highest)
    print(banks)

    if banks not in found:
        found.append(banks[:])
        counter += 1
    else:
        stop = True


print("Cycles: %d" % counter)
print("Between: %d" % (counter - found.index(banks)))
