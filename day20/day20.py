import re
from Particle import *


def parse_particles(input):
    """ Parse the input into a particles array """
    particles = []

    for x, line in enumerate(input):
        m = re.search("p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>", line)
        if m:
            p = (int(m.groups()[0]), int(m.groups()[1]), int(m.groups()[2]))
            v = (int(m.groups()[3]), int(m.groups()[4]), int(m.groups()[5]))
            a = (int(m.groups()[6]), int(m.groups()[7]), int(m.groups()[8]))

            particles.append(
                Particle(p, v, a, x)
            )

    return particles


def check_collide(particles):
    """ Remove all colliding particles"""
    delete = set()

    for part1 in particles:
        for part2 in particles:
            if part1 != part2 and part1.p == part2.p:
                delete.add(part1.p)

    particles = [part for part in particles if part.p not in delete]
    return particles


def solve(particles, part2=False):
    """
        Get the index of the closest particle after a long term,
        and the remaining particles for part2
    """
    for x in range(2000):
        for particle in particles:
            particle.move()

        if part2:
            particles = check_collide(particles)

    particles = sorted(particles, key=lambda k: k.distance())

    if part2:
        return len(particles)
    else:
        return particles[0].id


if __name__ == '__main__':
    input = open("input.txt").read().splitlines()

    particles = parse_particles(input)
    print('Closest particle: %d' % solve(particles))

    particles = parse_particles(input)
    print('Particles left: %d' % solve(particles, part2=True))
