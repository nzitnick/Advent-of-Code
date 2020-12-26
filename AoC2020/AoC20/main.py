import numpy as np
np.set_printoptions(linewidth=150)

def checkBorder(pictureOld, pictureNew):
    #print(pictureOld)
    #print(pictureNew)
    #allSides = [pictureNew[0], pictureNew[0][::-1], [i[0] for i in pictureNew], [i[0] for i in pictureNew][::-1], [i[-1] for i in pictureNew], [i[-1] for i in pictureNew][::-1], pictureNew[-1], pictureNew[-1][::-1]]
    #for i, x in enumerate(allSides):
    #print(x)
    i = 0
    while True:
        #print(pictureOld[0])
        #print(pictureNew[0])
        if str(pictureNew[-1]) == str(pictureOld[0]):
            #print('up')
            location = 'up'
            return pictureNew, location
            #print(i)
        elif str([i[-1] for i in pictureNew]) == str([i[0] for i in pictureOld]):
            #print('left')
            location = 'left'
            return pictureNew, location
            #print(i)
        elif str([i[0] for i in pictureNew]) == str([i[-1] for i in pictureOld]):
            #print('right')
            location = 'right'
            return pictureNew, location
            #print(i)
        elif str(pictureNew[0]) == str(pictureOld[-1]):
            #print('down')
            location = 'down'
            return pictureNew, location
            #print(i)
        else:
            if i == 8:
                pictureNew = np.flip(pictureNew, 1)
            if i == 16:
                return pictureNew, 'nope'
            pictureNew = np.rot90(pictureNew)
            i += 1
            continue
                
    '''if [i[0] for i in pictureOld] in [pictureNew[0], pictureNew[0][::-1], [i[0] for i in pictureNew], [i[0] for i in pictureNew][::-1], [i[-1] for i in pictureNew], [i[-1] for i in pictureNew][::-1], pictureNew[-1], pictureNew[-1][::-1]]:
        print('left')

    elif [i[-1] for i in pictureOld] in [pictureNew[0], pictureNew[0][::-1], [i[0] for i in pictureNew], [i[0] for i in pictureNew][::-1], [i[-1] for i in pictureNew], [i[-1] for i in pictureNew][::-1], pictureNew[-1], pictureNew[-1][::-1]]:
        print('right')

    elif pictureOld[-1] in [pictureNew[0], pictureNew[0][::-1], [i[0] for i in pictureNew], [i[0] for i in pictureNew][::-1], [i[-1] for i in pictureNew], [i[-1] for i in pictureNew][::-1], pictureNew[-1], pictureNew[-1][::-1]]:
        print('bottom')
    print(pictureNew[0])
    print([i[0] for i in pictureNew])'''

def problem1(pictures):
    grid =  [[[] for col in range(29)] for row in range(29)]
    tileGrid = [['' for col in range(29)] for row in range(29)]
    placedTiles = []
    first = True
    tilesPlaced = 0
    print(len(pictures))
    run = True
    i = 0
    while run:
        for x in pictures:
            x = x.split()
            picNum = x[1][:-1]
            x = np.array([list(i) for i in x[2:]])
            #print('')
            #print(x)
            if first:
                grid[14][14] = x
                tileGrid[14][14] = picNum
                placedTiles.append(picNum)
                first = False
                tilesPlaced += 1
                #i += 1
                continue
            if picNum not in placedTiles:
                for f, j in enumerate(grid):
                    for g, k in enumerate(j):                       
                        if k != []:
                            if picNum not in placedTiles:
                                #print('ooops')
                                x, location = checkBorder(k, x)
                                if location == 'nope':
                                    continue
                                elif location == 'up':
                                    grid[f - 1][g] = x
                                    tileGrid[f - 1][g] = picNum
                                    placedTiles.append(picNum)
                                elif location == 'down':
                                    grid[f + 1][g] = x
                                    tileGrid[f + 1][g] = picNum
                                    placedTiles.append(picNum)
                                elif location == 'left':
                                    grid[f][g - 1] = x
                                    tileGrid[f][g - 1] = picNum
                                    placedTiles.append(picNum)
                                elif location == 'right':
                                    grid[f][g + 1] = x
                                    tileGrid[f][g + 1] = picNum
                                    placedTiles.append(picNum)
                                #print(picNum)
                                tilesPlaced += 1
            if tilesPlaced >= len(pictures):
                run = False
                break
            
        #run = False
    #print('zzzzzzzzzzzzzzzzzz')
    '''for x in grid:
        for y in x:
            if y != []:
                for z in y:
                    print(z)'''
    for x in tileGrid:
        print(x)
    return grid


