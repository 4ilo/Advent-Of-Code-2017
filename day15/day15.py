

def generator(start, factor):
    """ Calculate the next value with the given factor and start value """
    divider = 2147483647
    next = (start * factor) % divider

    formated = bin(next)[2:]
    return formated[len(formated)-16:], next


def solve(factorA, factorB, valueA, valueB):
    """ Calculate the correct values for part 1 and 2 """
    cycles = 40000000
    correct1 = 0
    correct2 = 0

    numbersA = []
    numbersB = []

    for x in range(cycles):
        a, valueA = generator(valueA, factorA)
        b, valueB = generator(valueB, factorB)

        if valueA % 4 == 0:
            numbersA.append(a)
        if valueB % 8 == 0:
            numbersB.append(b)

        if a == b:
            correct1 += 1

    if len(numbersB) >= len(numbersA):
        tmp = numbersA
        numbersA = numbersB
        numbersB = tmp

    for x in range(len(numbersB)):
        if numbersA[x] == numbersB[x]:
            correct2 += 1

    return correct1, correct2


if __name__ == "__main__":
    factorA = 16807
    factorB = 48271

    valueA = 116
    valueB = 299

    print("Correct1: %d, Correct2: %d" % solve(factorA, factorB, valueA, valueB))

