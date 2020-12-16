from time import time

def problem1(numbers):
    i = 1
    mem = {}
    for x in numbers[:-1]:
        mem[x] = i
        lastnum = x
        i += 1
    lastnum = numbers[-1]
    while i < 30000000:
        if lastnum in mem.keys():
            num = str(i - int(mem[lastnum]))
            mem[lastnum] = i
            lastnum = num
        else:
            mem[lastnum] = i
            lastnum = '0'
        i += 1
    print(lastnum)

def main():
    startTime = time()
    with open('input.txt') as f:
        numbers = f.read().split(',')
    problem1(numbers)
    print('runtime: {}'.format(time() - startTime))

if __name__ == '__main__':
    main()