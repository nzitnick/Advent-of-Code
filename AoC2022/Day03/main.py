import time

def p1(input):
    prio = 0
    for x in input:
        first = x[:len(x)//2]
        second = x[len(x)//2:]
        firststuff = {}
        for y in first:
            if y in firststuff:
                continue
            firststuff[y] = y
        for y in second:
            if y in firststuff:
                value = ord(y) - 96
                if value < 0:
                    value += 58
                prio += value
                break
    print(prio)

def p2(input):
    i = 0
    prio = 0
    while i < len(input):
        first = {}
        second = {}
        for x in input[i]:
            if x in first:
                continue
            first[x] = x
        for x in input[i + 1]:
            if x in second:
                continue
            second[x] = x
        for x in input[i + 2]:
            if (x in first) and (x in second):
                value = ord(x) - 96
                if value < 0:
                    value += 58
                prio += value
                break
        i += 3
    print(prio)
        
def main():
    with open('AoC2022/Day03/input.txt') as f:
        input = f.read().splitlines()
    p1(input)
    p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))