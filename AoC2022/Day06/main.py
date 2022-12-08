import time

def p1(input):
    i = 0
    while i < len(input) - 3:
        buffer = input[i:i+4]
        if len(set(input[i:i+4])) == 4:
            print(i + 4)
            break
        i += 1
    
def p2(input):
    i = 0
    while i < len(input) - 3:
        buffer = input[i:i+14]
        if len(set(input[i:i+14])) == 14:
            print(i + 14)
            break
        i += 1
    
def main():
    with open('AoC2022/Day06/input.txt') as f:
        input = f.read()
    
    p1(input)
    p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))