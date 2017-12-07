
class Node:
    def __init__(self, name, weight):
        self.value = int(weight)
        self.name = name
        self.children = []

    def __str__(self):
        output = self.name + ' ' + str(self.value) + '\n'
        for child in self.children:
            output += '\t' + str(child)

        return output

    def append(self, node):
        self.children.append(node)

    def weight(self):
        sum = self.value
        for child in self.children:
            sum += child.weight()

        return sum

    def balanced(self):
        weights = [x.weight() for x in self.children]

        # Order and count the values
        test = dict([[x, weights.count(x)] for x in set(weights)])
        test = sorted(test.items(), key=lambda x:x[1])

        if len(test) == 1:
            return True

        else:
            wrong = test[0][0]
            diff = test[1][0] - test[0][0]
            for child in self.children:
                if child.weight() == wrong:
                    return (child, diff)