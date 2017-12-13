
def move_layers(layers):
    """ Move the layers once """
    for layer in layers:
        if layer["depth"]:
            if layer["dir"] == 0:
                if layer["location"] + 1 < layer["depth"]:
                    layer["location"] += 1
                else:
                    layer["location"] -= 1
                    layer["dir"] = 1
            else:
                if layer["location"] - 1 >= 0:
                    layer["location"] -= 1
                else:
                    layer["location"] += 1
                    layer["dir"] = 0

    return layers


def part1(data):
    """ Calculate the servity for the layers """

    layers = [{"depth": 0, "location": 0, "layer": x, "dir": 0} for x in range(int(data[-1].split(": ")[0]) + 1)]

    for line in data:
        tmp = line.split(": ")

        layer = layers[int(tmp[0])]
        layer["depth"] = int(tmp[1])


    packet = -1
    servity = 0

    stop = False
    while not stop:
        packet += 1
        layer = layers[packet]

        if layer["location"] == 0 and layer["depth"] != 0:
            servity += layer["depth"] * layer["layer"]

        layers = move_layers(layers)

        if packet == len(layers) - 1:
            stop = True

    return servity


def part2(data):
    """ Calculate the delay for free pasage """
    layers = []
    for line in data:
        layers.append(line.split(": "))

    count = 0

    while True:
        for layer in layers:
            if (count + int(layer[0])) % (2 * (int(layer[1]) - 1)) == 0:
                break
        else:
            return count
        count += 1


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")

    print("Servity: %d" % part1(data[:]))
    print("Free passage: %d" % part2(data))
