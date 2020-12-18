
def checkNeighbors(x, y, z, w, cubes):
    count = 0
    for wumbo in range(w - 1, w + 2):
        if 0 <= wumbo < len(cubes):
            for depth in range(z - 1, z + 2):
                if 0 <= depth < len(cubes[0]):
                    for row in range(y - 1, y + 2):
                        if 0 <= row < len(cubes[0][0]):
                            for column in range(x - 1, x + 2):     
                                if 0 <= column < len(cubes[0][0][0]):   
                                    if (cubes[wumbo][depth][row][column]) == '#' and not (depth == z and row == y and column == x and wumbo == w):
                                        count += 1
    return count


def problem2(cubes):
    i = 0
    location = {}
    while i < 6:
    for y in cubes:
        for x in y:
            if x 

        depth = cubes[0]
        for w, wumbo in enumerate(newCubes):
            for z, depth in enumerate(wumbo):
                for y, row in enumerate(depth):
                    for x in range(len(row)):
                        count = checkNeighbors(x, y, z, w, cubes)
                        if count == 3 and cubes[w][z][y][x] == '.': 
                            newCubes[w][z][y][x] = '#'
                        elif (count == 3 or count == 2) and cubes[w][z][y][x] == '#': 
                            newCubes[w][z][y][x] = '#'
                        else:
                            newCubes[w][z][y][x] = '.'                     
                    total += newCubes[w][z][y].count('#')
        
        cubes = newCubes
        i += 1
        print(total)


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        cubes = [list(i) for i in lines]
    problem2([[cubes]])


if __name__ == '__main__':
    main()