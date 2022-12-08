


def p1(input):
    print(input)
    elfs = []
    elf = []
    for x in input:
        if x == "":
            elfs.append(elf)
            elf = []
            continue
        elf.append(int(x))
    print(elfs)
    sumElfs = []
    for x in elfs:
        sumElfs.append(sum(x)) 
    print(sumElfs)
    s = sorted(sumElfs)
    print(sum(s[-3:]))
    #print(max(sumElfs))



def main():
    with open('AoC2022/Day01/input.txt') as f:
        input = f.read().splitlines()
    p1(input)

    

if __name__ == '__main__':
    main()