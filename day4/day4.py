
def check_phrase(phrase):
    """ Check if a part 1 passphrase is correct """
    words = phrase.split(" ")

    table = {}

    for word in words:
        if word not in table:
            table.update({word: 1})
        else:
            return False

    return True


def check_anagram(word, letters):
    """ Check if the given word is a anagram for the given letters """
    copy = list(word)
    for letter in letters:
        if letter in copy:
            copy[copy.index(letter)] = ""
        else:
            return False

    return True


def check_anagram_phrase(phrase):
    """ Check if the given passphrase is valid for part2 """
    words = phrase.split(" ")

    table = {}

    for word in words:
        if word in table:
            return False
        elif len(table) != 0:
            for search in table:
                if check_anagram(word, list(search)) and len(search) == len(word):
                    return False

            table.update({word: word})

        else:
            table.update({word: word})

    return True


def count_correct_phrases(phrases, anagram=False):
    """ Count the number of correct phrases """
    count = 0

    for phrase in phrases:
        if anagram:
            if check_anagram_phrase(phrase):
                count += 1
        else:
            if check_phrase(phrase):
                count += 1

    return count


data = open("input.txt").read().split("\n")

print("Part1: %d" % count_correct_phrases(data))
print("Part2: %d" % count_correct_phrases(data, anagram=True))

