
def remove_garbage(stream):
    """ Remove the garbage, and count the amount of garbage """
    garbage = False
    data = ""
    garbage_count = 0

    for index, char in enumerate(stream):
        if not garbage:
            if char == '<':
                garbage = True
            else:
                data += char

        else:
            if stream[index - 1] == '!':
                # Remove the next char
                stream = stream[:index] + '0' + stream[index+1:]
            elif char == '>':
                garbage = False
            elif char != '!':
                garbage_count += 1

    return data, garbage_count


def group_score(stream):
    """ Get the score for the remaining groups """
    score = 0
    open = 0

    for char in stream:
        if char == '{':
            open += 1

        elif char == '}':
            score += open
            open -= 1

    return score


if __name__ == '__main__':
    stream = open('input.txt').read()

    stream, garbage_count = remove_garbage(stream)

    print("Score: %d" % group_score(stream))
    print("Garbage count: %d" % garbage_count)

