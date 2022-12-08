import time

def p1(trees):
    vis = set([])
        
    #left
    for y in range(0, len(trees)):
        left = -1
        for x in range(0, len(trees[0])):
            if trees[y][x] > left:
                left = trees[y][x]
                vis.add("[" + str(x) + "," + str(y) + "]")
    
    #right
    for y in range(0, len(trees)):
        right = -1
        for x in range(len(trees[0]) -1, -1, -1):
            if trees[y][x] > right:
                right = trees[y][x]
                vis.add("[" + str(x) + "," + str(y) + "]")
                
    #up
    for x in range(0, len(trees[0])):
        up = -1
        for y in range(len(trees) -1, -1, -1):
            if trees[y][x] > up:
                up = trees[y][x]
                vis.add("[" + str(x) + "," + str(y) + "]")
    
    #down
    for x in range(0, len(trees[0])):
        down = -1
        for y in range(0, len(trees)):
            if trees[y][x] > down:
                down = trees[y][x]
                vis.add("[" + str(x) + "," + str(y) + "]")
                
    print(len(vis))
    
    
def p2(trees):
    score = []

    for j, y in enumerate(trees):
        for k, x in enumerate(y):
            if k == 0 or k == len(trees[0]) - 1 or j == 0 or j == len(trees):
                continue 

            #right
            right = 0
            for i in range(k + 1, len(trees[0])):
                right += 1
                if trees[j][i] >= x:
                    break
                
           #left
            left = 0
            for i in range(k - 1, -1, -1):
                left += 1
                if trees[j][i] >= x:
                    break
            
            #up
            up = 0
            for i in range(j - 1, -1, -1):
                up += 1
                if trees[i][k] >= x:
                    break
                
            #down
            down = 0
            for i in range(j + 1, len(trees)):
                down += 1
                if trees[i][k] >= x:
                    break
                
            score.append(right * left * up * down)
    print(max(score))
    
def main():
    with open('AoC2022/Day08/input.txt') as f:
        input = f.read().splitlines()
    trees = []
    for i, x in enumerate(input):
        trees.append([])
        for y in x:
            trees[i].append(int(y))
            
    p1(trees)
    p2(trees)
  

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))