
def findSeatID(seats):
    biggest = 0
    seatList = []
    for id in seats:
        row = 0
        hort = 0
        for i, x in enumerate(id[:7]):
            if x == 'B':
                row += 64 / (2 ** i)
        for i, x in enumerate(id[7:]):
            if x == "R":
                hort += 4 / (2 ** i)
        seatList.append(int(row * 8 + hort))
        if row * 8 + hort > biggest: 
            biggest = row * 8 + hort
    print(biggest)
    seatList.sort()
    for x in range(seatList[0], seatList[-1]):
        if not(x in (seatList)):
            print(x)    


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    findSeatID(lines)


if __name__ == '__main__':
    main()