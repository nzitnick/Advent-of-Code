from time import time

def problem1(cups):
    i = 0
    for index in range(1000000):
        current = cups[i]
        destination = current - 1     
        pickUp = []
        for x in range(3):
            if i + 1 < len(cups):
                offset = i + 1
            else: 
                offset = 0
            pickUp.append(cups.pop(offset))

        while True:
            if destination in cups:
                for x in range(3):
                    cups.insert(cups.index(destination) + 1, pickUp.pop())
                i = (cups.index(current) + 1) % len(cups)
                break
            else:
                destination -= 1
                if destination <= 0:
                    destination = max(cups)
    print(cups)


def problem2(cups):
    dictCups = {}
    for i, x in enumerate(cups):
        try:
            dictCups[x] = cups[i+1]
        except IndexError:
            dictCups[x] = cups[0]
    current = cups[0]
    for index in range(10000000):
        pickUp = [dictCups[current],dictCups[dictCups[current]],dictCups[dictCups[dictCups[current]]]]
        dictCups[current] = dictCups[dictCups[dictCups[dictCups[current]]]]
        destination = current
        while True:
            destination -= 1
            if destination <= 0:
                destination = len(cups)
            if destination in pickUp:
                continue
            temp = dictCups[destination]
            dictCups[destination] = pickUp[0]
            dictCups[pickUp[2]] = temp
            break
        current = dictCups[current]

    print(dictCups[1] * dictCups[dictCups[1]])

                
def main():
    startTime= time()
    with open('input.txt') as f:
        line = f.read().split()
    cups = [int(i) for i in line[0]]
    cups += range(10, 1000001)
    #print(cups)
    #problem1(cups)
    problem2(cups)
    print('runtime: {}'.format(time() - startTime))
if __name__ == '__main__':
    main()
