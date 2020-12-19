
def traversal(map, down, right):
    xMove = 0
    count = 0
    mapLen = len(map[0])
    for i, line in enumerate(map):
        if i % down == 0:
            if line[xMove] == '#':
                count += 1
            xMove = (xMove + right) % mapLen
   # print(count)
    return count

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    #print(len(lines))
    #overall = 0
    #overall = traversal(lines, 1, 3)
    #overall *= traversal(lines, 1, 1)
    #overall *= traversal(lines, 1, 5)
    #overall *= traversal(lines, 1, 7)
    #overall *= traversal(lines, 2, 1)
    #print(overall)

    trees = 0
    bestTrees = 0
    for right in range(len(lines[0])):
        for down in range(1, 5):
            if right == 0 and down > 1:
                continue
            trees = traversal(lines, down, right)
            if trees < bestTrees or (right == 0 and down == 1):
                bestTrees = trees
                bestRight = right
                bestDown = down
    print(bestTrees)
    print(bestRight)
    print(bestDown)

if __name__ == "__main__":
    main()