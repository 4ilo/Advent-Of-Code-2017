import re
from node import *


def create_nodes(name, data):
    """ Create a node in the tree, starting from the given value """
    for line in data:
        m = re.search("(\w+) \((\d+)\)", line)
        if m:
            if m.groups()[0] == name:
                line = line.replace(m.group(), '')
                node = Node(m.groups()[0], m.groups()[1])

                if line != "":

                    m2 = re.search(" -> ((\w+),) ((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+))$", line)
                    if m2:
                        for i in range(len(m2.groups())):
                            if i % 2 != 0 and m2.groups()[i] is not None:
                                child_node = create_nodes(m2.groups()[i], data)
                                node.append(child_node)
                return node


def part1(data):
    programs = []
    on_top = []

    for line in data:
        # Match first part pbga (66) and store in list
        m = re.search("(\w+) \((\d+)\)", line)
        if m:
            line = line.replace(m.group(), "")
            top = False
            if line != "":

                # Make a list of all programs, that appear as a child
                m2 = re.search(
                    " -> ((\w+),) ((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+), )?((\w+))$", line)
                if m2:
                    for i in range(len(m2.groups())):
                        if i % 2 != 0 and m2.groups()[i] is not None:
                            on_top.append(m2.groups()[i])
                            top = True

            programs.append({
                "name": m.groups()[0],
                "weight": m.groups()[1],
                "top": top
            })

    # Loop over the list of programs to find the one without a parent
    for program in programs:
        if program["name"] not in on_top and program["top"]:
            return program["name"]


def part2(data, first):
    node = (create_nodes(first, data), 0)

    stop = False
    while not stop:
        new_node = node[0].balanced()
        if new_node == True:
            value = node[0].value + node[1]
            stop = True

        node = new_node

    return value


data = open('input.txt').read().split('\n')
first = 'uownj'

print('Root program: ' + part1(data[:]))
print('weight: %d' % part2(data[:], first))
