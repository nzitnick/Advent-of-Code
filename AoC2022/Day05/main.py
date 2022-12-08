import time

def p1(input):
    instruc = input[input.index('') + 1:]
    
    crates = []
    for i in range(0, len(input[0]) // 4 + 1):
        crates.append([])
    for x in input[:input.index('')]:
        i = 1
        while i < len(x):
            if x[i].isalpha():
                crates[i // 4].append(x[i])
            i += 4
            
    for x in instruc:
        x = x.split()
        count = int(x[1])
        start = int(x[3])
        finish = int(x[5])
        for i in range(0,count):
            move = crates[start - 1].pop(0)
            crates[finish - 1].insert(0, move)
    result = ''
    for x in crates:
        result += x[0]
    print(result)

def p2(input):
    instruc = input[input.index('') + 1:]
    
    crates = []
    for i in range(0, len(input[0]) // 4 + 1):
        crates.append([])
    for x in input[:input.index('')]:
        i = 1
        while i < len(x):
            if x[i].isalpha():
                crates[i // 4].append(x[i])
            i += 4
            
    for x in instruc:
        x = x.split()
        count = int(x[1])
        start = int(x[3])
        finish = int(x[5])
        for i in range(0,count):
            move = crates[start - 1].pop(0)
            crates[finish - 1].insert(i, move)

    result = ''
    for x in crates:
        result += x[0]
    print(result)
    
def main():
    with open('AoC2022/Day05/input.txt') as f:
        input = f.read().splitlines()
    
    
    p1(input)
    p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))