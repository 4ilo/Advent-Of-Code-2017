
class Thread:

    def __init__(self, id):
        """ Constructor, the id is the value of register p """
        self.registers = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': id
        }

        self.queue = []
        self.pointer = 0
        self.send = []

    def run(self, instructions):
        """ Run 1 instruction based on the pointer and the queue """
        parts = instructions[self.pointer].split(" ")
        jump_offset = 1
        ret_val = False

        if parts[0] == "set":
            self.registers[parts[1]] = get_value(parts[2], self.registers)

        elif parts[0] == 'add':
            self.registers[parts[1]] += get_value(parts[2], self.registers)

        elif parts[0] == 'mul':
            self.registers[parts[1]] *= get_value(parts[2], self.registers)

        elif parts[0] == 'mod':
            self.registers[parts[1]] = self.registers[parts[1]] % get_value(parts[2], self.registers)

        elif parts[0] == 'snd':
            ret_val = str(get_value(parts[1], self.registers))
            self.send.append(ret_val)

        elif parts[0] == 'rcv':
            if len(self.queue) == 0:
                return 'wait'

            self.registers[parts[1]] = self.queue.pop(0)

        elif parts[0] == 'jgz':
            if get_value(parts[1], self.registers) > 0:
                jump_offset = get_value(parts[2], self.registers)

        self.pointer += jump_offset

        return ret_val

    def add_queue(self, number):
        """ Add a number to the queue """
        self.queue.append(int(number))

    def __str__(self):
        return str(self.pointer) + '-' + str(self.queue)


def get_value(key, registers):
    """ Get the value for the given key if in the registers. """
    if key in registers:
        return registers[key]

    return int(key)
