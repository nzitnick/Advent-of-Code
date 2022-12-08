import time

def p1(input):
    count = 0
    for x in input:  
        x = x.split(",")
        elfone = x[0].split("-")
        elftwo = x[1].split("-")
        if int(elfone[0]) >= int(elftwo[0]) and int(elfone[1]) <= int(elftwo[1]):
            count += 1
        elif int(elfone[0]) <= int(elftwo[0]) and int(elfone[1]) >= int(elftwo[1]):
            count += 1

    print(count)   
        #print(x)

def p2(input):
    count = 0
    for x in input:  
        x = x.split(",")
        elfone = x[0].split("-")
        elftwo = x[1].split("-")
        if int(elfone[0]) >= int(elftwo[0]) and int(elfone[1]) <= int(elftwo[1]):
            count += 1
        elif int(elfone[0]) <= int(elftwo[0]) and int(elfone[1]) >= int(elftwo[1]):
            count += 1
        elif int(elfone[0]) >= int(elftwo[0]) and int(elfone[0]) <= int(elftwo[1]):
            count += 1
        elif int(elfone[0]) <= int(elftwo[0]) and int(elfone[0]) >= int(elftwo[1]):
            count += 1
        elif int(elfone[0]) <= int(elftwo[0]) and int(elfone[1]) >= int(elftwo[0]):
            count += 1
        elif int(elfone[0]) >= int(elftwo[0]) and int(elfone[1]) <= int(elftwo[0]):
            count += 1
    print(count)
    
def main():
    with open('AoC2022/Day04/input.txt') as f:
        input = f.read().splitlines()
    p1(input)
    p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))