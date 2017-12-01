
def captcha(data, step=1.0):
    sum = 0
    extended = data + data

    for i in range(len(data)):
        if extended[i] == extended[i + int(step)]:
            sum = sum + int(data[i])

    return sum


data = open("input.txt").read()

print("captcha 1: %d" % captcha(data))
print("captcha 2: %d" % captcha(data, len(data)/2))