def problem2(grid):
    testPicture = []
    for y in range(5,17):
        temp = []
        for x in range(8, 20):
            #print(y , x)
            temp.append(grid[y][x])
        testPicture.append(temp)
    grid = [[grid[1][2], grid[1][3], grid[1][4]], [grid[2][2], grid[2][3], grid[2][4]], [grid[3][2], grid[3][3], grid[3][4]]]
    test = grid.copy()
    for i in range(12):
        for j in range(12):
            testPicture[i][j] = np.delete(testPicture[i][j], 0, 0)
            testPicture[i][j] = np.delete(testPicture[i][j], -1, 0)
            testPicture[i][j] = np.delete(testPicture[i][j], 0, 1)
            testPicture[i][j] = np.delete(testPicture[i][j], -1, 1)
    '''print('test')
    print(testPicture[0][0])
    print('')
    print(testPicture[0][2])
    print('')'''
    row = []
    for x in testPicture:
        row.append(np.concatenate(x, 1))
    #row1 = np.concatenate(testPicture[0], 1)
    #row2 = np.concatenate(testPicture[1], 1)
    #row3 = np.concatenate(testPicture[2], 1)
    #row = [row1, row2, row3]
    picture = np.concatenate(row)
    #picture = np.flip(picture, 0)
    #picture = np.rot90(picture,  3)
    #for x in row1:
    #print(picture)
    seaMonsterCount = 0
    index = 0
    while True:
        seaMonsterCount = 0
        #print('')
        for y in range(len(picture[0])):
            #tail = False
            #seg1 = False
            #seg2 = False
            for x in range(len(picture)):
                try:
                    if (picture[y][x] == '#' and picture[y + 1][x + 1] == '#') and (picture[y][x + 5] == '#' and picture[y][x + 6] == '#' and picture[y + 1][x + 7] == '#' and picture[y + 1][x + 4] == '#') and (picture[y][x + 11] == '#' and picture[y][x + 12] == '#' and picture[y + 1][x + 13] == '#' and picture[y + 1][x + 10] == '#') and (picture[y][x + 17] == '#' and picture[y][x + 18] == '#' and picture[y - 1][x + 18] == '#' and picture[y + 1][x + 16] == '#' and picture[y][x + 19] == '#'):
                        seaMonsterCount += 1
                        print('monster!!!!!!')
                        #tail = True
                        #print('tail')
                    '''elif (picture[y][x] == '#' and picture[y][x + 1] == '#' and picture[y + 1][x + 2] == '#' and picture[y + 1][x - 1] == '#') and seg1 == False and tail == True:
                        seg1 = True
                        #print('seg1')
                    elif picture[y][x] == '#' and picture[y][x + 1] == '#' and picture[y + 1][x + 2] == '#' and picture[y + 1][x - 1] == '#' and seg1 == True and tail == True and seg2 == False:
                        seg2 = True
                        #print('seg1')
                    elif picture[y][x] == '#' and picture[y][x + 1] == '#' and picture[y - 1][x + 1] == '#' and picture[y + 1][x - 1] == '#' and picture[y][x + 2] == '#'and seg1 == True and seg2 == True and tail == True:
                        seaMonsterCount += 1
                        tail = False
                        seg1 = False
                        seg2 = False
                        print('monster!!!!!!')'''
                except IndexError:
                    continue
        if seaMonsterCount >= 1:
            break
        if index == 4:
            picture = np.flip(picture, 1)
        picture = np.rot90(picture,  1)
        index += 1
        #print('rotate')
    countRough = 0
    #print(picture)
    for x in picture:
        countRough += (x == '#').sum()   
    print(countRough - (seaMonsterCount * 15))

def main():
    with open('input.txt') as f:
        pictures = f.read().split('\n\n')
    #pictures = [i.split() for i in pictures]
    print(len(pictures))
    grid = problem1(pictures)
    problem2(grid)
    #checkBorder(np.array(pictures[0].split()[2:]), np.array(pictures[1].split()[2:]))
    #print(np.array(pictures[0]))
    '''test = pictures[0][2:]
    test = [list(i) for i in test]
    for x in np.array(test):
        print(x)
    print('')
    for x in np.flip(np.array(test), 0):
        print(x)
    print('')
    for x in np.rot90(np.array(test)):
        print(x)'''

if __name__ == '__main__':
    main()