import time

def p1(input):
    screen = [[],[],[],[],[],[]]
    i = 1
    reg = 1
    cycle = [20, 60, 100, 140, 180, 220]
    sig = 0
    for x in input:
        x = x.split()
        if x[0] == "noop":
            i += 1
        elif x[0] == "addx":
            i += 1
            if i in cycle:
                #print("i: {} for reg: {}".format(i, reg))
                sig += i * reg
            i += 1
            reg += int(x[1])
        if i in cycle:
            #print("i: {} for reg: {}".format(i, reg))
            sig += i * reg
    
    print(sig)
def p2(input):
    screen = []
    for x in range(0, 6):
        temp = ["."] * 40 
        screen.append(temp)
    i = 1
    reg = 1
    
    if reg - 1 <= 1 % 40 and 1 % 40 <= reg + 1:
                screen[0][0] = '#'
    for x in input:
        x = x.split()
        if x[0] == "noop":
            i += 1
            if i >= 240:
                break
        elif x[0] == "addx":
            i += 1
            if reg - 1 <= (i - 1) % 40 and (i - 1) % 40 <= reg + 1:
                screen[(i-1) // 40][(i-1) % 40] = '#'

            i += 1
            reg += int(x[1])

        if reg - 1 <= (i - 1) % 40 and (i - 1) % 40 <= reg + 1:
            screen[(i-1) // 40][(i-1) % 40] = '#'
    
    for x in screen:
        print(x)
    
def main():
    with open('AoC2022/Day10/input.txt') as f:
        input = f.read().splitlines()
            
    p1(input)
    p2(input)
  

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))