
def findSeatID(lines):
    biggest = 0
    seatList = []
    for x in lines:
        x = x.replace('B', '1')
        x = x.replace('F', '0')
        x = x.replace('R', '1')
        x = x.replace('L', '0')
        
        value = int(x, 2)
        seatList.append(value)
        if value > biggest:
            biggest = value
    print(biggest)

    print(set(range(min(seatList), max(seatList))).difference(set(seatList)))


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()  
    findSeatID(lines)

if __name__ == '__main__':
    main()