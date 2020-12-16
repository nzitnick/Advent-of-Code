from time import time

def problem1(lines):
    mem = {}
    for x in lines:
        x = x.split()
        location = x[0]
        if location == 'mask':
            mask = x[2]
        else:
            task = int(x[2])
            i = -1
            while True:
                if mask[i] == '1':
                    task = task | 1 << (-i -1)
                elif mask[i] == '0':
                    task = task & ~(1 << (-i -1))
                i -= 1
                if i < -len(mask) :
                    break
            mem[int(location[4:-1])] = task
    #print(mem)
    print(sum(list(mem.values())))    

def maskSet(value, mask, i, address, mem):
    while True:
        if mask[i] == '1':
            address = address | 1 << (-i -1)
        elif mask[i] == 'X':
            if i - 1 < -len(mask):
                address = address & ~(1 << (-i -1))
                mem[address] = value
                address = address | 1 << (-i -1)
                mem[address] = value
            else:
                address = address & ~(1 << (-i -1))           
                mem = maskSet(value, mask, i - 1, address, mem)
                address = address | 1 << (-i -1)
                mem = maskSet(value, mask, i - 1, address, mem)
        i -= 1
        if i < -len(mask) :
            break
    mem[address] = int(value)
    return mem


def problem2(lines):
    mem = {}
    for x in lines:
        x = x.split()
        address = x[0]
        if address == 'mask':
            mask = x[2]
        else:
            task = int(x[2])
            mem = maskSet(task, mask, -1, int(address[4:-1]), mem)
    #print(mem)
    print(sum(list(mem.values())))    

def main():
    startTime = time()
    with open('input.txt') as f:
        lines = f.read().splitlines()
    #problem1(lines)
    problem2(lines)
    print('runtime: {}'.format(time() - startTime))

if __name__ == '__main__':
    main()