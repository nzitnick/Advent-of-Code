import time

def p1(input):
    dics = []
    sizes = {}
    for x in input:
        x = x.split()
        if x[0] == "$":
            if x[1] == "cd":
                if x[2] == "..":
                    dics.pop()   
                else:
                    dics.append(x[2])
                    name = ""
                    for y in dics:
                        name += y + "/"
                    if name not in sizes:
                        sizes[name] = 0
                    if x[2] == "/":
                            dics = ["/"]
            continue
        
        elif x[0] != "dir":
            name = ""
            for y in dics:
                name += y + "/"
                sizes[name] += int(x[0])
            
    total = 0
    for x in sizes.values():
        if x <= 100000:
            total += x
    print(total)
    
    values = sorted(sizes.values())
    for x in values:
        if x > 30000000 - (70000000 - values[-1]):
            print(x)
            break
    
    
#def p2(input):
    
    
def main():
    with open('AoC2022/Day07/input.txt') as f:
        input = f.read().splitlines()
    
    p1(input)
    #p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))