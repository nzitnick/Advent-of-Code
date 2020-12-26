

def problem1(cardKey, doorKey):
    print(cardKey)
    print(doorKey)
    subjectNum = 7
    #for subjectNum in range(1, 101):
    loopSize = 1
    value = 1
    while True:
        value *= subjectNum
        value = value % 20201227
        if value == cardKey:
            print(loopSize)
            break
        loopSize += 1
    loopSize = 1
    value = 1
    while True:
        value *= subjectNum
        value = value % 20201227
        if value == doorKey:
            print(loopSize)
            break
        loopSize += 1
    value = 1
    for i in range(1, loopSize + 1):
        value *= cardKey
        value = value % 20201227
    print(value)
def main():
    with open('input.txt') as f:
        [cardKey, doorKey] = f.read().split() 

    problem1(int(cardKey), int(doorKey))

if __name__ == '__main__':
    main()