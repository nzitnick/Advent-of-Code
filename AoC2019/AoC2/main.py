
def problem1(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    i = 0
    while True:
        op = intcode[i]
        if op == 99 or i > len(intcode) + 3:
            break
        a = intcode[i + 1]
        b = intcode[i + 2]
        reg = intcode[i + 3]

        if op == 1:
            intcode[reg] = intcode[a] + intcode[b]
        elif op == 2:
            intcode[reg] = intcode[a] * intcode[b]
        i += 4

    return intcode[0]


def problem2(intcode):
    for x in range(100):
        for y in range(100):
            #print(problem1(intcode.copy(), x, y))
            if problem1(intcode.copy(), x, y) == 1202:
                print('noun: {}'.format(x))
                print('verb: {}'.format(y))
                print(100 * x + y)
                return


def main():
    with open('input.txt') as f:
        lines = f.read().split(',')
    intcode = [int(i) for i in lines]
    print(problem1(intcode.copy(), 12, 2))
    problem2(intcode)


if __name__ == '__main__':
    main()