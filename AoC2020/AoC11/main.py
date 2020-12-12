import copy 
from time import time

def checkAdjacent(seats, x, y):  
    count = 0
    for i, j in [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]:
        if len(seats) > i >= 0 and len(seats[0]) > j >= 0:
            if seats[i][j] == '#':
                count += 1
    return count



def problem1(seats):
    while True:
        #print('go')
        newSeats = copy.deepcopy(seats)
        for i , x in enumerate(seats):
            for j, y in enumerate(x):
                if y == 'L':
                    if checkAdjacent(seats, i, j)  == 0:
                        newSeats[i][j] = '#'
                if y == '#':
                    if checkAdjacent(seats, i, j) >= 4:
                        newSeats[i][j] = 'L'
            #print(newSeats[i])       
        if seats == newSeats:
            print(sum([i.count('#') for i in seats]))
            break
        seats = newSeats 
 

def checkAdjacent2(seats, x, y):  
    count = 0 
    index = 0
    for i, j in [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]:
        while True:   

            #print(index)
            #print(i)
            #print(j)
            #print(r)
            if not (len(seats) > i >= 0 and len(seats[0]) > j >= 0):
                break
            #print(seats[i][j])
            if seats[i][j] == '#' or seats[i][j] == 'L':
                if seats[i][j] == '#':
                    count += 1
                break
            if index < 3:
                i -=1
            elif index > 4:
                i += 1
            if index == 0 or index == 3 or index == 5:
                j -= 1
            elif index == 2 or index == 4 or index == 7:
                j += 1
        index += 1
    return count


def problem2(seats):
    while True:
        #print('go')
        newSeats = copy.deepcopy(seats)
        for i , x in enumerate(seats):
            for j, y in enumerate(x):
                if y == 'L':
                    if checkAdjacent2(seats, i, j)  == 0:
                        newSeats[i][j] = '#'
                if y == '#':
                    if checkAdjacent2(seats, i, j) >= 5:
                        newSeats[i][j] = 'L'
            #print(newSeats[i])       
        if seats == newSeats:
            print(sum([i.count('#') for i in seats]))
            break
        seats = newSeats 


def main():
    startTime = time()
    with open('inputtest.txt') as f:
        lines = f.read().splitlines()
        seats = [list(i) for i in lines] 
    #problem1(seats)
    problem2(seats)
    print('time passed {}'.format(time() - startTime))

if __name__ == '__main__':
    main()