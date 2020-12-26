import ast 
from time import time

def problem1(paths):
    tiles = {}
    for path in paths:
        i = 0
        coordinates = [0, 0, 0]
        while True:
            try:
                if path[i] == 'e':
                    coordinates[0] += 1
                    coordinates[1] -= 1                    
                    i += 1
                elif path[i] == 'w':
                    coordinates[0] -= 1
                    coordinates[1] += 1 
                    i += 1
                elif path[i] + path[i + 1] == 'se':
                    coordinates[1] -= 1
                    coordinates[2] += 1
                    i += 2
                elif path[i] + path[i + 1] == 'ne':
                    coordinates[0] += 1
                    coordinates[2] -= 1
                    i += 2
                elif path[i] + path[i + 1] == 'sw':
                    coordinates[0] -= 1
                    coordinates[2] += 1
                    i += 2
                elif path[i] + path[i + 1] == 'nw':
                    coordinates[1] += 1
                    coordinates[2] -= 1
                    i += 2
            except IndexError:
                if str(coordinates) not in tiles:
                    tiles[str(coordinates)] = 'black'
                else:
                    if tiles[str(coordinates)] == 'black':
                        tiles[str(coordinates)] = 'white'
                    else:
                        tiles[str(coordinates)] = 'black'
                break
    #print(list(tiles.values()).count('black'))
    return tiles


def checkNeighbors(tile, tiles):
    neighbors = [[tile[0] + 1, tile[1] - 1, tile[2]], [tile[0], tile[1] - 1, tile[2] + 1], [tile[0] - 1, tile[1], tile[2] + 1], [tile[0] - 1, tile[1] + 1, tile[2]], [tile[0], tile[1] + 1, tile[2] - 1], [tile[0] + 1, tile[1], tile[2] - 1]]
    count = 0
    for neighbor in neighbors:
        if str(neighbor) in tiles:
            count += 1
    return count


def problem2(tiles):

    for index in range(100):
        tiles = {k:v for k,v in tiles.items() if v != 'white'}
        newTiles = tiles.copy()
        for tile in tiles:
            tile = ast.literal_eval(tile)
            moreTile = [tile, [tile[0] + 1, tile[1] - 1, tile[2]], [tile[0], tile[1] - 1, tile[2] + 1], [tile[0] - 1, tile[1], tile[2] + 1], [tile[0] - 1, tile[1] + 1, tile[2]], [tile[0], tile[1] + 1, tile[2] - 1], [tile[0] + 1, tile[1], tile[2] - 1]]
            for x in moreTile:
                count = checkNeighbors(x, tiles)
                if str(x) in tiles and (count == 0 or count > 2):
                    newTiles[str(x)] = 'white'
                elif count == 2: 
                    newTiles[str(x)] = 'black'
        tiles = newTiles
    print(list(tiles.values()).count('black'))

            
def main():
    startTime = time()
    with open('input.txt') as f:
        paths = f.read().splitlines()
    temp = problem1(paths)
    problem2(temp)
    print('runtime: {}'.format(time() - startTime))


if __name__ == '__main__':
    main()