
def checkNeighbors(x, y, z, cubes):
    count = 0
    for depth in range(z - 1, z + 2):
        if 0 <= depth < len(cubes):
            for row in range(y - 1, y + 2):
                if 0 <= row < len(cubes[0]):
                    for column in range(x - 1, x + 2):     
                        if 0 <= column < len(cubes[0][0]):   
                            if (cubes[depth][row][column]) == '#' and not (depth == z and row == y and column == x):

                                count += 1
    return count

def problem1(cubes):
    i = 0
    while i < 6:
        total = 0
        for z in cubes:
            for y in z:
                y.insert(0,'.')
                y.append('.')
            z.insert(0, ['.'] * len(z[0]))
            z.append(['.'] * len(z[0]))
        cubes.insert(0, [['.'] * len(cubes[0][0])] * len(cubes[0]))
        cubes.append([['.'] * len(cubes[0][0])] * len(cubes[0]))

        newCubes = [[ ['.' for col in range(len(cubes[0][0]))] for col in range(len(cubes[0]))] for row in range(len(cubes))] 

        depth = cubes[0]
        for z, depth in enumerate(newCubes):
            for y, row in enumerate(depth):
                for x in range(len(row)):
                    count = checkNeighbors(x, y, z, cubes)
                    if count == 3 and cubes[z][y][x] == '.': 
                        newCubes[z][y][x] = '#'
                    elif (count == 3 or count == 2) and cubes[z][y][x] == '#': 
                        newCubes[z][y][x] = '#'
                    else:
                        newCubes[z][y][x] = '.'
                    
                print(newCubes[z][y])
                total += newCubes[z][y].count('#')
            print("########################")
        cubes = newCubes
        i += 1
        print(total)


def main():
    with open('input1.txt') as f:
        lines = f.read().splitlines()
        cubes = [list(i) for i in lines]
    problem1([cubes])

if __name__ == '__main__':
    main()