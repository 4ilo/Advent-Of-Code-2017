# Perfect explanaion of hex grids
# https://www.redblobgames.com/grids/hexagons/


def distance(x, y, z):
    """ Calculate the distance to the start (0,0,0) """
    return (abs(x) + abs(y) + abs(z))/2


data = open("input.txt").read().split(",")

x_pos = 0
y_pos = 0
z_pos = 0

coords = []

for direction in data:
    if direction == "n":
        y_pos += 1
        z_pos -= 1
    elif direction == "s":
        y_pos -= 1
        z_pos += 1
    elif direction == "ne":
        x_pos += 1
        z_pos -= 1
    elif direction == "se":
        x_pos += 1
        y_pos -= 1
    elif direction == "sw":
        x_pos -= 1
        z_pos += 1
    elif direction == "nw":
        x_pos -= 1
        y_pos += 1

    coords.append(distance(x_pos, y_pos, z_pos))

print("X: %d, Y:%d, Z: %d" % (x_pos, y_pos, z_pos))
print("Distance: %d" % distance(x_pos, y_pos, z_pos))
print("Largest distance: %d" % max(coords))
