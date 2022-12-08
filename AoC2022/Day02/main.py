import time

def p1(input):
    #print(input)
    score = 0
    cheatsheet = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    for x in input:
        score += cheatsheet[x]
    print(score)

def p2(input):
    score = 0
    cheatsheet = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    for x in input:
        score += cheatsheet[x]
    print(score)

def main():
    with open('AoC2022/Day02/input.txt') as f:
        input = f.read().splitlines()
    p1(input)
    p2(input)

    

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))