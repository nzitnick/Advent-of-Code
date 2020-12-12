from time import time

def problem1(adaptors):
    count = [0,0,0]
    prevadaptor = 0
    for x in adaptors:
        diff = x - prevadaptor
        count[diff - 1] += 1
        prevadaptor = x
    count[2] += 1
    print(count)


def path(adaptors, count, prevadaptor, prevPath):
    i = 0
    while True:
        if  not adaptors:
            count +=1
            return count
        if adaptors[i] == adaptors[-1]:
            count += 1
            return count


        if i + 1 < len(adaptors): 
            if adaptors[i + 1] - prevadaptor <= 3: 
                if str(adaptors[i + 2:]) not in prevPath.keys():      
                    prevPath[str(adaptors[i + 2:])] = path(adaptors[i + 2:], 0, adaptors[i + 1], prevPath)
                ans = prevPath[str(adaptors[i + 2:])]
                count += ans
        
        if i + 2 < len(adaptors): 
            if adaptors[i + 2] - prevadaptor <= 3:     
                if str(adaptors[i + 3:]) not in prevPath.keys():
                    prevPath[str(adaptors[i + 3:])] = path(adaptors[i + 3:], 0, adaptors[i + 2], prevPath)
                ans = prevPath[str(adaptors[i + 3:])]
                count += ans
        
        prevadaptor = adaptors[i]
        i += 1


def main():
    startTime = time()
    with open('input.txt') as f:
        lines = f.read().splitlines()
        adaptors = [int(i) for i in lines]
    adaptors.sort()
    prevPath = {}
    print(path(adaptors, 0, 0, prevPath))
    print('run time {}'.format(time() - startTime))

if __name__ == '__main__':
    main()