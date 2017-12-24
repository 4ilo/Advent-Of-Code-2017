

def find_component(start_bridge, port, components):
    """ Find the next component with the given port number """
    available = [component for component in components if port in component]

    if len(available) == 0:
        return [start_bridge]

    bridge = []
    for component in available:
        remaining = components[:]
        remaining.remove(component)

        next_port = component[:]
        next_port.remove(port)

        bridge += find_component(start_bridge + [component], next_port[0], remaining)

    return bridge


def strength(bridge):
    """ Calculate the strength of the given bridge """
    strength = 0
    for component in bridge:
        for port in component:
            strength += int(port)

    return strength


def part1(bridges):
    """ Find the strongest bridge """
    best = 0
    for bridge in bridges:
        str = strength(bridge)
        if str > best:
            best = str

    return best


def part2(bridges):
    """ Find the strongest and longest bridge """
    bridges.sort(key=len, reverse=True)

    if strength(bridges[0]) > strength(bridges[1]):
        return strength(bridges[0])
    else:
        return strength(bridges[1])


if __name__ == '__main__':
    components = [x.split('/') for x in open("input.txt").read().splitlines()]

    bridges = find_component([], '0', components)

    print("Strongest Bridge: %d" % part1(bridges))
    print("Strongest and longest Bridge: %d" % part2(bridges[:]))

