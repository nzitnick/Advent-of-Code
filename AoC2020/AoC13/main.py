from time import time

def problem1(timestamp, buses):
    diff = {} 
    for bus in buses:
        if bus != 'x':
            diff[bus] = (int(bus) - (int(timestamp) % int(bus)))
    print(int(list(diff.keys())[list(diff.values()).index(min(list(diff.values())))]) * min(list(diff.values())))

def crt(buses):
    N = 1
    x = 0
    for bus in buses:
        if bus == 'x':
            continue 
        N *= int(bus)
    i = 0
    for bus in buses:
        if bus == 'x':
            i += 1
            continue
        mod = int(bus)
        Ni = N // mod
        index = 1
        while True:
            if ((Ni % mod) * index) % mod == 1:
                Xi = index
                break
            index += 1
        x += i * Ni * Xi
        i += 1
    print(N - (x % N))


def findArrival(x, y, gap, inc):
    sumy = y
    i = 1
    #print(((inc - ((sumy - x) % inc - gap)) / y))
    while True:
        if (sumy - x) % inc - gap == 0:
            print('y: {}'.format(sumy))
            print('i: {}'.format(i))
            print('#####################')
            return sumy 
        else:
            #print((inc - ((sumy - x) % inc - gap)) // y)
            sumy += y
            i += 1

def problem2(buses):

    i = 1
    gap = 1
    sumy = int(buses[0])
    inc = int(buses[0])
    while True:
        if i > len(buses) -1:
            print(sumy - len(buses) + 1)
            return
        if buses[i] == 'x':
            gap += 1
            i += 1
            continue
        else: 
            sumy = findArrival(sumy, int(buses[i]), gap, inc)
            inc *= int(buses[i])
            gap = 1
        i += 1


def main():
    startTime = time()
    with open('input.txt') as f:
        lines = f.read().splitlines()
    timestamp, buses = lines
    buses = buses.split(',')
    #problem1(timestamp, buses)
    crt(buses)
    print('runtime: {}'.format(time() - startTime))
    

if __name__ == '__main__':
    main()





