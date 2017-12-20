
class Particle:
    def __init__(self, p, v, a, id):
        self.p = p
        self.v = v
        self.a = a
        self.id = id

    def __str__(self):
        return str(self.id) + ': ' + str(self.p) + str(self.v) + str(self.a)

    def distance(self):
        """ Calculate the distance of the particle to 0,0,0 """
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def move(self):
        """ Move the particle 1 time """
        self.v = tuple(p + q for p, q in zip(self.v, self.a))
        self.p = tuple(p + q for p, q in zip(self.p, self.v))
